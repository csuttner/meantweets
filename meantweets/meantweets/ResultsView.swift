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
        sendRequest()
    }
    
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
    
    func loadDataToViews(from response: MTResponse) {
        outputTextView.text = response.handle
        // TODO: logic for loading other data from the response
    }
    
    //MARK: UI Elements
    
    let outputTextView: UITextView = {
        let textView = UITextView()
        textView.backgroundColor = .white
        textView.font = UIFont.preferredFont(forTextStyle: .title3)
        return textView
    }()
    
    //MARK: UI Setup
    
    func setupUi() {
        view.backgroundColor = .white
        view.addSubview(outputTextView)
        
        let padding: CGFloat = 16
        
        outputTextView.anchor(
            top: view.topAnchor,
            left: view.leftAnchor,
            bottom: view.bottomAnchor,
            right: view.rightAnchor,
            paddingTop: padding,
            paddingLeft: padding,
            paddingBottom: padding,
            paddingRight: padding
        )
    }
    
}
