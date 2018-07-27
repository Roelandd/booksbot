import scrapy


class BelsimpelSpider(scrapy.Spider):
    name = "belsimpelspider"
    devices = [
        'samsung-galaxy-s8/zwart/',
        'samsung-galaxy-s9/zwart/',
        'samsung-galaxy-s9-plus/64gb-zwart',
        'apple-iphone-x/64gb-zwart/',
        'apple-iphone-8/64gb-zwart/',
        'apple-iphone-8-plus/64gb-zwart/',
        'apple-iphone-7/32gb-zwart/'
        'oneplus-6/zwart/',
        'huawei-p20-lite/zwart/',
        'huawei-p20/zwart/',
        'huawei-p20-pro/zwart/'
    ]
    subscriptions = [
        't-mobile-normaal-go-next-2-jaar-hsnwa3',
        't-mobile-normaal-go-next-2-jaar-hsnwa',
        'vodafone-red-2-jaar',
        'vodafone-red-iphonex-2-jaar'
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
#                'data': quote.xpath('//*[@data-scrollpoint_name="inhoud-abonnement"]/ul/li[2]/text()').extract_first(),
#                'minuten': quote.xpath('//*[@data-scrollpoint_name="inhoud-abonnement"]/ul/li[1]/text()').extract_first(),
                'provider': quote.xpath('//*[@class="pd_offer_picker_product_images_provider"]/*/@alt').extract_first(),
                'toestel': quote.xpath('//*[@id="pd_title"]/text()').extract_first(),
            }

class MobielSpider(scrapy.Spider):
    name = "mobielspider"
    start_urls = [
        'https://www.mobiel.nl/abonnement/t-mobile/t-mobile-go-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31300&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/vodafone/vodafone-start-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=32154&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/vodafone/vodafone-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31635&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31233&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31234&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31235&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31236&%5Bvoice_bundle%5D=31238&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/hollandsnieuwe/hollandsnieuwe-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=36026&%5Bvoice_bundle%5D=36290&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/telfort/telfort-mobiel-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=35678&%5Bvoice_bundle%5D=35680&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/kpn/kpn-basis-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=30871&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/kpn/kpn-zorgeloos-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=30979&%5Bmax_price_incl_btw%5D=0#'
    ]

    def parse(self, response):
        for quote in response.xpath('//*[@class="proposed-phone__row js-phone-proposition"]'):
            try:
                yield {
                    'url': response.request.url,
                    'prijs': quote.css('span.proposed-phone__monthly-price::text').extract_first().strip(),
                    'abo': 'FUTURE',
                    'provider': response.request.url.split("/")[4],
                    'toestel': quote.css('div.proposed-phone__image-and-name::text').extract()[1].strip(),
                }
            except:
                continue
                
                
class GsmwebSpider(scrapy.Spider):
    name = "gsmwebspider"
    start_urls = [
        'https://www.gsmweb.nl/tele2&duration=24&abo_cat=per%20maand'
    ]

    def parse(self, response):
        for quote in response.xpath('//*[@class="brand"]'):
            print("brand detected")
            try:
                yield {
                    'url': response.request.url,
                    'prijs': ' ',
                    'abo': 'FUTURE',
                    'provider': response.css('h1').split(" ")[0],
                    'toestel': quote.css('td.dark::text').extract()[1].strip(),
                }
            except:
                continue
