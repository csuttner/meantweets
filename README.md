# **MeanTweets**

### <a href="https://github.com/csuttner/meantweets/wiki">Project Wiki</a>

### Show who people are online

iOS app and containerized backend, applying NLP to Twitter user data for obtaining insight about online behavior.

### Setup
  1. Clone repository:
  ```
    git clone https://github.com/csuttner/meantweets.git
  ```
  
  2. To query Twitter you must add API keys and Consumer tokens within a `secrets.py` file in your working directory.
  
 ```
    nano secrets.py
 ```
   Copy and Paste keys & tokens in the following format and exit the editor (Ctrl-X, Y, Enter).
  ```
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
  ```
