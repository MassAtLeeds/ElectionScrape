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
import collections
import time
import urllib

AREA_FILE = "ConstituencyONScodes.csv"

OUTFILE = "election_results-2017.csv"


# First read through the list of areas from the input file 

names = []
codes = []
with open(AREA_FILE) as f:
    for line in f:
        l = line.split(',') # This makes a new list called 'l' which has the name and code in it
        codes.append(l[0]) # The code is in the first column
        names.append(l[1].replace('"',"")) # The name is in the second column, also get rid of quotes

assert len(names) == len(codes), "For some reason codes and names are different lengths"

print("Have read {} names and {} codes".format(len(names), len(codes) ) )

# Full csv output to write out at the end (one list item for each row, first one is a header:
full_results = ["ConstituencyName, ConstituencyCode, Party, Candidate, Votes, Percentage, PctChange"] 

# Then add each area code the the end of the BBC url and start scraping

for (name, code) in zip(names,codes):
    
    # Get rid of whitspace around code and name
    name = name.strip()
    code = code.strip()
    print("Getting data for {} ({})".format(name,code))

    # Make a new url to access
    url =  "http://www.bbc.co.uk/news/politics/constituencies/"+code
    print("\tAccessing url: "+url)

    # Download the HTML from that site
    soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")

    #print(soup)

    # Get all of the tables that have the results that we're looking for. As it happens,
    # there should only be one of these.
    tables = soup.find_all('table', attrs={'class':'results-table--constituency-region'})
    assert len(tables) == 1, "Unexpected number of tables found: {}".format(len(tables))
    
    # This is the table that we want to interrogate
    table = tables[0]
        
    table_body = table.find('tbody')
    # print(table_body)
    rows = table_body.find_all('tr')
    for row in rows: # Each row has information about the votes for a party.
        # This row has all of the information for one of the parties.
        
        #print(row)
        
        # Get the party name first
        party = row.find_next('p', attrs={'class':'results-table__party-name-const-region--long'}).text
        #print ("** Party: "+str(party)+"**")
        
        # Now the candidate
        candidate= row.find_next('td', attrs={'class':'results-table__body-item--constituency-candidates'}).text.strip()
        #print ("** Candidate: "+str(candidate)+"**")
        
        # The votes, percentage, and percentage change need ot be gotten together
        results = row.find_all('td', attrs={'class':'results-table__body-item--constituency'})
        
        # First the Votes. These need a little parsing to get the actual number from the text ext
        votes = int(results[0].text.strip().split("Votes\n")[1].replace(",",""))
        #print ("** Votes: "+str(votes)+"**")

        # Now the Percentage
        pct = float(results[1].text.strip().split("header_vote_share\n")[1].replace(",",""))
        #print ("** Percengage: "+str(pct)+"**")

        # Now the Percantage change
        pct_change = float(results[2].text.strip().split("Net percentage change in seats\n")[1].replace(",",""))
        #print ("** Change: "+str(pct_change)+"**")
        
        # Make a csv string for this result to write out
        csv = "{ConstituencyName}, {ConstituencyCode}, {Party}, {Candidate}, {Votes}, {Percentage}, {PctChange}".format(
                        ConstituencyName=name,
                        ConstituencyCode=code,
                        Party=party,
                        Candidate=candidate,
                        Votes=votes,
                        Percentage=pct,
                        PctChange=pct_change
                        )

        full_results.append(csv)
        print("\t"+csv)




    time.sleep(1) # Wait a second before getting the next page
            
            

    #print(soup.table['results-table--constituency-region'])

print("Finished downloading data.\nResults are:")


print("\n".join(full_results))

with open(OUTFILE, 'w') as f:
    f.write("\n".join(full_results))

print("Have written results to {}".format(OUTFILE))


print("Finished")
