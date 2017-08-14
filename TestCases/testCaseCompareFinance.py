# -*- coding:utf-8 -*-
import Queue
import datetime

from Util import util
from Config import basicConfig
from ParserResponses import youyu, tencent


def test_compare_finance(env, stock_market, stock_code, stock_type, queue, log_file):
    youyu_result = youyu.parser_yff_finance(env, stock_market, stock_code)
    tencent_result = tencent.parser_tencent_financial(stock_market, stock_code)

    util.add_message_file(log_file,
                          "[%s]Market: %s Code: %s Response:%s" % (
                              util.get_time(datetime.datetime.now()),
                              stock_market,
                              stock_code,
                              str(youyu_result)
                          ))
    data = []

    for item in basicConfig.finance_hk:
        youyu_num = str(youyu_result[item])
        tencent_num = str(tencent_result[item])
        # ------------------------ 异常数据处理 ------------------------
        # 处理 自选股中带 ,
        if "," in tencent_num:
            tencent_num = tencent_num.replace(",", "")
        # --------------------------- 结束 ----------------------------
        if util.check_error_code(youyu_num) \
                or util.check_error_code(tencent_num) \
                or tencent_num == "0.00":
            data.append([
                item,
                youyu_num,
                tencent_num,
                basicConfig.test_skip
            ])
        else:
            if youyu_num == tencent_num or youyu_num in tencent_num:
                data.append([
                    item,
                    youyu_num,
                    tencent_num,
                    basicConfig.test_pass
                ])
            else:
                data.append([
                    item,
                    youyu_num,
                    tencent_num,
                    basicConfig.test_fail
                ])
    queue.put(
        {
            "stock_market": stock_market,
            "stock_code": stock_code,
            "stock_type": "",
            "result": util.test_result(data),
            "data": data
        }
    )
    return data


if __name__ == '__main__':
    q = Queue.Queue()
    print test_compare_finance("qa", "hk", "00376", q, "/Users/jenkins/Desktop/YouYuCompareStock/Logs/basicLOG_20170703180405.txt")






