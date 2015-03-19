########################################################
#     	 			                                   #
#	             Flipkart Products API	               #
#	                  Version 2.0     	               #
#	    		 	                	               #
#                Developer: Shreesha.S	               #
#          Contact: shreesha.suresh@gmail.com	       #
#				                                       #
########################################################


# Running this script returns the product details of the best matched product on flipkart based on the input string given
# Make sure you have BeautifulSoup 4 installed already

from bs4 import BeautifulSoup
import urllib2

# Get the product search query from user and parse the page source of the search result from flipkart website
product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
content = urllib2.urlopen('http://www.flipkart.com/search?otracker=start&q='+product).read()

soup = BeautifulSoup(content)

# Parse the page source of the matched product and find the seller-name 
link = soup.find_all("div", class_="pu-title fk-font-13")[0].find_all('a')[0].get('href')
link = "https://www.flipkart.com%s" % link

seller_info = urllib2.urlopen(link).read()
link_soup = BeautifulSoup(seller_info)

try:
    title = link_soup.find_all("h1", class_="title")[0].string.strip()
    print "Title:    %s" % title
except:
    print "Product not found"	

try:
    subtitle = link_soup.find_all("span", class_="subtitle")[0].string.strip()
    print "Subtitle: %s" % subtitle
except:
    print "Subtitle: None"

try:
    price = link_soup.find_all("span", class_="selling-price omniture-field")[0].string.strip()
    print "Price:    %s" % 	price
except:
    pass

print "Link:     %s" % link	

try:
    seller = link_soup.find_all("a", class_="seller-name")[0].string.strip()
    print "Seller:   %s" % seller
except:
    pass

