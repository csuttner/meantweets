//
//  TweetModel.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import Foundation

struct Tweet: Decodable {
    let handle: String
    let output: String
}
