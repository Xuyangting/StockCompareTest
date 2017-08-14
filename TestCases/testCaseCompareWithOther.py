# -*- coding:utf-8 -*-
import Queue
import datetime

from Util import util
from Config import basicConfig
from ParserResponses import youyu, sina, futu


def test_compare_other(env, stock_market, stock_code, stock_type, queue, log_file):
    youyu_result = youyu.parser_yff_basic(env, stock_market, stock_code, stock_type)
    sina_result = sina.parser_sina_basic(stock_market, stock_code)
    futu_result = futu.parser_futu_basic(stock_market, stock_code)
    util.add_message_file(log_file,
                          "[%s]Market: %s Code: %s Response:%s" % (util.get_time(datetime.datetime.now()), stock_market, stock_code, str(youyu_result)))
    data = []
    fail_item = []
    for item in basicConfig.compare_other_data:
        youyu_num = str(youyu_result[item])
        sina_num = str(sina_result[item])
        futu_num = str(futu_result[item])

        if util.check_error_code(sina_num) and util.check_error_code(futu_num):
            data.append([
                item,
                youyu_num,
                sina_num,
                futu_num,
                basicConfig.test_skip
            ])
        elif sina_num == "None" and util.check_error_code(futu_num):
            data.append([
                item,
                youyu_num,
                sina_num,
                futu_num,
                basicConfig.test_skip
            ])
        else:
            # ------------------------ 异常数据处理 ------------------------
            # 处理 --
            if youyu_result[item] == "--":
                sina_num = "--"
                futu_num = "--"
            # 处理不带单位的情况下,保留位数不一致,统一向有鱼股票看齐
            if util.check_not_contain_chinese(youyu_num):
                sina_num = util.decimal_format(youyu_num, sina_num)
                futu_num = util.decimal_format(youyu_num, futu_num)
            # --------------------------- 结束 ----------------------------
            if youyu_num == sina_num or youyu_num == futu_num:
                data.append([
                    item,
                    youyu_num,
                    sina_num,
                    futu_num,
                    basicConfig.test_pass
                ])
            else:
                fail_item.append(item)
                data.append([
                    item,
                    youyu_num,
                    sina_num,
                    futu_num,
                    basicConfig.test_fail
                ])
    queue.put(
        {
            "stock_market": stock_market,
            "stock_code": stock_code,
            "stock_type": stock_type,
            "result": util.test_result(data),
            "fail_item": fail_item,
            "data": data
        }
    )
    return data


if __name__ == '__main__':
    q = Queue.Queue()
    print test_compare_other("qa", "hk", "00376", "010104", q, "")






