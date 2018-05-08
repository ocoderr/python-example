import requests,re
import time
base_url = 'https://sukebei.nyaa.si'


def parse_html(html):
    tbody = re.search('<tbody>(.*?)</tbody>', html, re.S).group(1)
    # print(tbody)
    tr_list = re.findall(
        r'<tr (.*?)alt="(.*?)">(.*?)href="(.*?)" title="(.*?)">(.*?)href="(.*?)">(.*?)<td (.*?)>(.*?)</td>(.*?)<td (.*?)>(.*?)</td>(.*?)</tr>',
        tbody, re.S)

    for tr in tr_list:
        time.sleep(1)
        save(tr[6])
        print(tr[1], tr[3], tr[4], tr[6], tr[9], tr[12])


def save(download_link):
    no = re.search(r'/download/(\d*?).torrent',download_link).group(1)
    reps = requests.get(base_url + download_link, headers=header)
    fd = open(no+".torrent", 'wb')
    fd.write(reps.content)
    fd.close()




header = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'cookie': '__cfduid=d7d4252990644f8048570eedf7797b40f1523262220; _ga=GA1.2.820761005.1523262095; _gid=GA1.2.1159889298.1523262095; _gat_gtag_UA_107733743_3=1',
}
reps = requests.get(base_url, headers=header)

html = reps.text
parse_html(html)


