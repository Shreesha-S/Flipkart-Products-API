########################################################
#     	 			                       #
#	        Flipkart Products API	               #
#	             Version 2.0     	               #
#	    		 		               #
#               Developer: Shreesha.S	               #
#          Contact: shreesha.suresh@gmail.com	       #
#				                       #
########################################################


# Running this script returns the product details of the best matched product on flipkart based on the input string given
# Make sure you have BeautifulSoup 4 installed already

from bs4 import BeautifulSoup
import urllib2

# Get the product search query from user and parse the page source of the search result from flipkart website
product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
content = urllib2.urlopen('http://www.flipkart.com/ph/search/pr?q='+product+'&otracker=start&fromAS=false&showAS=false&_submit=').read()
soup = BeautifulSoup(content)

# Parse the page source of the matched product and find the seller-name 
link = "https://www.flipkart.com%s" % soup.find_all("a", class_="fk-product-link")[0].get('href')	
seller_info = urllib2.urlopen(link).read()
link_soup = BeautifulSoup(seller_info)


try:
	print "Title:    %s" % soup.find_all("span", class_="fk-product-title")[0].string.strip()
except:
	print "Product not found"	

try:	
	print "Subtitle: %s" % soup.find_all("span", class_="fk-product-subtitle")[0].string.strip()
except:
	print "Subtitle: None"

try:
	print "Price:    %s" % soup.find_all("span", class_="fk-product-price")[0].string.strip()	
except:
	pass

print "Link:     %s" % link	

try:
	print "Seller:   %s" % link_soup.find_all("a", class_="seller-name")[0].string.strip()	
except:
	pass
