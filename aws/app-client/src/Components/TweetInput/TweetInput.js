
import React, { Component } from 'react';
import './TweetInput.scss';


export default class TweetInput extends Component {
	constructor(props) {
		super(props);

		this.state = {
			title: '',
		};

		this.onTitleChange = this.onTitleChange.bind(this);
		this.onSubmit = this.onSubmit.bind(this);
	}

	render() {
		return (
			<div className='Tweet-input'>
				<input className='Tweet-input__title' placeholder='@Twitter Handle...' value={this.state.title} onChange={(e) => this.onTitleChange(e)} />
				<button className='Tweet-input__submit-btn' onClick={this.onSubmit} disabled={!this.state.title}>Submit</button>
			</div>
		);
	}

	onTitleChange(e) {
		this.setState({ title: e.target.value });
	}


	//TODO: Can we get the Tweet of the Tweet posted here and send it in the Tweet object argument for this.props.onSubmit(Tweet)
	onSubmit() {
		this.setState({title: ''});
		const Tweet = {
				title: this.state.title,
				upvotes: 0,
				comments: []
		}

		this.props.onSubmit(Tweet)
	}
}
