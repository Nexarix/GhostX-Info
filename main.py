import time
import subprocess
import sys
import os
import requests
from IpAddress.Ipaddress import *  # Ensure this is correctly imported
from MobileNumber.mobilenumber import get_mobile_number_info  # Ensure correct import

osystem = sys.platform

if osystem == "linux":
    os.system("clear")
else:
    os.system("cls")


def my_profile():
    dis = '''
          ┏━━┓┏━┓──┏━━┓────┏━┓───┏┓┏┓──── 
          ┗┃┃┛┃┃┃──┗┃┃┛┏━┳┓┃━┫┏━┓┗┓┏┛──── 
          ┏┃┃┓┃┏┛──┏┃┃┓┃┃┃┃┃┏┛┃┃┃┏┛┗┓────    
          ┗━━┛┗┛───┗━━┛┗┻━┛┗┛─┗━┛┗┛┗┛──── 
    '''
    bot_img = '''               ╶╶╶╶╭─┬─╮╭──╮╭╮╭╮╶╶╶╶ 
               ╶╶╶╶││││││╭─┤╰╮╭╯╶╶╶╶ 
               ╶╶╶╶││││││╰╮│╭╯╰╮╶╶╶╶ 
               ╶╶╶╶╰┴─┴╯╰──╯╰╯╰╯╶╶╶╶ 
    '''
    time.sleep(2)
    print(f"\033[1;36m{dis}")
    print(f"\033[1;36m{bot_img}")
    print("                      join my group: ")
    print(f"      \033[1;31m https://chat.whatsapp.com/DgVXxCESDZrGIiInRTjgtK")


my_profile()

print(f"\033[1;30m−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
print(f"\033[1;34m 1. IpAddress Information")
print(f"\033[1;34m 2. Mobile Number Information")
print(f"\033[1;30m−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
user_input = input("\033[1;32m Select the option: ").strip()

if user_input == "1":
    ip_address = input(f" Enter your IP Address: ").strip()
    time.sleep(1.5)
    print(" Please wait................")
    print(f"\033[1;30m−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    time.sleep(6)
    # Ensure track_ip function is implemented and available
    print(track_ip(ip_address))
    print(f"\033[1;30m−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

elif user_input == "2":
    phone_number = input(f" Enter your Mobile Number: ").strip()
    time.sleep(1.5)
    print(" Please wait................")
    print(f"\033[1;30m−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    time.sleep(6)
    # Ensure get_mobile_number_info function is implemented and available
    print(get_mobile_number_info(phone_number))
    print(f"\033[1;30m−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

else:
    print("\033[1;31m Invalid option. Please select either 1 or 2.\033[0m")
