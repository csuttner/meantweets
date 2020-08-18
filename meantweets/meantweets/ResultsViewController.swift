//
//  ResultsViewController.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import UIKit

class ResultsViewController: UIViewController {
    
    let outputTextView: UITextView = {
        let textView = UITextView()
        textView.backgroundColor = .white
        textView.font = UIFont.preferredFont(forTextStyle: .title3)
        textView.text = "Why is Congress scheduled to meet (on Post Office) next Monday, during the Republican Convention, rather than now, while the Dems are having their Convention. They are always playing games. GET TOUGH REPUBLICANS!!!"
        return textView
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(outputTextView)
    }
}
