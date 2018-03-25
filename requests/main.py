import json
import requests
from requests import exceptions

URI = "https://api.github.com"


def build_uri(endpoint):
    return "/".join([URI, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_get():
    response = requests.get(build_uri('search/repositories'), params={'q': 'requests'})
    print(better_print(response.text))
    print(response.url)
    print(response.request.headers)


def request_time():
    try:
        response = requests.get(build_uri('search/repositories'), params={'q': 'requests'}, timeout=0.1)
    except exceptions.Timeout as e:
        print(e)
    else:
        print(response.text)


def hard_request():
    from requests import Request, Session
    headers = {'User-Agent': 'fk1.2'}
    req = Request('Get', build_uri('search/repositories'), params={'q': 'requests'}, headers=headers)
    prepare = req.prepare()
    print(prepare.body)
    print(prepare.headers)
    s = Session()

    resp = s.send(prepare)
    print(resp.status_code)


def download_img():
    url = 'https://media.giphy.com/media/7vAgWaCVHmRjPK2MgF/giphy-downsized.gif'
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as resp:
        with open('giphy.gif', 'wb') as fd:
            for chunk in resp.iter_content(128):
                fd.write(chunk)


def call_back(response, *args, **kwargs):
    print(response.status_code)


def async_request():
    """
    通过事件回调方式完成
    :return:
    """
    response = requests.get(build_uri('search/repositories'), params={'q': 'requests'}
                            , hooks=dict(response=call_back))


def basic_auth():
    response = requests.get(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(response.status_code)


def basic_oauth():
    header = {'Authorization': 'token e7aa7cd9addd64efa1b21dee317819b5c60a84a4'}
    response = requests.get(build_uri('user'), headers=header)
    print(response.status_code)


from requests.auth import AuthBase


class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization']=' '.join(['token',self.token])
        return r


def basic_oauth1():
    auth = GithubAuth('e7aa7cd9addd64efa1b21dee317819b5c60a84a4')
    response = requests.get(build_uri('user'), auth=auth)
    print(response.status_code)


if __name__ == '__main__':
    basic_oauth1()
