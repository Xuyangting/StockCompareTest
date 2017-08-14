# -*- coding:utf-8 -*-
import requests

from Util import util
from Config import basicConfig, basicApi
from RequestsURL import basicRequest


# 个股详情数据: 今开,昨收,最高,最低等
def yff_basic(env, market_code, stock_code, stock_type):
    url = util.pack_url(env, basicApi.basic)
    payload = basicApi.get_basic_payload(market_code, stock_code, stock_type)
    return basicRequest.basic_request(url, payload)


# 个股财务1级
def yff_stock_finance(env, market_code, stock_code):
    url = util.pack_url(env, basicApi.finance)
    payload = basicApi.get_finance_payload(market_code, stock_code)
    return basicRequest.basic_request(url, payload)


# 个股财务2级 -> balance（资产负债表），cash（现金流量表），income（利润表）,ratio(财务比率)
def yff_stock_finance_money(env, market_code, stock_code, item):
    url = "%s?marketcode=%s&stockcode=%s&item=%s&date=0" % (util.pack_url(env, basicApi.finance_second), market_code, stock_code, item)
    return basicRequest.request_get(url)


# 新股日历
def yff_hk_new_stock_calendar(env):
    url = util.pack_url(env, basicApi.hk_new_stock_calendar)
    return basicRequest.request_get(url)


# 公司简介
def yff_stock_company_introduction(env, market_code, stock_code, stock_type):
    url = "%s?marketcode=%s&stockcode=%s&stock_type=%s" % (util.pack_url(env, basicApi.stock_company_introduce), market_code, stock_code, stock_type)
    return basicRequest.request_get(url)


if __name__ == '__main__':
    # util.view_json(yff_stock_finance_money("qa", "hk", "00700", "cash"))
    # util.view_json(yff_hk_new_stock_calendar("qa"))
    util.view_json(yff_stock_company_introduction("qa", "hk", "00700", "010104"))














