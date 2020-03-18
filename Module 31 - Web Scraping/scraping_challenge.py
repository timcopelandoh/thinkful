import scrapy
from scrapy.crawler import CrawlerProcess



#The first set of code downloads html of our web page of interest
'''
class ESSpider(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "ESS"
    
    # URL(s) to start with.
    start_urls = [
        'https://www.econjobrumors.com',
    ]

    # What to do with the URL.  Here, we tell it to download all the code and save
    # it to the mainpage.html file
    def parse(self, response):



    	with open('ejmr.html', 'wb') as f:
    		f.write(response.body)


# Instantiate our crawler.
process = CrawlerProcess()

# Start the crawler with our spider.
process.crawl(ESSpider)
process.start()
'''

num_pages = 20

class ESSpider(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "ESS"
    
    # URL(s) to start with.
    start_urls = [
        'https://www.econjobrumors.com',
    ]

    # Use XPath to parse the response we get.
    def parse(self, response):
        
        # Iterate over every <article> element on the page.
        for page in response.xpath('//tr'):
            
            # Yield a dictionary with the values we want.
            yield {
                # This is the code to choose what we want to extract
                # You can modify this with other Xpath expressions to extract other information from the site
                #'name': page.xpath('/a').extract_first(),
                #'name2': page.xpath('/a').extract_first(),
                'name': page.xpath('td/a[starts-with(@href, "https://www.econjobrumors.com/topic/")]/text()').extract_first(),
                'link': page.xpath('td/a[starts-with(@href, "https://www.econjobrumors.com/topic/")]/@href').extract_first(),
                #'/.text': page.xpath('/a/text').extract_first(),
                #'.text': page.xpath('/a.text').extract_first(),
                #'.text()': page.xpath('/a.text()').extract_first()
                #'date': article.xpath('header/section/span[@class="entry-date"]/text()').extract_first(),
                #'text': article.xpath('section[@class="entry-content"]/p/text()').extract(),
                #'tags': article.xpath('*/span[@class="tag-links"]/a/text()').extract()
            }
        page_num = int(response.xpath('//span[@class="page-numbers current"]/text()').extract_first())
        
        print(page_num)

        if page_num <= num_pages:
        	next_page = 'https://www.econjobrumors.com/page/' + str(page_num+1)
        	yield scrapy.Request(next_page, callback = self.parse)

# Tell the script how to run the crawler by passing in settings.
process = CrawlerProcess({
    'FEED_FORMAT': 'json',         # Store data in JSON format.
    'FEED_URI': 'firstpage4.json',  # Name our storage file.
    'LOG_ENABLED': False           # Turn off logging for now.
})

# Start the crawler with our spider.
process.crawl(ESSpider)
process.start()
print('Success!')