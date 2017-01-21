#NewsME  
##A Headline-Scrapper

`Python Script to scrap the news headlines from news-websites. (Accuracy 88%)`

**
###Usage::

1.Get Beutified HTML
```python
from newsme import NewsMe
url = "http://timesofindia.indiatimes.com/"

N = NewsMe(url)

print(N.html())

```

2.Get headlines:
```python
from newsme import NewsMe
url = "http://timesofindia.indiatimes.com/"

N = NewsMe(url)

for n in N.headlines():
	print(i)

```
***
###External Dependencies:
*beautifulsoup4
*urllib

***
###Contribute
New Features and Contributions are accepted

####Under Construction
