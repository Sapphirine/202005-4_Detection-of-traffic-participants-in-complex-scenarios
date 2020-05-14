//
//  Helpers.swift
//  yolov3
//
//  Created by Alexander on 10/07/2019.
//  fine turned by Guanhua Yu on 04/29/2019
//  Copyright © 2019 Alexander. All rights reserved.
//

import Foundation
import UIKit

let labels = ["car","bus","person","bike","truck","motor","train","rider","traffic sign","traffic light"]

struct ColorPallete {
  static let shared = ColorPallete()
  let colors: [CGColor]
  init() {
    colors = [
      ColorPallete.rgba(244,67,54,1), ColorPallete.rgba(33,150,243,1),
      ColorPallete.rgba(156,39,176,1), ColorPallete.rgba(0,150,136,1),
      ColorPallete.rgba(76,175,80,1), ColorPallete.rgba(139,195,74,1),
      ColorPallete.rgba(205,220,57,1), ColorPallete.rgba(255,235,59,1),
      ColorPallete.rgba(255,193,7,1), ColorPallete.rgba(255,152,0,1),
      ]
  }
  
  private static func rgba(_ red: CGFloat, _ green: CGFloat,
                           _ blue: CGFloat, _ alpha: CGFloat) -> CGColor {
    return UIColor(red: red / 255.0, green: green / 255.0,
                   blue: blue / 255.0, alpha: alpha).cgColor
  }
}

let anchors1_tiny: [Float] = [120,220, 184,282,  243,379]
let anchors2_tiny: [Float] = [44,91,  77,135,  111,144]
let anchors3_tiny: [Float] = [9,16,  21,39,  36,55]

let tiny_anchors = [
  "output1": anchors1_tiny,
  "output2": anchors2_tiny,
  "output3": anchors3_tiny,
]

let anchors1: [Float] = [116,90,  156,198,  373,326]
let anchors2: [Float] = [30,61,  62,45,  59,119]
let anchors3: [Float] = [10,13,  16,30,  33,23]

let anchors_416 = [
  "output1": anchors1,
  "output2": anchors2,
  "output3": anchors3
]
