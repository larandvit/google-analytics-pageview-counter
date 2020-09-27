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

Sample of usage in CentOS 8 where the tool and service account file located in /opt/generate_token folder and web site in /var/www/sample.com folder


```bash
python3 /opt/generate_token/generate_token.py -k /opt/generate_token/tech-jogging-blog-98stj21aac52.json -t /var/www/sample.com/report_access.js
``` 

## Prerequisites

1. Install Pyhon library

```bash
sudo pip3 install oauth2client
```

## How to run it

1. Generate a token. It's live for 1 hour.
2. Publish 3 files to a web server.
   1. show_pageviews.html
   2. pageviews.js
   3. report_access.js
3. Open show_pageviews.html page. 
4. If you need to keep it running, renew the token every hour.

## Set up to renew token every 59 minutes

1. Switch to root account.

```bash
sudo su
```

2. Open `crontab` editor.

```bash
crontab -e
```

3. Add the command item.

```
59 * * * * python3 /opt/generate_token/generate_token.py -k /opt/generate_token/tech-jogging-blog-98stj21aac52.json -t /var/www/sample.com/report_access.js
```

It can be optimized by creating a shell script in `launcher.sh` file and placing the command in the shell file. In that case, the time item is.

```
59 * * * * python3 /opt/generate_token/launcher.sh
```

4. Validate your setup.

```bash
crontab -l
```

## Documentation

[Add Google Analytics Pageviews in Static Web Site](https://techjogging.com/add-google-analytics-pageviews-static-web-site.html)
  
