//
//  WordTable.swift
//  meantweets
//
//  Created by Clay Suttner on 2/1/21.
//  Copyright © 2021 Fairchild-Suttner. All rights reserved.
//

import UIKit

class WordTable: UITableView {
    
    var words: [Word]! {
        didSet {
            reloadData()
        }
    }
    
    let identifier = "wordcell"
    
    init() {
        super.init(frame: .zero, style: .plain)
        register(WordCell.self, forCellReuseIdentifier: identifier)
        dataSource = self
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

extension WordTable: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return words.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = dequeueReusableCell(withIdentifier: identifier) as! WordCell
        cell.configure(for: words[indexPath.row])
        return cell
    }
}

