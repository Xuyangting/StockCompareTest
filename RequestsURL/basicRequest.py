# -*- coding:utf-8 -*-
import requests

from Config import basicConfig, basicApi


def basic_request(url, payload):
    s = requests.Session()
    # 重试3次
    retry_num = requests.adapters.HTTPAdapter(max_retries=3)
    try:
        if payload == {}:
            r = s.post(url, retry_num)
        else:
            r = s.post(url, params=payload)
        result = r.json()
    except:
        result = basicConfig.ResponseError
    return result


def request_get(url):
    try:
        r = requests.get(url)
        result = r.json()
    except:
        result = basicConfig.ResponseError
    return result


if __name__ == '__main__':
    print basic_request(basicApi.basic, basicApi.get_basic_payload("hk", "00376", "010104"))





