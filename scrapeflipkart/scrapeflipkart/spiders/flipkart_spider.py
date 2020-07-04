import scrapy
from scrapeflipkart.items import ScrapeflipkartItem 
import re


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    page_number = 2
    start_urls = [
        'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=c53cbb8b-f4f6-4b04-a5ca-1ddb4e248d66&as-searchtext=mobil&page=1'   
    ]

    def parse(self,response):
        items = ScrapeflipkartItem()
        all_items = response.css('div._3O0U0u')
        for i in all_items:
         product_name = i.css('._3wU53n::text').extract()
         price = i.css('._2rQ-NK').css('::text').extract()
         rating = i.css('.hGSR34').css('::text').extract()
         battery = i.css('.tVe95H:nth-child(4)').css('::text').extract() 
         ram = i.css('.tVe95H:nth-child(1)').css('::text').extract()
         display = i.css('.tVe95H:nth-child(2)').css('::text').extract()
         camera = i.css('.tVe95H:nth-child(3)').css('::text').extract()
         #hrefs = i.css('._3wU53n::attr(href)').extract_first()
         no_of_ratings = i.css('._38sUEc span span:nth-child(1)::text').extract()
         no_of_reviews = i.css('._1VpSqZ+ span::text').extract()
         

         items['product_name'] = product_name
         items['price'] = price
         items['rating'] = rating
         items['battery'] = battery
         items['ram'] = ram
         items['display'] = display
         items['camera'] = camera
         items['no_of_ratings'] = no_of_ratings
         items['no_of_reviews'] = no_of_reviews
         #items['processor'] = processor
         

         yield items
  

        next_page = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=c53cbb8b-f4f6-4b04-a5ca-1ddb4e248d66&as-searchtext=mobil&page= '+ str(FlipkartSpider.page_number)
        if FlipkartSpider.page_number<=41:
            FlipkartSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)

                
            
