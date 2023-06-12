import requests

url = "https://alpha-vantage.p.rapidapi.com/query?interval=5min&function=TIME_SERIES_INTRADAY&symbol=MSFT&datatype=json&output_size=compact"
headers = {
'x-rapidapi-key': " 14e58ca9ccmshfd7b68165c8bd40p1a1c44jsncc2652d4ca2c",
'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers)
print(response.text)