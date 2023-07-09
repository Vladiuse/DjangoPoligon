import json
import requests as req


# token = 'T5Ug9l_5gStBTeg6mUCUSQ25hjAZbRjO'
# url = f'https://api.kma.biz/?method=getoffers&token={token}&return_type=json'
# res = req.get(url)
# result = res.json()
#
# offers = result['offers']
# with open('offers_names.txt', 'w') as file:
#     for offer in offers:
#         name = offer['name']
#         file.write(name+'\n')

with open('offers_names.txt', ) as file:
    for line in file:
        offer = line.strip()
        if '-' not in offer and '–' not in offer:
            print(offer)

