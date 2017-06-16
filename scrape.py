# Read a file of ONS codes for each constituency, then go to the BBC election results website and
# scrape the results for each party per constituency.
#
# The URLs are like this:
#    http://www.bbc.co.uk/news/politics/constituencies/E14000636
# where E14000636 is the area code (that one is for Chipping Barnet).
#
# Requirements: the program needs the Beautiful Soup library
# (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


from bs4 import BeautifulSoup

AREA_FILE = "XX.csv"


# First read through the list of areas from the input file XXX

names = []
codes = []
with open(AREA_FILE) as f:
    for line in f:
        l = line.split(',') # This makes a new list called 'l' which has the name and code in it
        names.append(l[0]) # The name is in the first column
        codes.append(l[1]) # The code is in the second column

assert len(names) == len(codes), "For some reason codes and names are different lengths"

print("Have read {} names and {} codes".format(len(names), len(codes) ) )


# Then add each area code the the end of the BBC url and start scraping

for (name, code) in zip(names,codes):
    print(name,code)

    




print("Finished")
