import urllib.request

url = "https://backup.0x10.cloud/.env.backup"

try:
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')

    print ("respond received from server\n")

    if "DB_PASS" in content or "SECRET" in content:
        print("[+] Sensitive backup file is accessible")

    else:
        print("[-] No sensitive data found")

except Exception as e:
    print("Error: ", e) 