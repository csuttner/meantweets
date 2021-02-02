//
//  ViewController.swift
//  meantweets
//
//  Created by Clay Suttner on 8/17/20.
//  Copyright © 2020 Fairchild-Suttner. All rights reserved.
//

import UIKit

class MainView: UIViewController {
    
    // MARK: - UI Elements
    
    let labelStack: UIStackView = {
        let stack = UIStackView()
        
        let appLogo = UILabel()
        appLogo.font = UIFont.init(name: "HelveticaNeue-Bold", size: 40)
        appLogo.text = ">:|"
        appLogo.textColor = .white
        appLogo.transform = CGAffineTransform(rotationAngle: .pi / 2)
        
        let appName = UILabel()
        appName.font = UIFont.boldSystemFont(ofSize: 40)
        appName.text = " mean tweets"
        appName.textColor = .white
        
        stack.addArrangedSubview(appLogo)
        stack.addArrangedSubview(appName)
        return stack
    }()
    
    let searchBar: UISearchBar = {
        let searchBar = UISearchBar()
        searchBar.placeholder = "@twitter_handle"
        searchBar.searchBarStyle = .minimal
        searchBar.searchTextField.backgroundColor = .white
        return searchBar
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
    
    // MARK: Lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUi()
        enableDismissKeyboard()
    }
    
    // MARK: Tap Gesture
    
    func enableDismissKeyboard() {
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(dismissKeyboard))
        view.addGestureRecognizer(tapGestureRecognizer)
    }
    
    
    // MARK: Selectors
    
    @objc func didTapSubmit() {
        present(ResultsView(handle: searchBar.text ?? ""), animated: true, completion: nil)
    }
    
    @objc func dismissKeyboard() {
        searchBar.resignFirstResponder()
    }
    
    // MARK: - UI Setup
    
    func setupUi() {
        let height = view.frame.height
        let padding: CGFloat = 16
        
        setUpLabels(height: height)
        setUpSearchBar(padding: padding)
        setUpButton(height: height)
        
        view.backgroundColor = .systemBlue
    }
    
    func setUpLabels(height: CGFloat) {
        view.addSubview(labelStack)
        labelStack.translatesAutoresizingMaskIntoConstraints = false
        labelStack.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        labelStack.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -height / 6).isActive = true
    }
    
    func setUpSearchBar(padding: CGFloat) {
        view.addSubview(searchBar)
        searchBar.anchor(
            top: labelStack.bottomAnchor,
            left: view.leftAnchor,
            right: view.rightAnchor,
            paddingTop: padding,
            paddingLeft: padding,
            paddingRight: padding
        )
    }
    
    func setUpButton(height: CGFloat) {
        view.addSubview(submitButton)
        submitButton.translatesAutoresizingMaskIntoConstraints = false
        submitButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        submitButton.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: height / 6).isActive = true
        submitButton.addTarget(self, action: #selector(didTapSubmit), for: .touchUpInside)
    }

}
