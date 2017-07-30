from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("C:\Users\spook\Dropbox\Pythoncourse\Udemey\lottoTestFile.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
