# -*- coding:utf-8 -*-
import basicRequest
import time

from Util import util
from Config import basicConfig


# 异常股票进行转换
def change_abnormal_stock(stock_code):
    if stock_code == "INX":
        stock_code = ".INX"
    if stock_code == "HSI":
        stock_code = "800000"
    if stock_code == "HSCCI":
        stock_code = "800151"
    return stock_code


# 获取 security_id
def get_security_id(stock_market, stock_code):
    stock_code = change_abnormal_stock(stock_code)

    if stock_market in basicConfig.us:
        stock_market = "us"

    url = "http://www.futunn.com/trade/search?k=%s" % stock_code.lower()
    response_data = basicRequest.request_get(url)

    if response_data["code"] == basicConfig.ResponseError.get("code"):
        result = response_data
    else:
        security_id_data = response_data.get("data")
        try:
            security_id = security_id_data[0].get("security_id")
            for i in range(len(security_id_data)):
                if security_id_data[i].get("code_name") == stock_code and \
                                security_id_data[i].get("security_label") == stock_market:
                    security_id = security_id_data[i].get("security_id")
            result = {
                "code": security_id
            }
        except:
            result = basicConfig.NotFound
    return result


# 个股详情数据: 今开,昨收,最高,最低等
def futu_basic(stock_market, stock_code):
    stock_code = change_abnormal_stock(stock_code)

    date = str(time.time()).replace(".", "0")

    response_data = get_security_id(stock_market, stock_code)
    if util.check_error_code(response_data["code"]):
        result = response_data
    else:
        url = "http://www.futunn.com/trade/quote-basic?security_id=%s&_=%s" % (
            response_data.get("code"), date)
        result = basicRequest.request_get(url)
    return result


if __name__ == '__main__':
    print futu_basic("hk", "00376")



