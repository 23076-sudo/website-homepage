# **a simple webpage with jellyfin stats**

## requirements
- python 3.14.6
- python packages `requests` and `python-dotenv`
- caddy to serve the files
- internet (optional if jellyfin and webpage are only served from the same device)

## folder structure
app.py and .env in the root folder while the .json (created automaticly by app.py), html and css are in /homepage for save serving without exposing api keys

