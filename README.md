# **a simple webpage with jellyfin stats**

## requirements
- **linux as this is made for linux**
- python 3.14.6
- python packages `requests` and `python-dotenv`
- web server software to serve the files
- internet (optional)

## folder structure
app.py and .env in the root folder while the .json (created automaticly by app.py), html and css are in /homepage for safe serving without exposing api keys


## setup
1. `git clone https://github.com/23076-sudo/website-homepage`
2. `cd website-homepage`
3. `pip install requests python-dotenv`
4. arrange the files so that index.html styles.css are in the homepage folder and that app.py and .env is in the root folder
5. `cp example.env .env`
6. edit the .env using your prefered text editor
7. run app.py to generate the .json
8. serve the homepage folder with a web server software of your chosing
9. **optional but important to keep stats up to date** by using a cron job
`*/5 * * * * cd /path/to/website-homepage && /usr/bin/python3 app.py`

##  customizing
- swap the links in index.html for your own links if needed
-  replace the images and favicon with your favicon and images
