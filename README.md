# Google Analytics Pageviews Counter

## Description

This is a sample how to implement Google Analytics in static web site without authenticating of users.

There are components.

1. show_pageviews.html - shows pageviews counter.

2. pageviews.js - access to Google Analytics.

3. report_access.js - token to authorize access to Google Analytics.

4. generate_token.py - a tool to generate Google Analytics token.

5. [key name].json - Google analytics service account key file created in Google Analytics Platform APIs and Services.  

## Generate Google Analytics token usage

```
usage: generate_token.py [-h] -k KEYFILEPATH -t TOKENFILEPATH

Generate Google Analytics token v. 1.0.0

optional arguments:
  -h, --help            show this help message and exit
  -k KEYFILEPATH, --keyfilepath KEYFILEPATH
                        Google Analytics json key file path
  -t TOKENFILEPATH, --tokenfilepath TOKENFILEPATH
                        Google Analytics token destination path
``` 

Sample of usage


```bash
generate_token.py -k tech-jogging-blog-98stj21aac52.json -t report_access.js
``` 

## How to run it

1. Generate a token. It's live for 1 hour.
2. Publish 3 files to a web server.
   1. how_pageviews.html
   2. pageviews.js
   3. report_access.js
3. Open show_pageviews.html page. 
4. If you need to keep it running, renew the token every hour.
  