#################################################################################################################
##  CCBH Phone Lookup can be used to look up a text file of phone numbers                                       #
##   Created May 1 2013 by Carl Preusser                                                                        #
#################################################################################################################

# Import system modules
import urllib2
from xml.dom.minidom import parse, parseString

apikey = "enteryourapikeyhere"
apiST_HN = "1234" 
apiST_StreetName = "Spooner"
apiST_City = "New%25York"
apiST_State = "New%25York"

encoded_args = "house=" + apiST_HN + "&street=" + apiST_StreetName + "&city=" + apiST_City + "&state=" + apiST_State + "&areacode=&outputtype=XML&api_key=" + apikey


#change to existing and relevant API
#check it out here: http://pro.whitepages.com/developer/
url = 'http://api.whitepages.com/reverse_address/1.0?' + encoded_args

response = urllib2.urlopen(url)

#for line in response:
#    print line

data = response.read()
response.close()

responseXML = parseString(data)
xmlTag = responseXML.getElementsByTagName('wp:displayname')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
xmlData=xmlTag.replace('<wp:displayname>','').replace('</wp:displayname>','')
#print out the xml tag and data in this format: <tag>data</tag>
#print xmlTag
#just print the data
name = xmlData

address = apiST_HN + " " + apiST_StreetName + ", " + apiST_City
phoneNumber = "phonenumberfromapi"        
message = " add a message "        
dailyRecord = address + ". called " + name + message + phoneNumber 

print dailyRecord
 
