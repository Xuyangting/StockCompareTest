# -*- coding:utf-8 -*-
import basicRequest

from Config import basicApi


# 个股财务
def tencent_financial(stock_market, stock_code):
    return basicRequest.request_get(basicApi.get_finance_tc(stock_market, stock_code))


# 个股财务 -> 现金流量
def tencent_financial_money(stock_market, stock_code):
    return basicRequest.request_get(basicApi.get_finance_tc_money(stock_market, stock_code))


if __name__ == '__main__':
    print tencent_financial_money("hk", "00700")
