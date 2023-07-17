import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/
class SteamSpider(CrawlSpider):

    name = "SteamParser"
    start_url = ['https://store.steampowered.com/search/?filter=topsellers']
    page = 1

    rules = (Rule(LinkExtractor(allow = 'app'),callback='parse_tags'))
    def parse_tags(self,response):
        tags = response.css("a.app_tag")
        name = response.css("div.apphub_AppName::text").get()
        yield {
            "name":name,
            "tags": [tag.css("a::text").get().strip() for tag in tags]
        }