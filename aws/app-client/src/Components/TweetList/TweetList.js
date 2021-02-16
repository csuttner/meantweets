import React from 'react';
import './TweetList.scss';

import TweetCard from '../TweetCard/TweetCard';

const TweetList = ({Tweets, onUpvote, onDelete}) => {
	const TweetList = Tweets.sort((a, b) => a.title > b.title ? 1 : a.title < b.title ? -1 : 0).map(Tweet => <TweetCard key={Tweet.id} Tweet={Tweet} onUpvote={onUpvote} onDelete={onDelete}/>);
	return (
		<div className='Tweet-list'>
			{TweetList}
		</div>
	);
}

export default TweetList;
