# **MEAN tweets**
## **Show who people are when they are online**

MVP: create user-friendly platform for retrieving the average/mean tweet (output) from a twitter user's (input) tweet history.  

Frontend: input -> Twitter handle / account name
  1. iOS application
  2. test level 'user' scripts
  3. Website
  4. Twitter bot

Backend:
  1. API
  2. Machine Learning NLP model
      a. starting point: stripping stop words, word count, similar word buckets
  3. Database that stores results.  
      a. need to figure out what type of DB.

Test driven development.
 - start with a failing test
 - write the shortest amount of code to make that test pass
 - refactor code as needed

Do we start from nothing??
How do we organize best for TDD??






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

  3. Do more stuffs
