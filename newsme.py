from bs4 import BeautifulSoup
import urllib.request
headers = {}
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

class NewsMe:
	def __init__(self, url):
		self.url = url

	def html(self):
		req = urllib.request.Request(self.url,headers=headers)
		resp = urllib.request.urlopen(req)
		scrap_data = BeautifulSoup(resp.read(), "html.parser")
		return scrap_data.prettify()
		
	def headlines(self):
		req = urllib.request.Request(self.url,headers=headers)
		resp = urllib.request.urlopen(req)
		scrap_data = BeautifulSoup(resp.read(), "html.parser")
		d_l = []
		scrap_data = [i.text for i in scrap_data.find_all("a")]
		n = AvgHeadLen(scrap_data)
		for i in scrap_data:
			if len(i.strip())>n:
				d_l.append(i.strip())
		return d_l


def AvgHeadLen(head_list):
	total_letter = 0
	for i in head_list:
		total_letter = total_letter+len(i.strip())
	return int(total_letter/len(head_list))