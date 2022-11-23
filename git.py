import requests

website = requests.get('http://x.com')


if website.status_code == 200:
    print('Success!')
    print(website.text)
elif website.status_code == 404:
    print('Not Found.')
else:
    print("Unknown Error!")