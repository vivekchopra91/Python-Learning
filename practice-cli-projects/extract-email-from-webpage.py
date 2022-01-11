from requests_html import HTMLSession
import re
# from bs4 import BeautifulSoup

url =r"https://softobiz.com/contact-us/"

pattern =r"\w+@\S+\w"

session = HTMLSession()

response = session.get(url)

response.html.render()

body = response.html.find("body")[0]

emails = re.findall(r"\w+@\S+\w", body.text)

for index,email in enumerate(emails):
    print(index+1, email)