import re
import feedparser
import json
from bs4 import BeautifulSoup
# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition


class Feed(object):
    """docstring for Feed"""
    def __init__(self):
        super(Feed, self).__init__()
        self.itens = []

    def getItens(self):
        return self.itens

    def addItem(self, item):
        feedItem = FeedItem(item.title, item.link)
        feedItem.addDescription(item.summary)

        #  print(re.findall(r'\w+', txt))
        self.itens.append(feedItem)
        return self


class FeedItem(object):
    """docstring for FeedItem"""
    def __init__(self, title, link):
        super(FeedItem, self).__init__()
        self.title = title
        self.link = link
        self.descriptions = []

    def getDescriptions(self):
        return self.descriptions

    def addDescription(self, content):
        soup = BeautifulSoup(str(content), 'lxml')
        #  texts = [ (s.findAll(text=True)) for s in soup.findAll('p')]
        #  for rawText in texts:
        #      textDescriptionObject = Text()
        #      textDescriptionObject.addContent(rawText)
        #      self.descriptions.append(textDescriptionObject)
        
        images = soup.findAll('img')
        print(images)
        # for rawImage in images:
        #     imageDescriptionObject = Image()
        #     imageDescriptionObject.addContent(rawImage)
        #     self.descriptions.append(imageDescriptionObject)
        # for descriptionObject in self.descriptions:
        #     print(descriptionObject.getContent())
        #     pass
        # return self


class FeedItemDescription(object):
    """docstring for FeedItemDescription"""
    def __init__(self, tagType):
        super(FeedItemDescription, self).__init__()
        self.type = tagType

    def addContent(self, content):
        self.content = ''.join(content)
        return self

    def getContent(self):
        return self.content

    def __str__(self):
        return self.getContent()


class Text(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'text')
        


class Image(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'image')


class Link(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'link')
        self.content = []

    def addContent(self, content):
        self.content.append(content)
        return self


class FeedGetter(object):
    """docstring for FeedGetter"""
    def __init__(self):
        super(FeedGetter, self).__init__()

    def getFeed(self, rss_url):
        result = feedparser.parse(rss_url)
        return result


class FeedFactory(object):
    """docstring for FeedParser"""
    def __init__(self):
        super(FeedFactory, self).__init__()

    @staticmethod
    def getFeed(rawFeed):
        feed = Feed()
        for item in rawFeed.entries:
            feed.addItem(rawFeed.entries[1])
            return
        return feed


class Crawler(object):
    """docstring for Crawler"""
    def __init__(self):
        super(Crawler, self).__init__()

    def getFeed(self, url):
        getter = FeedGetter()
        rawFeed = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        return rawFeed


feed = Feed()
getter = FeedGetter()
rawFeed = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
FeedFactory.getFeed(rawFeed)
