from newsme.nm import NewsMe
url = "http://timesofindia.indiatimes.com/"

N = NewsMe(url)

print(N.html())
