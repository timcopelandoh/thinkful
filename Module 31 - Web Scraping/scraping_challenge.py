import scrapy
from scrapy.crawler import CrawlerProcess

class ESSpider(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "ESS"
    
    # URL(s) to start with.
    start_urls = [
        'https://www.espn.com/nfl/scoreboard/_/year/2019/seasontype/2/week/1',
    ]

    # What to do with the URL.  Here, we tell it to download all the code and save
    # it to the mainpage.html file
    def parse(self, response):
        with open('mainpage.html', 'wb') as f:
            f.write(response.body)


# Instantiate our crawler.
process = CrawlerProcess()

# Start the crawler with our spider.
process.crawl(ESSpider)
process.start()
