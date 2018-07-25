# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-100-minuten-2000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-100-minuten-5000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-100-minuten-10000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/samsung-galaxy-s9/zwart/aanbieding?abonnement=t2-onbeperkt-minuten-onbeperkt-mb-4g-2-jaar',
    ]

    def parse(self, response):
        for quote in response.css('div.pd_chosen_offer_cta'):
            yield {
                'toestel': quote.xpath('//*[@id="pd_title"]::text').extract_first(),
                'prijs': quote.css('div.pd_offer_picker_row_price::text').extract_first()
            }
