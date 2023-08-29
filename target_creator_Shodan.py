import requests

SHODAN_API_KEY = "BURAYA_SHODAN_API_ANAHTARINIZI_YAZIN"
search_query = "Apache"

url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={search_query}"

response = requests.get(url)
data = response.json()

ip_addresses = [result["ip_str"] for result in data["matches"]]

with open("ip_addresses.txt", "w") as file:
    for ip in ip_addresses:
        file.write(ip + "\n")
