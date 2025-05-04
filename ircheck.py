#!/usr/bin/env python3
import requests
import time
from colorama import init, Fore

init(autoreset=True)

def show_logo():
    blue = "\033[94m"
    reset = "\033[0m"
    print(blue + """
       _________
     /         \\
    |  O     O  |
    |     ^     |
    |   \\___/   |
     \\_________/

        ircheck
    """ + reset)

sites = {
    "Divar": "https://divar.ir/u/{}",
    "Sheypoor": "https://www.sheypoor.com/u/{}",
    "Zoomg": "https://www.zoomg.ir/user/{}/",
    "Zoomit": "https://www.zoomit.ir/user/{}/",
    "Vigiato": "https://vigiato.net/user/{}/",
    "Gamefa": "https://gamefa.com/user/{}/",
    "Rubika": "https://rubika.ir/{}",
    "Filimo": "https://www.filimo.com/user/{}",
    "Namava": "https://www.namava.ir/user/{}",
    "Tamasha": "https://tamasha.com/{}",
    "Telewebion": "https://www.telewebion.com/user/{}",
    "Shad": "https://shad.ir/{}",
    "Eitaa": "https://eitaa.com/{}",
    "Aparat": "https://www.aparat.com/{}",
}
def check_username(username):
    for name, url in sites.items():
        full_url = url.format(username)
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Found on {name}: {full_url}")
            elif response.status_code == 404:
                print(Fore.RED + f"[-] Not found on {name}")
            else:
                print(Fore.YELLOW + f"[!] Error checking {name} (status: {response.status_code})")
        except requests.RequestException:
            print(Fore.YELLOW + f"[!] Error connecting to {name}")
        time.sleep(0.5)

if __name__ == "__main__":
    show_logo()
    user = input("Enter the username to check: ")
    print()
    check_username(user)
