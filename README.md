# **MEAN tweets**

### This is fun code for learning puposes.

Objective: get the average/mean of a twitter user's tweet history.

Input: Twitter handle / account name

Output: a single tweet that averages tweet length and key word usage.

Instructions for running:
  1. Clone repository:
  ```
    git clone https://github.com/skutchiewutch/bizzle.git
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
  
## Docker Setup
```
docker-compose build
```
you only need to build this image once
```
docker-compose up
```
go to http://localhost:5000/ for homepage placeholder
go to http://localhost:5000/meantweet/@clayclayclay to test the barebones api

Once that looks good just add this to your testing workflow 

