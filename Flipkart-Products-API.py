########################################
#     				       #
#	Flipkart Products API	       #
#	     Version 1.0     	       #
#				       #
#       Developer: Shreesha.S	       #
#  Contact: shreesha.suresh@gmail.com  #
#				       #
########################################


# Running this script returns the product details of the best matched product on flipkart based on the input string given

import urllib2

# Returns the details after slicing
def details(count, product):
	data = loadURL(product)
	str1 = data[count:(count + 500)]
	detail_start = str1.find(">") + 1
	detail_end = str1.find("<")
	return str1[detail_start:detail_end]	

# Loads the page source of the URL
def loadURL(product):
	req = urllib2.urlopen('http://www.flipkart.com/ph/search/pr?q='+product+'&otracker=start&fromAS=false&showAS=false&_submit=').read()
	return req

# Takes the product name / search query as input
product = raw_input("Enter product name: ")
product = product.replace(' ', '+')
data = loadURL(product)

# Print product title 
product_title = data.find('class="fk-product-title"')
print "Title:    %s" % (details(product_title, product))

# Print product sub title
product_sub_title = data.find('class="fk-product-subtitle"')
print "Sub Tile: %s" % (details(product_sub_title, product))

# Print product price
price_slice = data.find('class="fk-product-price "')
print "Price:    %s" % (details(price_slice, product))

# Print the product link
product_link = data.find('class="fk-product-link"')
data = loadURL(product)
str1 = data[(product_link+32):(product_link + 1000)]
stop = str1.find('"')
link = data[(product_link + 31):((product_link + 32) + stop)]
print "Link:     https://www.flipkart.com%s" % link


#####################################################################
#								    #
#  There might be some data lost while retrieving the information.  #
#  In those cases please try retrieving the information again.	    #
#								    #
#####################################################################
