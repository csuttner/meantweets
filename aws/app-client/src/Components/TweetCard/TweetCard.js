import React from 'react';
import { NavLink } from 'react-router-dom';
import './TweetCard.scss';

import UpvoteIcon from '../../Icons/UpvoteIcon';
// import CommentIcon from '../../Icons/CommentIcon';
import DeleteIcon from '../../Icons/DeleteIcon';



const TweetCard = ({Tweet, onUpvote, onDelete}) => {
	const pathname = `/tweets/${Tweet.id}`;

	return (
		<div>
			<div className='Tweet-card__title-delete'>
				<div className='Tweet-card__title'>{Tweet.title}</div>
				<div className='Tweet-card__delete-icon-container' onClick={(e) => onDelete(e, Tweet)}>
					<DeleteIcon className='Tweet-card__delete-icon'/>
				</div>
			</div>
			<div className='Tweet-card__body'>{JSON.stringify(Tweet.body, null, 2)}</div>
		</div>
	);
}

export default TweetCard;
