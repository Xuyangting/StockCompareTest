# -*- coding:utf-8 -*-
from RequestsURL import futu
from Config import basicConfig
from Util import util


def parser_futu_basic(stock_market, stock_code):
    response = futu.futu_basic(stock_market, stock_code)
    data = {}
    compare_data = basicConfig.compare_other_data

    if util.check_error_code(response["code"]):
        for item in compare_data:
            data[item] = response["code"]
    else:
        try:
            temp_data = response.get("data").get("quote")
            temp_list = ["open_price", "last_price", "highest_price", "lowest_price", "volume", "turnover", "price"]
            for i in range(len(compare_data)):
                data[compare_data[i]] = temp_data.get(temp_list[i])
        except:
            for item in compare_data:
                data[item] = basicConfig.ParserError.get("data")
    return data


if __name__ == '__main__':
    util.view_json(parser_futu_basic("hk", "00376"))



