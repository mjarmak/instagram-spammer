# instagram-spammer
To get this working:

## For local runs:
- geckodriver exe: https://github.com/mozilla/geckodriver/releases/tag/v0.29.1
- chromedriver.exe: https://chromedriver.chromium.org/downloads and get your specific version

## For Heroku cloud runs:
### Buildpacks:
- heroku buildpacks:add -a instagram-spammer-production --index 2 https://github.com/heroku/heroku-buildpack-google-chrome
- heroku buildpacks:add -a instagram-spammer-production --index 1 https://github.com/heroku/heroku-buildpack-chromedriver

### Environment variables:
- Check the chrome binary path here: https://github.com/heroku/heroku-buildpack-google-chrome#selenium
- Check the chrome driver path here: https://github.com/heroku/heroku-buildpack-chromedriver
- heroku config:set -a instagram-spammer-production GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google-chrome or use the buildpack default $GOOGLE_CHROME_BIN
- heroku config:set -a instagram-spammer-production CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver

### Python buildpack
- Go to https://devcenter.heroku.com/articles/python-support#supported-runtimes to check for supported python versions