import scrapy
import math
class BelsimpelSpider(scrapy.Spider):

    name = "belsimpelspider"
    devices = [
        'apple-iphone-x/64gb-zwart/',
        'apple-iphone-x/256gb-zwart/',
        'apple-iphone-8/64gb-zwart/',
        'apple-iphone-8/256gb-zwart/',
        'apple-iphone-8-plus/64gb-zwart/',
        'apple-iphone-8-plus/256gb-zwart/',
        'apple-iphone-7/32gb-zwart/',
        'apple-iphone-7/128gb-zwart/',
        'apple-iphone-7-plus/32gb-jet-black/',
        'apple-iphone-7-plus/256gb-jet-black/',
        'apple-iphone-se/32gb-zwart/',
        'apple-iphone-6-plus/16gb-zwart/',
        'apple-iphone-6/32gb-zwart/',
        'samsung-galaxy-j3-2017/zwart/',
        'samsung-galaxy-j5-2017/zwart/',
        'samsung-galaxy-j7-2017/zwart/',
        'samsung-galaxy-a5-2017/zwart/',
        'samsung-galaxy-a8-2018/zwart/',
        'samsung-galaxy-s7/zwart/',
        'samsung-galaxy-s7-edge/zwart/',
        'samsung-galaxy-s8/zwart/',
        'samsung-galaxy-s8-plus/zwart/',
        'samsung-galaxy-s9/zwart/',
        'samsung-galaxy-s9/256gb-zwart/',
        'samsung-galaxy-s9-plus/zwart/',
        'samsung-galaxy-note-8/zwart/',
        'huawei-p20-lite/zwart/',
        'huawei-p20/zwart/',
        'huawei-p20-pro/zwart/',
        'huawei-p10-lite/zwart/',
        'huawei-p10/zwart/',
        'huawei-mate-10-pro/128gb-grijs/',
        'huawei-mate-lite/zwart/',
        'huawei-p-smart/zwart/',
        'huawei-p-smart-plus/zwart/',
        'huawei-p8-lite-2017/zwart/',
        'motorola-moto-g6/blauw/',
        'motorola-moto-g6-plus/blauw/',
        'nokia-6-1/zwart/',
        'nokia-7-plus/zwart/',
        'google-pixel-2/64gb-zwart/',
        'nokia-8/grijs/',
        'oneplus-6/zwart/',
    ]
    subscriptions = [
        't-mobile-normaal-go-next-2-jaar-hsnwa3',
        't-mobile-normaal-go-next-2-jaar-hsnwa',
        't-mobile-normaal-go-next-2-jaar',
        'vodafone-red-2-jaar',
        'vodafone-red-iphonex-2-jaar',
        'vodafone-start-xl-2-jaar',
        'vodafone-start-iphonex-xl-2-jaar',
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

    def get_subscription(self,url):
    	if 't-mobile-normaal-go-next-2-jaar' in url:
    		return 'go next'
    	elif 'vodafone-red-2-jaar' in url:
    		return 'red'
    	elif 'vodafone-start-xl-2-jaar' in url:
    		return 'start xl'
    	elif 't2-100-minuten-2000-mb-4g-2-jaar' in url:
    		return '100/2000'
    	elif 't2-100-minuten-5000-mb-4g-2-jaar' in url:
    		return '100/5000'
    	elif 't2-100-minuten-10000-mb-4g-2-jaar' in url:
    		return '100/10000'
    	elif 't2-onbeperkt-bellen-onbeperkt-mb-4g-2-jaar' in url:
    		return 'onbeperkt'
    	elif 'hollandsnieuwe-6000-mb-min-sms-4g-2-jaar' in url:
    		return '6000 min/sms/mb'
    	elif 'telfortnieuw-150-minuten-10000-mb-4g-2-jaar' in url:
    		return '150/10000'
    	elif 'kpn-basis-2-jaar' in url:
    		return 'basis'
    	elif 'kpn-zorgeloos-standaard-2-jaar' in url:
    		return 'zorgeloos standaard'

    def parse(self, response):
        for item in response.css('div.pd_chosen_offer_cta'):
            yield {
                'url': response.request.url,
                'toestelbundel': item.css('ul.js_fcs_table_rows > li > label > span > span.text_nowrap::text').extract()[0][2:],
                'bijbetaal': item.css('ul.js_fcs_table_rows > li > label > span.pull_right').extract_first(),
                'abo': self.get_subscription(response.request.url),
                'provider': item.xpath('//*[@class="pd_offer_picker_product_images_provider"]/*/@alt').extract_first()[:-11].lower(),
                'toestel': item.xpath('//*[@id="pd_title"]/text()').extract_first().strip(),
                'shop': 'belsimpel'
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
        'https://www.mobiel.nl/abonnement/hollandsnieuwe/hollandsnieuwe-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=37525&%5Bvoice_bundle%5D=36290&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/telfort/telfort-mobiel-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=35678&%5Bvoice_bundle%5D=35680&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/kpn/kpn-basis-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=30871&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/kpn/kpn-zorgeloos-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=30979&%5Bmax_price_incl_btw%5D=0#'
    ] 

    def get_subscription(self,url):
    	if 't-mobile-go' in url:
    		return 'go next'
    	elif 'vodafone-2-jaar' in url:
    		return 'red'
    	elif 'vodafone-start-2-jaar' in url:
    		return 'start xl'
    	elif '31233' in url:
    		return '100/2000'
    	elif '31234' in url:
    		return '100/5000'
    	elif '31235' in url:
    		return '100/10000'
    	elif '31236' in url:
    		return 'onbeperkt'
    	elif 'hollandsnieuwe' in url:
    		return '6000 min/sms/mb'
    	elif 'telfort' in url:
    		return '150/10000'
    	elif 'kpn-basis' in url:
    		return 'basis'
    	elif 'kpn-zorgeloos' in url:
    		return 'zorgeloos standaard'

    def parse(self, response):
        for item in response.xpath('//*[@class="proposed-phone__row js-phone-proposition"]'):
            try:
                yield {
                    'url': response.request.url,
					'toestelbundel': item.css('dd.proposition__price-details__value::text').extract()[1],
                    'abo': self.get_subscription(response.request.url),
                    'provider': response.request.url.split("/")[4],
                    'toestel': item.css('div.proposed-phone__image-and-name::text').extract()[1].strip(),
                    'shop': 'mobiel'
                }
            except:
                continue
