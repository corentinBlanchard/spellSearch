import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "bestiaire"
    # start_urls = [
    #     'http://legacy.aonprd.com/bestiary/aasimar.html#aasimar'
    # ]

    start_urls = [
        'http://legacy.aonprd.com/bestiary2/additionalMonsterIndex.html',
        'http://legacy.aonprd.com/bestiary/monsterIndex.html'
    ]
    data = []

    def parse(self, response):
        url = response.url.split("/")
        if response.url.startswith("http://legacy.aonprd.com/" + url[3]):
            TITLE_SELECTOR = "//h1[@class='monster-header']/text()"


            title = response.xpath(TITLE_SELECTOR).extract_first()
            if title is not None:
                spells = []

                for r in response.css('a'):
                    url = r.css('::attr(href)').get()
                    txt = r.css('::text').get()
                    if url.startswith("../coreRulebook/spells/"):
                        spells.append(txt)

                spells = list(set(spells))
                self.data.append({
                    'title' : title,
                    'spells' : spells
                })

        stoke_link_list = response.css("a::attr(href)").getall()
        for next_page in stoke_link_list:
            if next_page is not None:
                if not next_page.startswith("http://legacy.aonprd.com/") and not next_page.startswith(".."):
                    next_page = "http://legacy.aonprd.com/" + url[3] + "/" + next_page
                if next_page.startswith("http://legacy.aonprd.com/" + url[3]):
                    #break
                    yield response.follow(next_page, callback=self.parse)
                    

    

    def closed(self, reason):
        # will be called when the crawler process ends
        # any code 
        # do something with collected data 
        with open('bestiaire.json', 'w') as outfile:
            # json.dump(self.data, outfile, indent=4)
            json.dump(self.data, outfile)
