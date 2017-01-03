from newsme import NewsMe
url = "http://businessinsider.com" 

N = NewsMe(url)

for i in N.headlines():
	print(i)