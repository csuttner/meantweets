import React from 'react';
import { Route } from 'react-router-dom';
import './App.scss';

import Home from '../Home/Home';
import TweetDetails from '../TweetDetails/TweetDetails';

const App = () => {
  return (
    <div className="App">

      <Route exact={true} path='/' component={Home} />
      <Route path='/tweets/:TweetId' component={TweetDetails} />
    </div>
  );
}

export default App;
