# Crawler para coleta de feeds
# Author: Joao Pacheco
# Date: 02/02/2018

import feedparser
import json
from collections import OrderedDict
from bs4 import BeautifulSoup


class Feed(object):
    """Feed Class
        Responsavel pelo nó mais externo da estrutura contruida
        Representa a pagina de com varias noticias
    """
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
    """Model que armazena um feed da pagina de feeds"""
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
        soup = BeautifulSoup(str(content), 'lxml')
        self.setTextDescription(soup)
        self.setImageDescription(soup)
        self.setLinkDescription(soup)
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
    """ Modelo que armazena a estrutura basica da descricao de uma noticia"""
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
    """Modelo que armazena a estrutura especifica do tipo text de uma descricao de uma noticia"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'text')

    def addContent(self, content):
        aux = ''.join(content)
        self.content = ''.join(content)
        return not (not aux.rstrip())


class Image(FeedItemDescription):
    """Modelo que armazena a estrutura especifica do tipo image de uma descricao de uma noticia"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'image')


class Link(FeedItemDescription):
    """Modelo que armazena a estrutura especifica do tipo links de uma descricao de uma noticia"""
    def __init__(self):
        FeedItemDescription.__init__(self, 'links')
        self.content = []

    def addContent(self, content):
        self.content.append(content)
        return self


class FeedGetter(object):
    """Coleta o feed a partir de uma url"""
    def __init__(self):
        super(FeedGetter, self).__init__()

    def getFeed(self, rss_url):
        result = feedparser.parse(rss_url)
        return result


class FeedFactory(object):
    """Responsavel pela construcao dos objetos FEED e FEEdTOJSON """
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
        return json.dumps(feedToJson, indent=4, ensure_ascii=False)


class Crawler(object):
    """Wrapper para execucao do FeedGetter"""
    def __init__(self):
        super(Crawler, self).__init__()

    def getFeed(self, url):
        getter = FeedGetter()
        rawFeed = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        return rawFeed


class CrawlerResponse(object):
    """Realiza a coleta do Feed e a codifica em em algum formato REST """
    def __init__(self):
        super(CrawlerResponse , self).__init__()

    def getResponse(self):
        getter = FeedGetter()
        rawFeed = getter.getFeed('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        feed = FeedFactory.getFeed(rawFeed)
        return FeedFactory.FeedToJson(feed)


"""Se for executada via linha de comando, imprime o json resultante na tela"""
if __name__ == '__main__':
    resp = CrawlerResponse()
    print(resp.getResponse())
