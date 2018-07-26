import scrapy


class BelsimpelSpider(scrapy.Spider):
    name = "quotes"
    devices = [
        'samsung-galaxy-s9/zwart/',
        'apple-iphone-x/64gb-zwart/',
        'apple-iphone-8/64gb-zwart/',
        'apple-iphone-8-plus/64gb-zwart/'
    ]
    subscriptions = [
        't-mobile-normaal-go-next-2-jaar-hsnwa3',
        't-mobile-normaal-go-next-2-jaar-hsnwa',
        'vodafone-red-2-jaar',
        'vodafone-start-xl-2-jaar',
        't2-100-minuten-2000-mb-4g-2-jaar',
        't2-100-minuten-5000-mb-4g-2-jaar',
        't2-100-minuten-10000-mb-4g-2-jaar',
        't2-onbeperkt-bellen-onbeperkt-mb-4g-2-jaar',
        'hollandsnieuwe-6000-mb-min-sms-4g-2-jaar',
        'telfortnieuw-150-minuten-10000-mb-4g-2-jaar',
        'kpn-basis-2-jaar',
        'kpn-zorgeloos-standaard-2-jaar'
    ]
    start_urls = []

    for dev in devices:
        for sub in subscriptions:
            url = 'http://www.belsimpel.nl/' + dev + 'aanbieding?abonnement=' + sub
            start_urls.append(url)

    def parse(self, response):
        for quote in response.css('div.pd_chosen_offer_cta'):
            yield {
                'url': response.request.url,
                'prijs': quote.xpath('//*[@class="pd_offer_picker_row pd_offer_picker_row_hardware_cost"]/*/text()').extract_first(),
                'data': quote.xpath('//*[@class="fcs_table_col1"]/text()').extract_first(),
                'minuten': quote.xpath('//*[@class="fcs_table_col2"]/text()').extract_first(),
                'toestel': quote.xpath('//*[@id="pd_title"]/text()').extract_first(),
            }
