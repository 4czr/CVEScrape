# CVEScrape
CVEScrape, well, it's in the name :)... CVEScrape is written in python and scrapes for CVE's off the internet either by searching keyword or getting the latest available. Currently only exploit-db is supported, although I intend to add multiple websites to scrape from and organazing all the data into most recent order. This for me is just a practice for webscraping with Selenium and BeautifulSoup and also data mining and analysis. Selenium was a complete pain so I may convert this project to Scrapy or Pyppeteer.

Twitter @_Ozz

Github @4czr

Email ozz@riseup.net

# Use
```
python3 main.py -h | Displays this help text
python3 main.py -s KEYWORD | Search for CVE by keyword
python3 main.py -r | Displays the most recent CVEs posted
```

# How To Install
#####  *Python 3.10.2 or later recommended*
## Windows

First install selenium
```pip install selenium```

Then install BeautifulSoup
```pip install bs4```

After this you will need to get the ChromeDriver
```https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.71/```

Download the windows zip and extract the EXE to your C:\\ (or edit the path in main.py to where you driver is located)
NOTE: Please make sure you have Chrome 97 installed on your system, as well as download the driver 97!

Then you should be good to go!
## Linux/Mac
First install selenium
```pip install selenium```

Then install BeautifulSoup
```pip install bs4```

After this you will need to get the ChromeDriver (linux64 version)
```https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.71/```
Extract the zip to your home directory and edit main.py and replace the driver path with yours

NOTE: Please make sure you have Chrome 97 installed on your system, as well as download the driver 97!

Then you should be good to go!

# Version
**1.2**

# What's To Come?
- Multi-site intergration
- Better data orginization
