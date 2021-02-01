//
//  TweetRequest.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import Foundation

enum RequestError: Error {
    case noDataAvailable
    case cantProcessData
}

struct MTRequest {
    
    let resourceURL: URL

    init(handle: String) {
        let resourceString = "http://localhost:5000/meantweet/\(handle)"
        guard let resourceURL = URL(string: resourceString) else {
            fatalError("Invalid URL String")
        }
        self.resourceURL = resourceURL
        print(resourceURL)
    }
    
    func send(completion: @escaping(Result<MTResponse, RequestError>) -> Void) {
        let dataTask = URLSession.shared.dataTask(with: resourceURL) { data, _, _ in
            guard let jsonData = data else {
                completion(.failure(.noDataAvailable))
                return
            }
            
            do {
                let decoder = JSONDecoder()
                let mtResponse = try decoder.decode(MTResponse.self, from: jsonData)
                completion(.success(mtResponse))
            } catch {
                completion(.failure(.cantProcessData))
            }
        }
        dataTask.resume()
    }
}
