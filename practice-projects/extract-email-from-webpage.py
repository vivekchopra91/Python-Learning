from requests_html import HTMLSession
import re
# from bs4 import BeautifulSoup

url =r"https://www.randomlists.com/email-addresses"

pattern =r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

session = HTMLSession()

response = session.get(url)

response.html.render()

body = response.html.find("body")[0]

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", body.text)

for index,email in enumerate(emails):
    print(index+1, "---->", email)