# -*- coding: UTF-8 -*-
"""
@File: crawl_live.py
@Description: 
@Author: lee sure
@DateTime: 2022/06/10 01:19
@Project_name: python-advanced
@IDE: PyCharm
"""

import requests

from selenium import webdriver


def main():
    # 请求头
    headers = {
        "Host": "moodle.uowplatform.edu.au",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Referer": "https://moodle.uowplatform.edu.au/login/index.php",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        # "Cookie": "MoodleSession=bprleqrqmsp5cbgvv6qtmd45k4"
    }
    url_moodle_home = 'https://moodle.uowplatform.edu.au/my/'

    r = requests.request("get", url_moodle_home, headers=headers)
    print(r.content.decode("utf-8"))



    # html_content = r.content.decode("utf-8")
    # soup = BeautifulSoup(html_content, 'html.parser')
    # headers["logintoken"] = soup.select("input[name='logintoken']")[0].attrs['value']
    # print(headers)
    # r2 = requests.request("get", url1, headers=headers, allow_redirects=True,
    #                       auth=HTTPDigestAuth("xl090", "xluow1995@"), verify=False)

    # 需求用的的请求数据
    # data = {"logintoken": soup.select("input[name='logintoken']")[0].attrs['value'],
    #         "username": "xl090", "password": "xluow1995@", "rememberusername": "1"}

    # r2 = requests.request("post",r.url, headers=headers,data=data)
    # print(r2.headers.get("Set-Cookie").split(";")[0])
    # headers['Cookie']=r2.headers.get("Set-Cookie").split(";")[0]
    # print(headers)

    # r3 = requests.request("get", url1, headers=headers)



if __name__ == '__main__':
    main()
