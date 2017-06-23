# ElectionScrape

Code to scrape the results of the 2017 UK general election (votes per party per constituency)

It reads the data from the BBC election results pages. E.g.: [http://www.bbc.co.uk/news/politics/constituencies/E14000636](http://www.bbc.co.uk/news/politics/constituencies/E14000636)

Here's one we prepared earlier: [election_results-2017.csv](./election_results-2017.csv)

## Requirements

  - python3
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library (install with something like: ```pip install beautifulsoup4```).

## Usage Instructions

 - Download this project. It includes the script to do the scraping (`scrape.py`) and a list of all constituency names.
 - Run it with: ```python scrape.py```
 - It will make a file called `election_results-2017.csv`

Note: it takes a second or so to do each constituency, so will take around 10 mins to do all 650 constituencies.


## Other resources

Matt Daws put together a nice script to scrape the results of the 2010 election:

[https://github.com/MatthewDaws/Python_bits/blob/master/election2017/Previous%20Results.ipynb](https://github.com/MatthewDaws/Python_bits/blob/master/election2017/Previous%20Results.ipynb)
