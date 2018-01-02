import lxml.html
import requests
import scraper as sc


class Scraping:

    def __init__(self):
        self.url = 'http://www.vdaepc.de/service-informationen/artztsuche/'
        self.data = []

    def get_data(self):
        self.source = requests.get(self.url)
        self.etree = lxml.html.fromstring(self.source.content)
        self.tree = self.etree.xpath('//div[@class="arztinfo"]')
        for element in self.tree:
            self.name = sc.get_text(element.xpath('./h4/text()'))
            self.website = sc.get_href(element.xpath('.//following-sibling::span[contains(text(), "Webseite:")]/following-sibling::a[@href]'))
            self.email = sc.get_text(element.xpath('.//following-sibling::span[contains(text(), "Email:")]/following-sibling::a[1]/text()'))
            self.data.append([self.name, self.website, self.email])
        sc.Database(('name', 'website', 'email')).push_data(self.data)


Scraping = Scraping()
Scraping.get_data()
