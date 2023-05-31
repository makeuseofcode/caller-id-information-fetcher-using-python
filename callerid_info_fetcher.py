import requests

number = input("Enter valid number:")
print("--------------------------------------")
api = 'YOUR_API_KEY'
url = 'http://apilayer.net/api/validate?access_key=' + api + '&number=' + number
response = requests.get(url)
answer = response.json()
if answer["valid"] == True:
    print("Number:",answer["number"])
    print("Local format:", answer["local_format"])
    print("International format:",answer["international_format"])
    print("Country prefix:",answer["country_prefix"])
    print("Country code:",answer["country_code"])
    print("Country name:",answer["country_name"])
    print("Location:",answer["location"])
    print("Carrier:",answer["carrier"])
    print("Line type:",answer["line_type"])
else:
    print("Invalid API key or number. Please try again.")
