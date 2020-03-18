import scrapy
from scrapy.crawler import CrawlerProcess



#The first set of code downloads html of our web page of interest

class ESSpider(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "ESS"
    
    # URL(s) to start with.
    start_urls = [
        'https://www.reddit.com/r/datascience',
    ]

    # What to do with the URL.  Here, we tell it to download all the code and save
    # it to the mainpage.html file
    def parse(self, response):



    	with open('r_datascience.html', 'wb') as f:
    		f.write(response.body)


# Instantiate our crawler.
process = CrawlerProcess()

# Start the crawler with our spider.
process.crawl(ESSpider)
process.start()
'''



class ESSpider(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "ESS"
    
    # URL(s) to start with.
    start_urls = [
        'https://lark.thinkful.com/grading/',
    ]

    # Use XPath to parse the response we get.
    def parse(self, response):
        
        # Iterate over every <article> element on the page.
        for article in response.xpath('//script'):
            
            # Yield a dictionary with the values we want.
            yield {
                # This is the code to choose what we want to extract
                # You can modify this with other Xpath expressions to extract other information from the site
                'name': article.xpath('header/h2/a/@title').extract_first(),
                'date': article.xpath('header/section/span[@class="entry-date"]/text()').extract_first(),
                'text': article.xpath('section[@class="entry-content"]/p/text()').extract(),
                'tags': article.xpath('*/span[@class="tag-links"]/a/text()').extract()
            }

# Tell the script how to run the crawler by passing in settings.
process = CrawlerProcess({
    'FEED_FORMAT': 'json',         # Store data in JSON format.
    'FEED_URI': 'firstpage.json',  # Name our storage file.
    'LOG_ENABLED': False           # Turn off logging for now.
})

# Start the crawler with our spider.
process.crawl(ESSpider)
process.start()
print('Success!')'''