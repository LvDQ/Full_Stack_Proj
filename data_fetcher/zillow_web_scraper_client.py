"""
Requests is an elegant and simple HTTP library for Python, built for human beings. 
 http://docs.python-requests.org/en/master/user/quickstart/

How to install: sudo pip install requests

 """
import requests


"""
lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.

How to install: sudo pip install lxml

using lxml.html to get the structure of response

https://lxml.de/lxmlhtml.html
Note that .xpath(expr) is also available as on all lxml elements.

XPath:
https://www.programcreek.com/python/example/61622/lxml.html.fromstring
https://stackoverflow.com/questions/30852777/how-to-set-up-xpath-query-for-html-parsing

"""

from lxml import html


"""

re = regular expression

"""
import random
import re


from decimal import Decimal
from re import sub
from urllib import pathname2url


from zillow_api_client import getCompsZpids

"""

VARIABLIES

GET_INFO_XPATH: searched by user(SO LONG TIME TO DO!!!!)

"""

SOURCE_URL = '''http://www.zillow.com'''
SEARCH_FOR_SALE_PATH = '''homes/for_sale'''
GET_PROPERTY_BY_ZPID_PATH = '''homes'''
GET_SIMILAR_HOMES_FOR_SALE_PATH = '''homedetails'''
IMAGE_URL_REGEX_PATTERN = '"z_listing_image_url":"([^"]+)",'
SIMILAR_HOMES_ZPID_REGEX_PATTERN ='\/(\d+)_zpid'+ '_zpid'

SEARCH_XPATH_FOR_ZPID = '''//div[@id='list-results']/div[@id='search-results']/ul[@class='photo-cards']/li/article/@id'''
GET_INFO_XPATH_FOR_STREET_ADDR = '''//*[@class='zsg-h1 hdp-home-header-st-addr']/text()'''
GET_INFO_XPATH_FOR_CITY_STATE_ZIP = '''//*[@class='zsg-h2']/text()'''
GET_INFO_XPATH_FOR_TYPE = '''//*[@class='fact-value']/text()'''
GET_INFO_XPATH_FOR_BEDROOM = '''//*[@class='zsg-content-item']/h3/span/text()'''
GET_INFO_XPATH_FOR_BATHROOM = '''///*[@class='zsg-content-item']/h3/span/text()'''
GET_INFO_XPATH_FOR_SIZE = '''///*[@class='zsg-content-item']/h3/span/text()'''
GET_INFO_XPATH_FOR_SALE = '''//*[@class='status']/text()'''
GET_INFO_XPATH_LIST_FOR_PRICE = '''//*[@class='value']/text()'''
GET_INFO_XPATH_FOR_LATITUDE = '''//meta[@itemprop = 'latitude']/@content'''
GET_INFO_XPATH_FOR_LONGITUDE = '''///meta[@itemprop = 'longtitude']/@content'''
GET_INFO_XPATH_DESCRIPTION = '''//div[@class='zsg-lg-2-3 zsg-md-1-1 hdp-header-description']/div[@class='zsg-content-component']/div/text()'''
GET_INFO_XPATH_FOR_FACTS = '''//div[@class='fact-group-container zsg-content-component top-facts']/ul/li/text()'''
GET_INFO_XPATH_FOR_ADDITIONAL_FACTS = '''//div[@class='fact-group-container zsg-content-component z-moreless-content hide']/ul/li/text()'''
GET_SIMILAR_HOMES_FOR_SALE_XPATH = '''//ol[@id='fscomps']/li/div[@class='zsg-media-img']/a/@href'''


# Load user agents(Or user agent will show python.request, and then denied as a stupid bot)
USER_AGENTS_FILE = 'user_agents.txt'
USER_AGENTS = []


"""
Python Read files and add ua(USER_AGENTS) into a list:

https://docs.python.org/2/library/functions.html#open
https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

Parameter rb: https://stackoverflow.com/questions/9644110/difference-between-parsing-a-text-file-in-r-and-rb-mode

"""
with open(USER_AGENTS_FILE, 'rb') as uaf:
    for ua in uaf.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1:-1-1])
random.shuffle(USER_AGENTS)


def build_url(url,path):
	if(url[-1] == '/'):
		url = url[:-1]
	return '%s/%s' % (url,path)


def getHeaders():
    ua = random.choice(USER_AGENTS)  # select a random user agent
    headers = {
        "Connection" : "close",
        "User-Agent" : ua
    }
    return headers


"""

XPATH: https://www.w3schools.com/xml/xpath_syntax.asps

"""

def search_zillow(request_url, xpath):
    session_requests = requests.session()
    response = session_requests.get(request_url, headers=getHeaders())
    tree = html.fromstring(response.content)
    #print tree.xpath(xpath)
    return tree.xpath(xpath)

""" Search properties by zip code """
def search_zillow_by_zip(zipcode):
    request_url = '%s/%s' % (build_url(SOURCE_URL, SEARCH_FOR_SALE_PATH), str(zipcode))
    raw_result = search_zillow(request_url, SEARCH_XPATH_FOR_ZPID)
    # eliminate 'zpid_'
    return [x.replace('zpid_', '') for x in raw_result]

""" Search properties by city and state """
def search_zillow_by_city_state(city, state):
    city_state = pathname2url('%s %s' % (city, state))
    request_url = '%s/%s' % (build_url(SOURCE_URL, SEARCH_FOR_SALE_PATH), city_state)
    raw_result =  search_zillow(request_url, SEARCH_XPATH_FOR_ZPID)
    return [x.replace('zpid_', '') for x in raw_result]

""" Get Similar homes for sale """
def get_similar_homes_for_sale_by_id(zpid):
    request_url = '%s/%s_zpid' % (build_url(SOURCE_URL, GET_SIMILAR_HOMES_FOR_SALE_PATH), str(zpid))
    #raw_result = search_zillow(request_url, GET_SIMILAR_HOMES_FOR_SALE_XPATH)
    raw_result = getCompsZpids(zpid)
    #return [re.search(SIMILAR_HOMES_ZPID_REGEX_PATTERN, x).group(1) for x in raw_result]
    return raw_result




"""

 Get property information by Zillow Property ID(zpid)

 This is used to be good to use, but recent days they added Google reCAPTHA service to block bots

"""


"""
 No request header, so be rejected as a stupid bots

def get_property_by_zpid(zpid):
	request_url = '%s/%s' % (build_url(SOURCE_URL,GET_DETAILS_BY_ZPID_PATH),str(zpid))
	# besiege to be a normal user
	session_requests = requests.session()
	print request_url
	#response = session_requests.get(request_url)
	response = session_requests.get("https://www.amazon.com/dp/B07BKSH4KY/ref=cm_gf_aAN_i18_i6_d_c0_qd0___________________FTnLSt4TDBSyRxVSCJE1")

	try:
		tree = html.fromstring(response.content)
	except Exception:
		return {}

	print response.content


"""

def get_property_by_zpid(zpid):
    request_url = '%s/%s_zpid' % (build_url(SOURCE_URL, GET_PROPERTY_BY_ZPID_PATH), str(zpid))
    session_requests = requests.session()
    response = session_requests.get(request_url, headers=getHeaders())
    try:
    	#print response.content
        tree = html.fromstring(response.content)
    except Exception:
        return {}

    # Street address
    street_address = None
    try:
        street_address = tree.xpath(GET_INFO_XPATH_FOR_STREET_ADDR)
        print street_address[0].tag
        street_address = street_address[0].strip(', ')
        print street_address
        print "this place"
    except Exception:
        pass

    # City, state and zipcode
    city_state_zip = None
    city = None
    state = None
    zipcode = None
    try:
        city_state_zip = tree.xpath(GET_INFO_XPATH_FOR_CITY_STATE_ZIP)[0]
        city = city_state_zip.split(',')[0].strip(', ')
        state = city_state_zip.split(',')[1].split(' ')[1].strip(', ')
        zipcode = city_state_zip.split(',')[1].split(' ')[2].strip(', ')
    except Exception:
        pass

    # Type: Condo, Town hourse, Single family etc.
    property_type = None
    try:
        property_type = tree.xpath(GET_INFO_XPATH_FOR_TYPE)[0]
    except Exception:
        pass

    # Bedroom
    bedroom = None
    try:
        bedroom = int(tree.xpath(GET_INFO_XPATH_FOR_BEDROOM)[1].split(' ')[0])
    except Exception:
        bedroom = 0

    # Bathroom (float since bathroom can be .5)
    bathroom = None
    try:
        bathroom = float(tree.xpath(GET_INFO_XPATH_FOR_BATHROOM)[3].split(' ')[0])
    except Exception:
        bathroom = 0

    # Square feet
    size = None
    try:
        size = int(tree.xpath(GET_INFO_XPATH_FOR_SIZE)[5].split(' ')[0].replace(',', ''))
    except Exception:
        size = 0

    # Is for sale
    for_sale_text = tree.xpath(GET_INFO_XPATH_FOR_SALE)
    r = re.compile('.+For Sale.+')
    is_for_sale = len(filter(r.match, for_sale_text)) > 0

    # Listed price
    list_price = None
    try:
        list_price_raw = tree.xpath(GET_INFO_XPATH_LIST_FOR_PRICE)
        if len(list_price_raw) > 0:
            list_price = int(list_price_raw[0].replace(',', '').strip(' $'))
    except Exception:
        pass

    # geo
    latitude = None
    longitude = None
    try:
        latitude = float(tree.xpath(GET_INFO_XPATH_FOR_LATITUDE)[0])
        longitude = float(tree.xpath(GET_INFO_XPATH_FOR_LONGITUDE)[0])
    except Exception:
        pass

    # Image
    image_url = None
    try:
        r = re.compile(IMAGE_URL_REGEX_PATTERN)
        result = r.search(response.content)
        image_url = result.group(1)
    except Exception:
        pass 

    # Description
    description = None
    try:
        description = tree.xpath(GET_INFO_XPATH_DESCRIPTION)
    except Exception:
        pass

    # Basic facts
    facts = None
    try:
        facts = tree.xpath(GET_INFO_XPATH_FOR_FACTS)
    except Exception:
        pass

    # Additional facts
    additional_facts = None
    try:
        additional_facts = tree.xpath(GET_INFO_XPATH_FOR_ADDITIONAL_FACTS)
    except Exception:
        pass

    return {'zpid' : zpid,
            'street_address' : street_address,
            'city' : city,
            'state' : state,
            'zipcode' : zipcode,
            'property_type' : property_type,
            'bedroom' : bedroom,
            'bathroom' : bathroom,
            'size' : size,
            'latitude' : latitude,
            'longitude' : longitude,
            'is_for_sale' : is_for_sale,
            'list_price' : list_price,
            'image_url' : image_url,
            'description' : description,
            'facts' : facts,
            'additional_facts' : additional_facts}
  

"""Get properties' information by zipcode"""
def get_properties_by_zip(zipcode):
    zpids = search_zillow_by_zip(zipcode)
    return [get_property_by_zpid(zpid) for zpid in zpids]

"""Get properties' information by city and state"""
def get_properties_by_city_state(city, state):
    zpids = search_zillow_by_city_state(city, state)
    return [get_property_by_zpid(zpid) for zpid in zpids]

def find_xpath(zpid,xpath):
    request_url = '%s/%s_zpid' % (build_url(SOURCE_URL, GET_PROPERTY_BY_ZPID_PATH), str(zpid))
    session_requests = requests.session()
    response = session_requests.get(request_url, headers=getHeaders())
    try:
    	#print response.content
        tree = html.fromstring(response.content)
    except Exception:
        return {}

    # Street address
    street_address = None
    try:
        street_address = tree.xpath(xpath)
        print street_address[0].tag
        street_address = street_address[0].strip(', ')
        print street_address
    except Exception:
        pass

    return {'item': street_address}