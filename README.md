#NewsME  
##A Headline-Scrapper

`Python Script to scrap the news headlines from news-websites.`

***
###Usage::
1.Importing 
```python

from newsme.nm import NewsMe

```

2.Get Beutified HTML
```python

url = "http://thehindustantimes.com"

N = NewsMe(url)

print(N.html())

```

3.Get headlines with urls:
```python

N.headlines()

```
4. Change the order to fetch more accurate healines data
```python

N = NewsMe(url, order=3)

```
***
###External Dependencies:

* beautifulsoup4
* urllib

***
###Contribute
New Features and Contributions are accepted.

####Under Construction
