# -*- coding: utf-8 -*-
"""intersection_over_union.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OfhslJ9ERQChFctvhmyXnnNxGc0QCMSB

IOU : is a metric that messuares how similar a predicted bounding box is to the original bounding box.


![index.png](data:image/png;base64,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)

IOU > 0.5 == decent

IOU > 0.7 == good

IOU > 0.9 == perfect
"""

import torch

def intersection_over_union(boxes_preds, boxes_labels, box_format="midpoint"):
    # box_preds has a size of (Batch_size , 4) where 4 represent (x,y,w,h in case of midpoint rep) or (x1,y1,x2,y2 in case of croners rep)
    if box_format == "midpoint":
        box1_x1 = boxes_preds[..., 0:1] - boxes_preds[..., 2:3] / 2
        box1_y1 = boxes_preds[..., 1:2] - boxes_preds[..., 3:4] / 2
        box1_x2 = boxes_preds[..., 0:1] + boxes_preds[..., 2:3] / 2
        box1_y2 = boxes_preds[..., 1:2] + boxes_preds[..., 3:4] / 2
        box2_x1 = boxes_labels[..., 0:1] - boxes_labels[..., 2:3] / 2
        box2_y1 = boxes_labels[..., 1:2] - boxes_labels[..., 3:4] / 2
        box2_x2 = boxes_labels[..., 0:1] + boxes_labels[..., 2:3] / 2
        box2_y2 = boxes_labels[..., 1:2] + boxes_labels[..., 3:4] / 2

    elif box_format == "corners":
        box1_x1 = boxes_preds[..., 0:1]
        box1_y1 = boxes_preds[..., 1:2]
        box1_x2 = boxes_preds[..., 2:3]
        box1_y2 = boxes_preds[..., 3:4]
        box2_x1 = boxes_labels[..., 0:1]
        box2_y1 = boxes_labels[..., 1:2]
        box2_x2 = boxes_labels[..., 2:3]
        box2_y2 = boxes_labels[..., 3:4]

    x1 = torch.max(box1_x1, box2_x1)
    print (x1)
    y1 = torch.max(box1_y1, box2_y1)
    x2 = torch.min(box1_x2, box2_x2)
    y2 = torch.min(box1_y2, box2_y2)

    # Need clamp(0) in case they do not intersect, then we want intersection to be 0
    intersection = (x2 - x1).clamp(0) * (y2 - y1).clamp(0)
    box1_area = abs((box1_x2 - box1_x1) * (box1_y2 - box1_y1))
    box2_area = abs((box2_x2 - box2_x1) * (box2_y2 - box2_y1))

    #devide by zero case
    return intersection / (box1_area + box2_area - intersection + 1e-6)

def intersection_over_union_wh(boxes1, boxes2):
    #same as the above function but instead in case of W, H 
    #will be used in DataSet class
    intersection = torch.min(boxes1[..., 0], boxes2[..., 0]) * torch.min(boxes1[..., 1], boxes2[..., 1])
    union = (boxes1[..., 0] * boxes1[..., 1] + boxes2[..., 0] * boxes2[..., 1] - intersection)
    return intersection / union

x = torch.tensor([[0.2800, 0.2200],
        [0.3800, 0.4800],
        [0.9000, 0.7800],
        [0.0700, 0.1500],
        [0.1500, 0.1100],
        [0.1400, 0.2900],
        [0.0200, 0.0300],
        [0.0400, 0.0700],
        [0.0800, 0.0600]])

y = torch.tensor([0.7180, 0.8408])

IOU = intersection_over_union_wh(x,y)
print (IOU)
