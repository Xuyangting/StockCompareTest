# -*- coding:utf-8 -*-
from RequestsURL import tencent
from Config import basicConfig
from Util import util


# 解析-个股财务
def parser_tencent_financial(stock_market, stock_code):
    response = tencent.tencent_financial(stock_market, stock_code)
    data = {}
    for key in basicConfig.finance_hk:
        data.setdefault(key, "0.00")
    compare_data = basicConfig.finance_hk
    if util.check_error_code(response.get("code")):
        for item in compare_data:
            data[item] = basicConfig.ResponseError.get("code")
    else:
        try:
            temp = response.get("data")
            first = temp[0]
            second = temp[1]
            third = temp[2]
            data[u"流动资产"] = first[1][1][0]
            data[u"流动负债"] = first[2][1][0]
            data[u"总资产"] = first[3][1][0]
            data[u"总负债"] = first[4][1][0]
            data[u"营业额"] = second[1][1][0]
            data[u"经营活动现金流量"] = third[1][1][0]
            data[u"投资活动现金流量"] = third[2][1][0]
            data[u"融资活动现金流量"] = third[3][1][0]
        except:
            for item in compare_data:
                data[item] = basicConfig.ParserError.get("data")
    return data


# 解析-个股财务 -> 现金流量表
def parser_tencent_financial_money(stock_market, stock_code):
    response = tencent.tencent_financial_money(stock_market, stock_code)
    data = {}
    print data

if __name__ == '__main__':
    util.view_json(parser_tencent_financial("hk", "00700"))


