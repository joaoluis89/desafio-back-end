import feedparser
import json
from collections import OrderedDict
from bs4 import BeautifulSoup


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

        self.itens.append(feedItem)
        return self

    def __iter__(self):
        return iter(self.getItens())

    def __next__(self):
        return next(self.getItens())


class FeedItem(object):
    """docstring for FeedItem"""
    def __init__(self, title, link):
        super(FeedItem, self).__init__()
        self.title = title
        self.link = link
        self.descriptions = []

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def getDescriptions(self):
        return self.descriptions

    def addDescription(self, content):
        # print (content)
        soup = BeautifulSoup(str(content), 'lxml')
        self.setTextDescription(soup)
        self.setImageDescription(soup)
        self.setLinkDescription(soup)
        for descriptionObject in self.descriptions:
            # print(descriptionObject.getContent())
            pass
        return self

    def setTextDescription(self, soup):
        texts = [(s.findAll(text=True)) for s in soup.findAll('p')]
        for rawText in texts:
            textDescriptionObject = Text()
            if textDescriptionObject.addContent(rawText):
                self.descriptions.append(textDescriptionObject)
        return

    def setImageDescription(self, soup):
        images = soup.findAll('img')
        for img in images:
            imageDescriptionObject = Image()
            imageDescriptionObject.addContent(img.get('src'))
            self.descriptions.append(imageDescriptionObject)
        return

    def setLinkDescription(self, soup):
        links = [(s.findAll('a')) for s in soup.findAll('li')]
        linkDescriptionObject = Link()
        for link in links:
            linkDescriptionObject.addContent(link[0].get('href'))
        self.descriptions.append(linkDescriptionObject)
        return


class FeedItemDescription(object):
    """docstring for FeedItemDescription"""
    def __init__(self, tagType):
        super(FeedItemDescription, self).__init__()
        self.type = tagType

    def addContent(self, content):
        self.content = ''.join(content)
        return True

    def getContent(self):
        return self.content

    def getType(self):
        return self.type

    def __str__(self):
        return self.getContent()


class Text(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'text')

    def addContent(self, content):
        aux = ''.join(content)
        self.content = ''.join(content)
        return not (not aux.rstrip())


class Image(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'image')


class Link(FeedItemDescription):
    """docstring for Link"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'links')
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
            feed.addItem(item)
        return feed

    @staticmethod
    def FeedToJson(feed):
        feedToJson = {}
        feedCollection = []
        for item in feed:
            description = []
            for row in item.getDescriptions():
                auxDicinary = OrderedDict()
                auxDicinary['type'] = row.getType()
                auxDicinary['content'] = row.getContent()
                description.append(auxDicinary)
            feedItem = OrderedDict()
            feedItem['item'] = OrderedDict()
            feedItem['item']['title'] = item.getTitle()
            feedItem['item']['link'] = item.getLink()
            feedItem['item']['description'] = description
            feedCollection.append(feedItem)
        feedToJson['feed'] = feedCollection
        print(json.dumps(feedToJson, indent=4, ensure_ascii=False))
        return


class Crawler(object):
    """docstring for Crawler"""
    def __init__(self):
        super(Crawler, self).__init__()

    def getFeed(self, url):
        getter = FeedGetter()
        rawFeed = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        return rawFeed


def main():
    getter = FeedGetter()
    rawFeed = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
    feed = FeedFactory.getFeed(rawFeed)
    FeedFactory.FeedToJson(feed)

main()
