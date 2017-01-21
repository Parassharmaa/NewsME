from newsme.nm import NewsMe
url = "http://timesofindia.indiatimes.com/"

N = NewsMe(url)

for i in N.headlines():
	print(i)
