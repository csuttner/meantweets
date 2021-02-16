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
        let resourceString = "https://api.meantweets.io/meantweet/\(handle)"
        guard let resourceURL = URL(string: resourceString) else {
            fatalError("Invalid URL String")
        }
        self.resourceURL = resourceURL
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
    
    func sendMock() -> MTResponse {
        let path = Bundle.main.path(forResource: "MockData", ofType: "json")
        let json = try! String(contentsOfFile: path!, encoding: .utf8)
        let data = json.data(using: .utf8)!
        let decoder = JSONDecoder()
        return try! decoder.decode(MTResponse.self, from: data)
    }
}
