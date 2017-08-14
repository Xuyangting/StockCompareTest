# -*- coding:utf-8 -*-
import datetime

from ParserResponses import youyu
from Util import util
from Config import basicConfig


def test_with_stage(env, stock_market, stock_code, stock_type, queue, log_file):
    result = []
    stage_info = youyu.parser_yff_basic(basicConfig.env_stage, stock_market, stock_code, stock_type)
    live_info = youyu.parser_yff_basic(basicConfig.env_live, stock_market, stock_code, stock_type)
    util.add_message_file(log_file,
                          "[%s]Market: %s Code: %s Response:%s" % (util.get_time(datetime.datetime.now()), stock_market, stock_code, str(live_info)))
    for key in stage_info.keys():
        if stage_info.get(key) == live_info.get(key):
            result.append([key, stage_info.get(key), live_info.get(key), basicConfig.test_pass])
        else:
            result.append([key, stage_info.get(key), live_info.get(key), basicConfig.test_fail])

    queue.put(
        {
            "stock_market": stock_market,
            "stock_code": stock_code,
            "stock_type": stock_type,
            "result": util.test_result(result),
            "data": result
        }
    )
    return result












