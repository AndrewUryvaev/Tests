import requests

token_ya = ''

def get_headers(token):
    return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }
def get_foldres():
    foldres = 'new_foldres'
    file_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = get_headers(token_ya)
    #res_d = requests.delete(f'{file_url}?path={foldres}',headers=headers)
    res_c = requests.put(f'{file_url}?path={foldres}',headers=headers)

    return res_c.status_code

get_foldres()