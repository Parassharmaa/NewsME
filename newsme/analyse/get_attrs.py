import requests
from bs4 import BeautifulSoup

main_tags = ["h"+str(i) for i in range(1,7)]
main_tags.append("div")
print(main_tags)

def classes(d):
	soup = BeautifulSoup(d, "html.parser")
	cl = []
	for t in main_tags:
		cl.append([i.get('class') for i in soup.select('t')])
		print(cl)


	return cl


if __name__ == "__main__":
	d  = requests.get("http://thehindu.com").text
	print(classes(d))
