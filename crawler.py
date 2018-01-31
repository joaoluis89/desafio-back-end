from html.parser import HTMLParser  
import feedparser
import json
from urllib.request import urlopen  
from urllib import parse

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition

class FeedParser(object):
    """docstring for FeedParser"""
    def __init__(self):
        super(FeedParser, self).__init__()
    def get_and_filter_feed(self, rss_url): #, latest_feed_timestamp):
        filtered_feed = list()

        result = feedparser.parse(rss_url)
        for entry in result.entries:
            print(entry)
            print()
        return 0

parser = FeedParser()
parser.get_and_filter_feed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
