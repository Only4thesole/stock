# Developed by @cookiepluhg

import requests, json, os.path

# Check if a valid config file exists.
if not os.path.exists('config.json'):
	print "Config file not found!"
	exit()
else:
	with open('config.json') as json_data:
		config = json.load(json_data)


# Function that prints the banner.
def printBanner(productId):
	print "-------------------------------------------"
	print " Retrieving stock for " + productId.upper() + " on Adidas GB"
	print "-------------------------------------------"
	print " VARIANT \t  SIZE \t\tSTOCK"
	print "-------------------------------------------"


# Function that retrieves the stock.
def retrieveStock(productId):
	URL = "http://www.adidas.com.au/on/demandware.store/Sites-adidas-GB-Site/en_GB/Product-GetVariants?pid=" + productId.upper()

	session = requests.Session()
	source_code = session.get(URL)

	if "Page not found" in source_code.text:
		print " Invalid product ID."
		exit()
	else:
		data = source_code.json()

	for l in data['variations']['variants']:
		variant = l['id']
		size = l['attributes']['size']
		stock = str(int(l['ATS']))

		print (" %s\t  %s\t\t%s" % (variant, size, stock))

	print "-------------------------------------------"


# Main function.
def main():
	pId = config['product_code']
	printBanner(pId)
	retrieveStock(pId)

main()
