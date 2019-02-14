#!/usr/bin/python -tt

import sys
import urllib
import re


class BabyNames:
    def __init__(self, year):
        self.year = year
    
    def retrieveNames(self, url):
        return        
    
    def printNames(self):
        return

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: [--summaryfile] URL'
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
        
    try:
        text = urllib.urlopen(args[0])
        if text.info().gettype() == "text/html":
            # years = re.findall(r'\d\d\d\d\sto\s\d\d\d\d</h2><ul>(.*?)</ul>', text.read())
            years = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
            for year in years:
                # extract the URL from the <li> tag and add URL to list
                y = re.findall(r'', text.read())
            ''' 
            instantiate objects for getting baby names
            we iterate through the list of URLs from above
            '''
            # for yearURL in yearURLs:
            #     bn = BabyNames(yearURL)
            #     bn.printNames()
    except IOError:
        print "could not access web address", args[0]
        
        
if __name__ == "__main__":
    main()
        
        
# wget("https://www.babycentre.co.uk/popular-baby-names")


# def something():
#     text = ""
#     pagetext = text.read()
#     pagetext = ""
#     beg = pagetext.search('<ol>')
#     end = pagetext.search('<ol>')
#     list = pagetext[beg:end]
