# insta_followers

This piece of code logins to instagram with credentials stored in 'secret.py'
Fetches the list of users that you follow and your followers and returns back the users which aren't following you back.

## Steps to build:
- Create virtual environment
    - virtualenv -p python3 venv
- Activate environment
    - venv\Source\activate
- Install selenium dependency in activated environment
    - pip3 install selenium
- Download Chrome web driver for Windows x64
    - https://chromedriver.chromium.org/downloads
    - Place the unzipped .exe file in C:\Windows
- Run program
    - python main.py