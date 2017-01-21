#NewsME  
##A Headline-Scrapper

`Python Script to scrap the news headlines from news-websites. (Accuracy 88%)`

***
###Usage::

1.Get Beutified HTML
```python
from newsme.nm import NewsMe
url = "http://timesofindia.indiatimes.com/"

N = NewsMe(url)

print(N.html())

```

2.Get headlines with urls:
```python
from newsme.nm import NewsMe
url = "http://timesofindia.indiatimes.com/"

N = NewsMe(url)

N.headlines()

```

***
###External Dependencies:
**beautifulsoup4

***
###Contribute
New Features and Contributions are accepted

####Under Construction
