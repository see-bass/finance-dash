import requests

url = "https://morning-star.p.rapidapi.com/stock/v2/get-financial-details"

querystring = {"performanceId":"0P0000OQN8","dataType":"A","reportType":"A","type":"incomeStatement"}

headers = {
	"X-RapidAPI-Key": "8c86128819msh99c25f8c2e98232p12f358jsna52fccb57dbb",
	"X-RapidAPI-Host": "morning-star.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())