# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-100-minuten-2000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-100-minuten-5000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-100-minuten-10000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-onbeperkt-bellen-onbeperkt-mb-4g-2-jaar',
    ]

    def parse(self, response):
        for quote in response.css('div.pd_chosen_offer_cta'):
            yield {
                'prijs': quote.xpath('/html/body/div[10]/div/div[1]/div[1]/div/div[4]/div[5]/div[1]/text()').extract_first(),
                'toestel': quote.xpath('//*[@id="pd_title"]/text()').extract_first(),
            }
