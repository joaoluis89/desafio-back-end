from html.parser import HTMLParser  
import feedparser
import json
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
        self.itens.append(item)
        return self


class FeedItem(object):
    """docstring for FeedItem"""
    def __init__(self, titulo, link):
        super(FeedItem, self).__init__()
        self.titulo = titulo
        self.link = link
        self.descriptions = []

    def getDescriptions(self):
        return self.descriptions

    def addDescription(self, description):
        self.descriptions.append(description)
        return self


class FeedItemDescription(object):
    """docstring for FeedItemDescription"""
    def __init__(self, tagType):
        super(FeedItemDescription, self).__init__()
        self.type = tagType

    def addContent(self, content):
        self.content = content
        return self

    def getContent(self):
        return self.content


class Text(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'text')
        self.content = ''


class Image(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'image')
        self.content = ''


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
        print(result.entries[0].title)

class Crawler(object):
    """docstring for Crawler"""
    def __init__(self):
        super(Crawler, self).__init__()
    def getFeed(self, url):
        getter = FeedGetter()
        rawFeeds = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        


feed = Feed()

