import urllib
import urllib2
import json
from datetime import datetime, timedelta
from  pytz import timezone


symbolslist = open("/home/lumatthews/scripts/stocks/followstocks.txt").read()
symbolslist = symbolslist.split("\n")


for symbol in symbolslist:
	long = len(symbol)
	if long != 0:
		myfile = open("/home/lumatthews/scripts/stocks/price_history/"+symbol+".txt","w+")
		myfile.close()
		htmltext = urllib.urlopen("http://www.bloomberg.com/markets/api/bulk-time-series/price/"+symbol+"%3AUS?timeFrame=1_DAY")
		data = json.load(htmltext)
		try:
			datapoints = data[0]['price'] 
		except KeyError:
			pass
	else:
		pass
	for point in datapoints:
		if long != 0:
			try:
				current_time = datetime.strptime(point['dateTime'], '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=5)
				myfile = open("/home/lumatthews/scripts/stocks/price_history/"+symbol+".txt","a")
				myfile.write("{0},{1},{2}\n".format(symbol, point['value'], current_time))
				myfile.close()
				#print "Price:", point['value'], "Time:", current_time
			except:
				pass
		else:
			pass
	if long != 0:
		insert_time = datetime.now().time()
		print "symbol",symbol, "has been updated to the records @ ",insert_time 
		print "the number of points is ", len(datapoints)
	else:
		pass



#print datapoints[len(datapoints)-1]['value']



#data_read = data[0]['price']
#for price in data_read:
#	print "Price:", price[0]['value']

#print '"price":', data[0]['price'][0]['value']





#print "SPACE"
#print "SPACE"
#print "SPACE"


#data_clean = json.dumps(data, sort_keys=True, indent=4)
#print data_clean

