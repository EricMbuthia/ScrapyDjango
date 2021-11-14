import scrapy
from scrapy.loader import ItemLoader
from wlw_companies_spider.items import WlwCompaniesSpiderItem

class BookstrSpider(scrapy.Spider):
    name = "companystr"
    allowed_domains = ['wlw.de']
    start_urls = ["https://www.wlw.de/de/suche?q=logistik&supplierTypes=Dienstleister"]
    # base_url ='http://books.toscrape.com/'
    base_url = "https://www.wlw.de"
    count = 0
 
    def parse(self, response):
        #Fetch all links
        #\fetch comapny data 
        #Fetch next and then follow
        # all_books = response.xpath('//article[@class="product_pod"]')
        company_links = response.xpath('//div[@class="company-title-link-wrap"]/a[@class="company-title-link"]/@href').get()
        for company_link in company_links:
            company_url = self.base_url +company_link

            yield scrapy.Request(company_link, callback=self.parse_company)
        next_page = self.base_url + response.xpath('//div[@class="pagination-next"]//a/@href').get()
        if next_page is not None and self.count < 3:
        # if next_page is not None : Use this to go to the last page
            self.count = +1
            yield response.follow(next_page, callback = self.parse)
    def parse_company(self, response):
        item = WlwCompaniesSpiderItem()
        company = ItemLoader(item = WlwCompaniesSpiderItem(), response = response)

    #     company_name_raw = ('//h1[@class= "business-card__title"]/text()' ).get()
    # comapny_name_clean = ('//address[@class ="location-and-contact__address"]/strong/text()').get()
    # comapnylocraq = ('//div[@class= "business-card__address"]/text()').get()
    # company-bix phone = ('//div[@id= "location-and-contact__phone"]//a/@href').get() should be cleaned tel:+43 19346765
    # coampnay email =response.xpath('//a[@id= "location-and-contact__email"]//span/text()').get()
    # street_code = //address[@class ="location-and-contact__address"]/div/div[1]/text().get()
    # postal_code  = //address[@class ="location-and-contact__address"]/div/div[2]/text().get()

        company_name_raw ='//h1[@class= "business-card__title"]/text()'
        company_name_clean = '//address[@class ="location-and-contact__address"]/strong/text()'
        company_loc_raw = '//div[@class= "business-card__address"]/text()'
        company_biz_phone ='//div[@id= "location-and-contact__phone"]//a/@href'
        company_biz_email = '//a[@id= "location-and-contact__email"]//span/text()'
        company_street_name = '//address[@class ="location-and-contact__address"]/div/div[1]/text()'
        company_postal_code = '//address[@class ="location-and-contact__address"]/div/div[2]/text()'
        company.add_xpath(company_name_raw)
        company.add_xpath(company_name_clean)
        company.add_xpath(company_loc_raw)
        company.add_xpath(company_biz_phone)
        company.add_xpath(company_biz_email)
        company.add_xpath(company_street_name)
        company.add_xpath(company_postal_code)


    