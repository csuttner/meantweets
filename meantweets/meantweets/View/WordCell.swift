//
//  WordCell.swift
//  meantweets
//
//  Created by Clay Suttner on 2/1/21.
//  Copyright © 2021 Fairchild-Suttner. All rights reserved.
//

import UIKit

class WordCell: UITableViewCell {
    
    let wordLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.preferredFont(forTextStyle: .title3)
        return label
    }()
    
    let scoreLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.preferredFont(forTextStyle: .title3)
        return label
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUi()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setupUi() {
        contentView.addSubview(wordLabel)
        wordLabel.anchor(
            left: contentView.leftAnchor,
            centerY: contentView.centerYAnchor,
            paddingLeft: .padding
        )
        
        contentView.addSubview(scoreLabel)
        scoreLabel.anchor(
            right: contentView.rightAnchor,
            centerY: contentView.centerYAnchor,
            paddingRight: .padding
        )
    }
    
    func configure(for word: Word) {
        wordLabel.text = word.word
        scoreLabel.text = String(word.score)
    }
    
}
