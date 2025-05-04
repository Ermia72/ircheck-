import requests

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

username = input("Enter username to check: ")

sites = [
    "https://www.aparat.com/{}",
    "https://eitaa.com/{}",
    "https://ble.ir/{}",
    "https://gap.im/{}",
    "https://iGap.net/{}",
    "https://bale.ai/{}",
    "https://rubika.ir/{}",
    "https://www.filimo.com/user/{}",
    "https://www.namava.ir/profile/{}",
    "https://tamasha.com/{}/",
    "https://www.telewebion.com/user/{}",
    "https://divar.ir/u/{}",
    "https://www.sheypoor.com/profile/{}",
    "https://www.zoomit.ir/user/{}",
    "https://www.vigiato.net/author/{}",
    "https://zoomg.ir/user/{}",
    "https://gamefa.com/author/{}",
    "https://shad.ir/{}"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for site in sites:
    url = site.format(username)
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}[FOUND] {url}{RESET}")
        elif response.status_code == 404:
            print(f"{RED}[NOT FOUND] {url}{RESET}")
        else:
            print(f"{YELLOW}[UNKNOWN STATUS {response.status_code}] {url}{RESET}")
    except requests.RequestException as e:
        print(f"{YELLOW}[ERROR] {url} -> {e}{RESET}")
