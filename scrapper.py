from bs4 import BeautifulSoup
import requests, shutil, random, string
import os

def create_dirs(url):
	urlData = url.split('/');
	boardPath = 'images/' + urlData[-4]
	threadPath = boardPath + '/' + urlData[-1];

	if not os.path.exists('images'):
		os.makedirs('images')
	if not os.path.exists(boardPath):
		os.makedirs(boardPath)
	if not os.path.exists(threadPath):
		os.makedirs(threadPath)
	return threadPath

def resource_img(url, dirname):
	filename = url.split('/')[-1]
	filePath = dirname + '/' + filename
	if not os.path.exists(filePath):
		response = requests.get(url, stream = True)
		with open(filePath, 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response
		print(filename + ' ' + url)
		return 1
 	else: 
 		return 0


#url = "http://boards.4chan.org/hr/thread/2485923/vanessa-hudgens"
print '<-- :::::: Python Scrapper ::::::-->'
url = raw_input('Enter your input:')
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
dirname = create_dirs(url)
resources = 0

links = soup.find_all('a', class_='fileThumb')
for link in links:
	resources = resources + resource_img('http:' + link.get('href'), dirname)

print resources, ' Resources Downloaded.'