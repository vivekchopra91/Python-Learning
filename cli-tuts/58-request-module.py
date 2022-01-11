import requests

# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")        # get all content of that url
# print(r.text)
# print(r.status_code)

url = "http://www.something.com"

data = {
    "p1":4,
    "p2":8
}
r2 = requests.post(url=url, data=data)
print(r2.status_code)