//
//  TweetModel.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import Foundation

struct MTResponse: Decodable {
    let handle: String
    let tweet_count: Int
    let distinct_words: Int
    let words: [Word]
}

struct Word: Decodable {
    let word: String
    let count: Int
    let score: Int
}
