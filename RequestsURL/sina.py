# -*- coding:utf-8 -*-
import requests

from Util import util
from Config import basicConfig


# 个股详情数据: 今开,昨收,最高,最低等
def sina_basic(stock_market, stock_code):
    if stock_code == "DJI":
        stock_code == "dji,gb_ixic,gb_inx,hf_DJS,hf_NAS"

    url = "http://hq.sinajs.cn/?list=" + stock_market + stock_code
    if stock_market == "hk":
        url = "http://hq.sinajs.cn/?_=%s&list=rt_%s" % (util.get_request_id(), stock_market + stock_code)
    if stock_market in ["am", "ny", "ar", "oq", "ix"]:
        url = "http://hq.sinajs.cn/?list=gb_%s" % stock_code.lower()
    try:
        r = requests.get(url)
        return r.text
    except:
        return basicConfig.ResponseError.get("code")


if __name__ == '__main__':
    print sina_basic("ix", "INX")



