import requests
import time


def get_mobile_number_info(phone_number):
    api_key = 'aFwivIX8hJHIPYF3VPfyFgFtwIdLJsq6' 
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            if data['valid']:
                
                print(f"\033[1;32m Country: {data['country_name']}")
                print(f"\033[1;32m Phone Number: {data['international_format']}")
                print(f"\033[1;32m Location: {data['location']}")
                print(f"\033[1;32m Carrier: {data['carrier']}")
                print(f"\033[1;32m Line Type: {data['line_type']}")
            else:
                print(f"Invalid phone number: {phone_number}")
        else:
            print("Error: Unable to fetch data.")
    except Exception as e:
        print(f"An error occurred: {e}")