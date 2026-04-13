import urllib.request

url = "https://files.0x10.cloud/.env"

try:
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')

    print ("respond received from server\n")

    if len(content) > 0:
        print("[+] .env file may be accessible")

    else:
        print("[-] No content found")

except Exception as e:
    print("Error: ", e)  