//
//  ViewController.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import UIKit

class MainViewController: UIViewController {
    
    // MARK: - UI Elements
    
    lazy var mainStack: UIStackView = {
        let mainStack = UIStackView()
        mainStack.axis = .vertical
        mainStack.alignment = .center
        
        let subStack = UIStackView()
        subStack.axis = .horizontal
        
        let appLogo = UILabel()
        appLogo.textColor = .white
        appLogo.font = UIFont.init(name: "HelveticaNeue-Bold", size: 40)
        appLogo.text = ">:|"
        appLogo.transform = CGAffineTransform(rotationAngle: .pi / 2)
        subStack.addArrangedSubview(appLogo)

        let appName = UILabel()
        appName.textColor = .white
        appName.font = UIFont.boldSystemFont(ofSize: 40)
        appName.text = " mean tweets"
        subStack.addArrangedSubview(appName)
        
        mainStack.addArrangedSubview(subStack)
        
        let searchBar = UISearchBar()
        searchBar.placeholder = "@twitter_handle"
        searchBar.searchBarStyle = .minimal
        searchBar.searchTextField.backgroundColor = .white
        
        let anotherStack = UIStackView()
        anotherStack.axis = .vertical
        
        anotherStack.addArrangedSubview(mainStack)
        anotherStack.addArrangedSubview(searchBar)
        
        return anotherStack
    }()
    
    let submitButton: UIButton = {
        let button = UIButton()
        button.setTitle("  submit  ", for: .normal)
        button.titleLabel?.font = UIFont.preferredFont(forTextStyle: .largeTitle)
        button.titleLabel?.textColor = .systemBlue
        button.layer.borderWidth = 2
        button.layer.borderColor = CGColor(srgbRed: 1, green: 1, blue: 1, alpha: 1)
        button.sizeToFit()
        button.layer.cornerRadius = button.frame.height / 2
        return button
    }()
    
    // MARK: - Lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUpUI()
    }
    
    // MARK: - UI Setup
    
    func setUpUI() {
        let height = view.frame.height
        let padding: CGFloat = 16
        
        setUpStack(height: height, padding: padding)
        setUpButton(height: height)
        
        view.backgroundColor = .systemBlue
    }
    
    func setUpStack(height: CGFloat, padding: CGFloat) {
        view.addSubview(mainStack)
        mainStack.spacing = padding
        mainStack.translatesAutoresizingMaskIntoConstraints = false
        mainStack.leftAnchor.constraint(equalTo: view.leftAnchor, constant: padding).isActive = true
        mainStack.rightAnchor.constraint(equalTo: view.rightAnchor, constant: -padding).isActive = true
        mainStack.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        mainStack.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -height / 6).isActive = true
    }
    
    func setUpButton(height: CGFloat) {
        view.addSubview(submitButton)
        submitButton.translatesAutoresizingMaskIntoConstraints = false
        submitButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        submitButton.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: height / 6).isActive = true
        submitButton.addTarget(self, action: #selector(didTapSubmit), for: .touchUpInside)
    }

    // MARK: - Selectors
    
    @objc func didTapSubmit() {
        let vc = ResultsViewController()
        present(vc, animated: true, completion: nil)
    }
    
}

