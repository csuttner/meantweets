//
//  ResultsViewController.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import UIKit

class ResultsView: UIViewController {
    
    //MARK: Properties
    
    let handle: String
    
    //MARK: UI Elements
    
    let table = WordTable()
    
    let outputLabel: UILabel = {
        let label = UILabel()
        label.textColor = .black
        label.lineBreakMode = .byWordWrapping
        label.numberOfLines = 0
        label.font = UIFont.preferredFont(forTextStyle: .title3)
        return label
    }()
    
    //MARK: Init
    
    init(handle: String) {
        self.handle = handle
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    //MARK: Lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUi()
        
        // Mock request that gets data from local JSON file
        sendMockRequest()
    }
    
    // Real request method
    func sendRequest() {
        let mtRequest = MTRequest(handle: handle)
        mtRequest.send { [weak self] result in
            switch result {
            case .failure(let error):
                print(error)
            case .success(let mtResponse):
                self?.loadDataToViews(from: mtResponse)
            }
        }
    }
    
    func sendMockRequest() {
        let mtRequest = MTRequest(handle: handle)
        let mtResponse = mtRequest.sendMock()
        loadDataToViews(from: mtResponse)
    }
    
    func loadDataToViews(from response: MTResponse) {
        outputLabel.text =
            "handle: \(response.handle)\n" +
            "tweet count: \(response.tweet_count)\n" +
            "distinct words: \(response.unique_words)"
        table.words = response.words
    }

    //MARK: UI Setup
    
    func setupUi() {
        view.backgroundColor = .white
        
        view.addSubview(outputLabel)
        outputLabel.anchor(
            top: view.topAnchor,
            left: view.leftAnchor,
            right: view.rightAnchor,
            paddingTop: .padding,
            paddingLeft: .padding,
            paddingRight: .padding
        )
        
        view.addSubview(table)
        table.anchor(
            top: outputLabel.bottomAnchor,
            left: view.leftAnchor,
            bottom: view.bottomAnchor,
            right: view.rightAnchor
        )
    }
    
}
