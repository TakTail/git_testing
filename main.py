import requests

website = requests.get('http://x.com')


if website.status_code == 200:
    print(f"code={website.status_code} | Success!")
    print(f"website content: {website.text}")
elif website.status_code == 404:
    print(f"code={website.status_code} | Not Found.")
else:
    print(f"code={website.status_code} | Unknown Error!")