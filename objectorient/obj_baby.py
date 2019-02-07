#!/usr/bin/python -tt

import urllib

def wget(url):
    try:
        text = urllib.urlopen(url)
        if text.info().gettype() == "text/html":
            print text.read()
    except IOError as err:
        print "could not access web address", url
        print err
        
wget("http://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/100-most-popular-boys-names-so-far-in-2018")

def something():
    text = ""
    # pagetext = text.read()
    pagetext = ""
    beg = pagetext.search('<ol>')
    end = pagetext.search('<ol>')
    list = pagetext[beg:end]
