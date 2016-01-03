## Predicting Retweetability of a tweet:

This project is based on the paper [Factors Impacting Retweet in Twitter Network](http://www-users.cs.umn.edu/~echi/papers/2010-socialcom/2010-06-25-retweetability-cameraready-v3.pdf). 
We gathered content and contexual features from a dataset of tweets and it is used to identify factors associated with retweet rate.  
Features used include: followers_count, friends_count, user_mentions, urls_count, hashtags_count, favourites_count  

#### Dataset:
https://archive.org/details/archiveteam-json-twitterstream-2012 (27 million tweets)  


Principle Component Analysis (PCA) and Generalised Linear Modelling were used to analyze the factors affecting retweet rate.

### Directories:

pRetweet  
 |__ data  
...|__ 01  
...|__ 02  
...|__  :  
...|__ 31  
...|__ dw.sh           : download datasets  
...|__ unbzipall.sh    : for each directory in 01..31, unbzip folder locally (using unbzip.sh)  
...|__ formatall.sh    : go to each directory, format json to correct format using proper.rb, puts formatted files in 'out' folder  
...|__ populateall.sh  : get all data from out folder and insert into db  
...|__ unbzip.sh  
...|__ proper.rb  
...|__ json_to_db.py  
 |__ pca.py       :  
 |__ linear.py    :  
 |__ graph*.py ..  :  


### Instructions:

1. Download Datasets using dw.sh. There are 31 .zip files. Unzip all and put unzipped folders (01..31) in data folder.

2. Run unbzipall.sh

3. Run formatall.sh

4. Create MySQL database 'pretweet'. Put proper tablename, username and password in json_to_db.py file
   Run populateall.sh

Now the database contains all the records.

5. Run pca.py, linear.py etc for analysis of data


