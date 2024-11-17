import requests

def track_ip(ip_address):
    api_url = f"http://ip-api.com/json/{ip_address}?fields=status,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,mobile,proxy,hosting,query"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        details = [
            f"\033[1;32m Status: {data['status']}",
            f"\033[1;32m IP Address: {data['query']}",
            f"\033[1;32m Country: {data['country']}",
            f"\033[1;32m City: {data['city']}",
            f"\033[1;32m Region: {data['region']}",
            f"\033[1;32m ISP: {data['isp']}",
            f"\033[1;32m Zip Code: {data['zip']}",
            f"\033[1;32m Latitude: {data['lat']}",
            f"\033[1;32m Longitude: {data['lon']}",
            f"\033[1;32m Time Zone: {data['timezone']}",
            f"\033[1;32m Country Code: {data['countryCode']}",
            f"\033[1;32m Currency: {data['currency']}",
            f"\033[1;32m Region Name: {data['regionName']}",
            f"\033[1;32m Organisation: {data['org']}",
            f"\033[1;32m Continent Code: {data['continentCode']}",
            f"\033[1;32m Mobile Number: {data['mobile']}",
            f"\033[1;32m Hosting: {data['hosting']}"
        ]

        for line in details:
            print(line)

        with open("ip_details.txt", "w") as file:
            for line in details:
                file.write(line + "\n")

        print("\nDetails saved to 'ip_details.txt'")

    else:
        print("Failed to retrieve IP information")
