# -*- coding:utf-8 -*-
from RequestsURL import sina
from Config import basicConfig
from Util import util


# 异常数据返回为空检测
def analysis_response(result):
    try:
        if len(result) < 30:
            return "1"
        else:
            return result.split("\"")[1].split(",")
    except Exception, e:
        print e


# 个股详情数据
def parser_sina_basic(stock_market, stock_code):
    response = sina.sina_basic(stock_market, stock_code)

    data = {}
    # 美股没有成交额, 默认都设置为0.00,以便测试过程中跳过
    for key in basicConfig.compare_other_data:
        data.setdefault(key, "0.00")

    compare_data = basicConfig.compare_other_data
    compare_data_us = basicConfig.compare_other_data_us

    if response == basicConfig.ResponseError.get("code"):
        for item in compare_data:
            data[item] = basicConfig.ResponseError.get("code")
    else:
        try:
            result = analysis_response(response)
            # 港股、美股、沪深 数据区分下标
            hs_index = [1, 2, 4, 5, 8, 9, 3]
            hk_index = [2, 3, 4, 5, 12, 11, 6]
            us_index = [5, 26, 6, 7, 10, 1]

            if stock_market in basicConfig.us:
                for i in range(len(compare_data_us)):
                    data[compare_data_us[i]] = result[us_index[i]]
            elif stock_market in basicConfig.hk:
                for i in range(len(compare_data)):
                    data[compare_data[i]] = result[hk_index[i]]
            else:
                for i in range(len(compare_data)):
                    data[compare_data[i]] = result[hs_index[i]]
        except:
            for item in compare_data:
                data[item] = basicConfig.ParserError.get("data")
    return data

if __name__ == '__main__':
    util.view_json(parser_sina_basic("ny", "BABA"))






