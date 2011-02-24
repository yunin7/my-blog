import urllib, urllib2, simplejson

atext = 'Hello world!'

atext = urllib.urlencode(atext)
url = ('http://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q=%s&langpair=en|ru' % (atext))

request = urllib2.Request(url, None, {'Referer':'localhost'})
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)
print results['responseData']['translatedText']

