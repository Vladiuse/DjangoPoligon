import requests as req

API_KEY = 'b6fa521878b3a56abce39d79857aa8a9b08f81d0dab0cf6a9cef84abca07d2b2'
API_KMA_ACC = 'ec20023c0f0b67f8cb43a3a9b828fd539bdc85a8c0af5373836688f3a37ed09f'
headers = {'x-apikey': API_KMA_ACC}
api_url = 'https://www.virustotal.com/api/v3/urls'
# data = {
#     'url': 'bromelain-new.com'
# }
# res = req.post(api_url, data=data, headers=headers)
# print(res.status_code)
# print(res.text)


# data = {
#     'id': 'u-1c63fae18d719b07a7d079b0d2b16e73ee51eae05f2b0b9bde2070ca889aa991-1678952769'
# }
# api_url = f'https://www.virustotal.com/api/v3/analyses/u-1c63fae18d719b07a7d079b0d2b16e73ee51eae05f2b0b9bde2070ca889aa991-1678952769'
# res = req.get(api_url,headers=headers)
# print(res.status_code)
# print(res.text)

def get_domain_check_id(url):
    data = {
        'url': url
    }
    res = req.post(api_url, data=data, headers=headers)
    if res.status_code == 200:
        pass
    else:
        print(res.status_code, url)
        print(res.json())
    try:
        check_id = res.json()['data']['id']
        return check_id
    except Exception as error:
        print(url, error)
        return None

def get_checked_data(check_id):
    api_url = f'https://www.virustotal.com/api/v3/analyses/{check_id}'
    try:
        res = req.get(api_url,headers=headers)
        return res.json()
    except Exception as error:
        print(check_id, error)
        return None


check_id = get_domain_check_id('n.full.pantogor-new.com')
if check_id:
    check_data = get_checked_data(check_id)
    print(check_id)
    print(check_data)


