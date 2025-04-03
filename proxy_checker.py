# Made by @hiden_25 And H2I TEAM
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Initialize colorama for colored output

PROXY_API_URLS = [
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxyscrape.com/free-proxy-list",
    "https://spys.one/en/free-proxies/"
]

def fetch_proxies():
    proxies = set()
    for url in PROXY_API_URLS:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies.update(response.text.splitlines())
        except:
            continue
    return list(proxies)

print(Back.BLACK + Fore.CYAN + "Developer:- github.com/")
print(Back.BLACK + Fore.YELLOW + "Telegram:- @hiden_25")

proxy_list_file = input(Back.BLACK + Fore.GREEN + "Enter Proxy List File (or type 'auto' to fetch from API): ").strip()
proxy_type = input(Back.BLACK + Fore.GREEN + "Enter Proxy Type (socks4/socks5/http/https): ").strip()
thread_count = int(input(Back.BLACK + Fore.GREEN + "Enter Number of Threads (default 50): ") or "50")

if proxy_list_file.lower() == "auto":
    proxy_list = fetch_proxies()
    print(Back.BLACK + Fore.GREEN + f"✅ {len(proxy_list)} proxies fetched from API.")
else:
    try:
        with open(proxy_list_file, "r") as file:
            proxy_list = list(set(file.read().split()))
    except FileNotFoundError:
        print(Back.BLACK + Fore.RED + f"❌ Error: File '{proxy_list_file}' not found!")
        exit()

working_proxies = []

def check_proxy(proxy):
    try:
        start_time = time.time()
        response = requests.get(
            "https://ipwho.is/",
            timeout=5,
            headers={"User-Agent": "Advanced Proxy Checker"},
            proxies={"https": f"{proxy_type}://{proxy}"}
        )
        elapsed_time = round(time.time() - start_time, 3)
        data = response.json()

        if data.get("success"):
            working_proxies.append({
                "proxy": proxy,
                "latency": elapsed_time,
                "country": data.get("country", "Unknown"),
                "city": data.get("city", "Unknown"),
                "anonymity": "Elite" if "X-Forwarded-For" not in response.headers else "Anonymous"
            })
            print(Back.BLACK + Fore.GREEN + f"✅ {proxy} - {data.get('country', 'Unknown')}, {data.get('city', 'Unknown')} | {elapsed_time}s")
        else:
            print(Back.BLACK + Fore.RED + f"❌ {proxy} - Invalid Proxy")
    except requests.RequestException:
        print(Back.BLACK + Fore.RED + f"❌ {proxy} - Connection Failed")

with ThreadPoolExecutor(max_workers=thread_count) as executor:
    executor.map(check_proxy, proxy_list)

output_json = f"{proxy_type}_working_proxies.json"
with open(output_json, "w") as file:
    json.dump(working_proxies, file, indent=4)

print(Back.BLACK + Fore.CYAN + f"\n🎯 {len(working_proxies)} Working Proxies Saved in JSON!")
print(Back.BLACK + Fore.YELLOW + f"📁 JSON File: {output_json}")

# Made by @hiden_25 And H2I TEAM
