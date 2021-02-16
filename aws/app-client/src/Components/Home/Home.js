import React, { Component } from 'react';
import './Home.scss';

import TweetInput from '../TweetInput/TweetInput';
import TweetList from '../TweetList/TweetList';
import { API } from "aws-amplify";

export default class Home extends Component {
  constructor(props) {
    super(props);

    this.state = {
      Tweets: []
    };

    this.onSubmitTweet = this.onSubmitTweet.bind(this);
    this.onUpvote = this.onUpvote.bind(this);
    this.onDelete = this.onDelete.bind(this);
  }

  async componentWillMount() {
    try {
      const Tweets = await this.Tweets();
      this.setState({ Tweets });
    } catch (e) {
      alert(e);
    }
  }

  Tweets() {
   return API.get("tweets", "/tweets");
  }

  onSubmitTweet(Tweet) {
    API.post("tweets", "/tweets", {
			body: Tweet
		}).then(res => {
      const newTweets = this.state.Tweets.concat(res);
      this.setState({Tweets: newTweets})
    });
  }

  onUpvote(e, Tweet) {

    e.preventDefault();
    API.patch("tweets", `/tweets/${Tweet.id}`, {
			body: Tweet
		}).then(res => {
      const newTweets = this.state.Tweets.map(newTweet => {
        if(newTweet.id === res.id) {
          newTweet.upvotes = newTweet.upvotes + 1;
        }
        return newTweet
      });

      this.setState({Tweets: newTweets});
    });

  }

  onDelete(e, Tweet) {
    e.preventDefault();
    API.del("tweets", `/tweets/${Tweet.id}`).then(res => {
      const remainingTweets = this.state.Tweets.filter(remainingTweet => remainingTweet.id !== Tweet.id);

      this.setState({Tweets: remainingTweets});
    });

  }

  render() {
    return (
      <div className="Home">
        <TweetInput onSubmit={this.onSubmitTweet} />
        <TweetList Tweets={this.state.Tweets} onUpvote={this.onUpvote} onDelete={this.onDelete} />
      </div>
    );
  }

}
