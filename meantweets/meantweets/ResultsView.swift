//
//  ResultsViewController.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import UIKit

class ResultsView: UIViewController {
    
    let handle: String
    
    init(handle: String) {
        self.handle = handle
        super.init(nibName: nil, bundle: nil)
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    let outputTextView: UITextView = {
        let textView = UITextView()
        textView.backgroundColor = .white
        textView.font = UIFont.preferredFont(forTextStyle: .title3)
        return textView
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUpView()
        fireRequest()
    }
    
    func setUpView() {
        view.backgroundColor = .white
        view.addSubview(outputTextView)
        
        let padding: CGFloat = 16
        
        outputTextView.anchor(top: view.topAnchor, left: view.leftAnchor, bottom: view.bottomAnchor, right: view.rightAnchor, paddingTop: padding, paddingLeft: padding, paddingBottom: padding, paddingRight: padding)
    }
    
    func fireRequest() {
        let tweetRequest = TweetRequest(handle: handle)
        tweetRequest.getTweet(completion: { [weak self] result in
            switch result {
            case .failure(let error):
                print(error)
            case .success(let tweet):
                DispatchQueue.main.async { [weak self] in
                    self?.outputTextView.text = tweet.handle
                }
            }
        })
    }
}
