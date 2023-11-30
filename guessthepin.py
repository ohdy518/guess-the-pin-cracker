import requests

cookies = {
    'GDPR': 'true',
}

headers = {
    'authority': 'www.guessthepin.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'GDPR=true',
    'origin': 'https://www.guessthepin.com',
    'referer': 'https://www.guessthepin.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

data = {
    'guess': '1000',
}

start = int(input("Start: "))
end = int(input("End: "))

for i in range(start, end, 1):
    data['guess'] = "0" * (4-len(str(i))) + str(i)
    response = requests.post('https://www.guessthepin.com/prg.php', cookies=cookies, headers=headers, data=data)
    if "is not the PIN." in str(response.content):
        print("No:", data["guess"])
    else:
        print("Yes:", data['guess'])
        exit()
