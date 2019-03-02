import zillow_web_scraper_client as client

#print client.get_property_by_zpid(89237746)
"""
print client.search_zillow_by_zip("94015")

print client.search_zillow_by_city_state("San Francisco", "CA")

print client.get_property_by_zpid(83154148)

print client.get_properties_by_zip(94080)

print client.get_properties_by_city_state('San Bruno', 'CA')

print client.get_similar_homes_for_sale_by_id(2096630311)
"""
print client.search_zillow_by_zip("94015")

#print client.find_xpath(89237746,'''//*[@class='value']/text()''')


"""
SEARCH_XPATH_FOR_ZPID = '''//div[@id='list-results']/div[@id='search-results']/ul[@class='photo-cards']/li/article/@id'''
GET_INFO_XPATH_FOR_STREET_ADDR = '''//*[@class='zsg-h1 hdp-home-header-st-addr']/text()'''
GET_INFO_XPATH_FOR_CITY_STATE_ZIP = '''//*[@class='zsg-h2']/text()'''
GET_INFO_XPATH_FOR_TYPE = '''//div[@class='loan-calculator-container']/div/@data-type'''
GET_INFO_XPATH_FOR_BEDROOM = '''//header[@class='zsg-content-header addr']/h3/span[@class='addr_bbs'][1]/text()'''
GET_INFO_XPATH_FOR_BATHROOM = '''//header[@class='zsg-content-header addr']/h3/span[@class='addr_bbs'][2]/text()'''
GET_INFO_XPATH_FOR_SIZE = '''//header[@class='zsg-content-header addr']/h3/span[@class='addr_bbs'][3]/text()'''
GET_INFO_XPATH_FOR_SALE = '''//div[@id='home-value-wrapper']/div[@class='estimates']/div/text()'''
GET_INFO_XPATH_LIST_FOR_PRICE = '''//div[@id='home-value-wrapper']/div[@class='estimates']/div[@class='main-row  home-summary-row']/span/text()'''
GET_INFO_XPATH_FOR_LATITUDE = '''//div[@class='zsg-layout-top']/p/span/span[@itemprop='geo']/meta[@itemprop='latitude']/@content'''
GET_INFO_XPATH_FOR_LONGITUDE = '''//div[@class='zsg-layout-top']/p/span/span[@itemprop='geo']/meta[@itemprop='longitude']/@content'''
GET_INFO_XPATH_DESCRIPTION = '''//div[@class='zsg-lg-2-3 zsg-md-1-1 hdp-header-description']/div[@class='zsg-content-component']/div/text()'''
GET_INFO_XPATH_FOR_FACTS = '''//div[@class='fact-group-container zsg-content-component top-facts']/ul/li/text()'''
GET_INFO_XPATH_FOR_ADDITIONAL_FACTS = '''//div[@class='fact-group-container zsg-content-component z-moreless-content hide']/ul/li/text()'''
GET_SIMILAR_HOMES_FOR_SALE_XPATH = '''//ol[@id='fscomps']/li/div[@class='zsg-media-img']/a/@href'''


"""