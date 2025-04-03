🔥 Advanced Proxy Checker

🚀 Advanced Proxy Checker is a high-performance tool for checking HTTP, HTTPS, SOCKS4, and SOCKS5 proxies with multi-threading support.  
It can automatically fetch fresh proxies from online sources or validate a given proxy list efficiently.

---

📌 Features  
✅ Supports HTTP, HTTPS, SOCKS4, SOCKS5 proxies  
✅ Auto-fetches fresh proxies from multiple API sources  
✅ Multi-threaded processing for faster validation  
✅ Detects Country, City, and Anonymity Level of proxies  
✅ Saves working proxies in a structured JSON file  
✅ Lightweight, fast, and easy to use  

---

⚙️ Installation  

📱 For Termux (Android)  
```bash
pkg update && pkg upgrade -y
pkg install python -y
pkg install git -y
git clone https://github.com/ceo-developer/Proxy_checker.git
cd Proxy_checker
pip3 install -r requirements.txt
```

🖥️ For Kali Linux / Ubuntu  
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/ceo-developer/Proxy_checker.git
cd Proxy_checker
pip3 install -r requirements.txt
```

---

🚀 Usage  

Basic Usage  
```bash
python3 proxy_checker.py
```

Example 1: Checking proxies from a file  
```
Enter Proxy List File (or type 'auto' to fetch from API): proxies.txt
Enter Proxy Type (socks4/socks5/http/https): https
Enter Number of Threads (default 50): 100
```

Example 2: Fetching Proxies Automatically  
```
Enter Proxy List File (or type 'auto' to fetch from API): auto
```

📂 Output Files:  
- ✅ Working Proxies: `working_proxies.json`  
- ❌ Not Working Proxies: `not_working_proxies.txt`  

---

📝 Output Format  
The working proxies will be saved in JSON format like this:  
```json
[
    {
        "proxy": "123.45.67.89:8080",
        "latency": 0.534,
        "country": "United States",
        "city": "New York",
        "anonymity": "Elite"
    }
]
```

---

🔧 How It Works  
1️⃣ Loads proxies from a file or API sources  
2️⃣ Uses multi-threading for fast validation  
3️⃣ Checks each proxy by sending requests to an API  
4️⃣ Saves working proxies with response time, country, and anonymity level  

---

🛡️ License  
This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it.  

---

👤 Developer Info  
👨‍💻 Developer: [dəˈveləpər](https://github.com/hiden_25)
👨‍💻 Contribute: H2I TEAM
📢 Telegram Channel: [H2I CODER](https://t.me/h2icoder)  

---

⭐ If you find this tool useful, don't forget to star the repository on GitHub! ⭐  

---
