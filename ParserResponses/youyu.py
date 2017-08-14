# -*- coding:utf-8 -*-
from RequestsURL import youyu
from Config import basicConfig
from Util import util


def parser_yff_basic(env, stock_market, stock_code, stock_type):
    yff = youyu.yff_basic(env, stock_market, stock_code, stock_type)
    data = {}
    for key in basicConfig.compare_other_data:
        data.setdefault(key, "0.00")
    compare_data = basicConfig.compare_other_data

    if util.check_error_code(yff.get("code")):
        for item in compare_data:
            data[item] = basicConfig.ResponseError.get("data")
    else:
        try:
            yff_result = yff.get("data").get("datagrid")
            for item in yff_result:
                data[item.get("k")] = item.get("v")

            yff_result_price = yff.get("data").get("price")
            check_list = [["1", u"最新价"], ["6", u"涨跌额"], ["7", u"涨跌率"]]
            for check in check_list:
                data[check[1]] = yff_result_price.get(check[0])

            check_list = [["3", u"今开"], ["2", u"昨收"], ["4", u"最高"], ["5", u"最低"]]
            yff_result_temp = yff.get("data")
            for check in check_list:
                data[check[1]] = yff_result_temp.get(check[0])
        except:
            for item in compare_data:
                data[item] = basicConfig.ParserError.get("data")
    return data


def parser_yff_finance(env, stock_market, stock_code):
    yff = youyu.yff_stock_finance(env, stock_market, stock_code)
    data = {}
    for key in basicConfig.finance_hk:
        data.setdefault(key, "0.00")
    compare_data = basicConfig.finance_hk
    if util.check_error_code(yff.get("code")):
        for item in compare_data:
            data[item] = basicConfig.ResponseError.get("data")
    else:
        try:
            yff_result = yff.get("data")
            for result in yff_result:
                result_data = result.get("data")
                for result_item in result_data:
                    data[result_item.get("title")] = result_item.get("value")
        except:
            for item in compare_data:
                data[item] = basicConfig.ParserError.get("data")
    return data


if __name__ == '__main__':
    util.view_json(parser_yff_finance("qa", "hk", "00700"))










