// const body = Tweet ? Tweet.body : ''; line 40
// <div className='Tweet-details__body'>{body}</div> line 50

import React, { Component } from 'react';
import './TweetDetails.scss';
import { API } from "aws-amplify";
import UpvoteIcon from '../../Icons/UpvoteIcon';

export default class TweetDetails extends Component {
	constructor(props) {
		super(props);

		this.state = {
			Tweet: null,
			comment: ''
		};

		this.onCommentChange = this.onCommentChange.bind(this);
		this.onUpvoteChange = this.onUpvoteChange.bind(this);
		this.onSubmit = this.onSubmit.bind(this);
	}

	async componentWillMount() {
		try {
			const Tweet = await this.getTweet();
			this.setState({ Tweet });
		} catch (e) {
			alert(e);
		}
	}

	getTweet() {
		return API.get("tweets", this.props.location.pathname);
	}

	render() {
		let commentLabel = 'There are no comments on this Tweet';
		const Tweet = this.state.Tweet;
		const title = Tweet ? Tweet.title : '';
		const upvotes = Tweet ? Tweet.upvotes : 0;

		let commentList = null
		if (Tweet && Tweet.comments && Tweet.comments.length) {
			commentList = Tweet.comments.map(comment => <div key={comment} className='Tweet-details__comment'>{comment}</div>);
			commentLabel = 'Comments'
		}

		return (
			<div className='Tweet-details'>
				<div className='Tweet-details__tweet'>
					<div className='Tweet-details__title'>{title}</div>
					<div className='Tweet-details__upvotes'>
						<UpvoteIcon className='Tweet-details__upvote-icon' />
						<div className='Tweet-details__upvote-count'>{upvotes}</div>
					</div>
				</div>
				<div className='Tweet-details__comment-input'>
					<textarea className='Tweet-details__comment-textarea' placeholder='Type comment here...' value={this.state.comment} onChange={(e) => this.onCommentChange(e)} />
					<button className='Tweet-details__comment-submit' onClick={this.onSubmit} disabled={!this.state.comment}>Save Comment</button>
				</div>
				<div className='Tweet-details__comments'>
					<div className='Tweet-details__comment-label'>{commentLabel}</div>
					{commentList}
				</div>
			</div>
		);
	}

	onCommentChange(e) {
		this.setState({ comment: e.target.value });
	}

	onUpvoteChange(e) {
		this.setState({ upvotes: this.state.upvotes + 1 });
		let updated_Tweet = this.state.Tweet;
		updated_Tweet.upvotes = this.state.upvotes;
	}

	onSubmit() {
		let updated_Tweet = this.state.Tweet;
		updated_Tweet.comments.push(this.state.comment);
		this.setState({ Tweet: updated_Tweet, comment: '' });
	}
}
