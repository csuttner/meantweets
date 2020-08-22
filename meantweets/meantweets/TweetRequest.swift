//
//  TweetRequest.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import Foundation

enum TweetError: Error {
    case noDataAvailable
    case cantProcessData
}

struct TweetRequest {
    
    let resourceURL: URL
    
    
    
    init(handle: String) {
        let resourceString = "http://localhost:5000/meantweet/\(handle)"
        guard let resourceURL = URL(string: resourceString) else {
            fatalError("Invalid URL String")
        }
        self.resourceURL = resourceURL
        print(resourceURL)
    }
    
    func getTweet(completion: @escaping(Result<Tweet, TweetError>) -> Void) {
        let dataTask = URLSession.shared.dataTask(with: resourceURL) { data, _, _ in
            guard let jsonData = data else {
                completion(.failure(.noDataAvailable))
                return
            }
            
            do {
                let decoder = JSONDecoder()
                let tweetResponse = try decoder.decode(Tweet.self, from: jsonData)
                let tweet = tweetResponse
                completion(.success(tweet))
            } catch {
                completion(.failure(.cantProcessData))
                
            }
        }
        dataTask.resume()
    }
}
