# instagram-spammer
To get this working:

## For local runs:
- geckodriver exe from https://github.com/mozilla/geckodriver/releases/tag/v0.29.1

## For Heroku cloud runs:
### Buildpacks:
- heroku buildpacks:add -a instagram-spammer-prod --index 1 https://github.com/heroku/heroku-buildpack-chromedriver
- heroku buildpacks:add -a instagram-spammer-prod --index 2 https://github.com/heroku/heroku-buildpack-google-chrome

### Environment variables:
- heroku config:set -a instagram-spammer-prod GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google_chrome
- heroku config:set -a instagram-spammer-prod CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
