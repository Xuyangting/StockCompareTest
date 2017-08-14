# -*- coding:utf-8 -*-
import time
import sys
import os
import threading
import Queue
import datetime

from Config import basicConfig
from DealMySQL import dataCenter
from Util import createReport, util
from TestCases import testCaseCompareWithStage, testCaseCompareWithOther, testCaseCompareFinance

# ------------------ 全局变量 ------------------
HTML = "%s/Files/basicHTML.txt" % os.getcwd()
LOG = "%s/Logs/basicLOG_%s.txt" % (os.getcwd(), util.get_log_time(datetime.datetime.now()))


# ------------------- 多线程 -------------------
def test_by_thread(env, test_target, start_index, test_stocks):
    result = []
    threads = []
    # 获取每个子线程返回数据结果
    q = Queue.Queue()

    test_stocks_length = len(test_stocks)
    if start_index + basicConfig.thread_num > test_stocks_length:
        end_index = test_stocks_length
    else:
        end_index = start_index + basicConfig.thread_num

    for n in xrange(start_index, end_index):
        threads.append(threading.Thread(target=test_target, args=(
                    env,
                    test_stocks[n][0],
                    test_stocks[n][1],
                    test_stocks[n][2],
                    q,
                    LOG
                )
            )
        )

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    while not q.empty():
        result.append(q.get())

    print "[%s] Progress: %s/%s" % (util.get_time(datetime.datetime.now()), str(end_index), str(test_stocks_length))
    return result


# ------------------- 主函数 -------------------
def test(env, market, job, choose):
    # 初始化测试环境
    html_pass = []
    html_fail = []
    html_skip = []
    html = []
    start_time = time.clock()
    data_center = dataCenter.PullData()
    test_stocks = data_center.get_data(market)
    util.clear_file(LOG)
    test_start_index = 0
    # test_end_index = 1000
    test_end_index = len(test_stocks)

    # 执行测试
    print "[%s] Start Test Time" % util.get_time(datetime.datetime.now())
    for i in xrange(test_start_index, test_end_index, basicConfig.thread_num):
        if choose == basicConfig.stage:
            html += test_by_thread(env, testCaseCompareWithStage.test_with_stage, i, test_stocks)
        elif choose == basicConfig.finance:
            html += test_by_thread(env, testCaseCompareFinance.test_compare_finance, i, test_stocks)
        else:
            html += test_by_thread(env, testCaseCompareWithOther.test_compare_other, i, test_stocks)

    # 将测试结果进行划分, 划分为:1.测试通过 2.测试跳过 3.测试失败
    for item in html:
        if item["result"] == basicConfig.test_pass:
            html_pass.append(item)
        elif item["result"] == basicConfig.test_skip:
            html_skip.append(item)
        else:
            html_fail.append(item)

    # 统计测试失败的测试每个指数失败的数目
    fail_total_item = []
    for item in html_fail:
        fail_total_item += item.get("fail_item")
    fail_total_item_num = util.get_reply_num(fail_total_item)
    # 生成测试报告
    end_time = time.clock()
    print "[%s] Create Html Report" % util.get_time(datetime.datetime.now())
    if choose == basicConfig.stage:
        title = basicConfig.stageReportTitle
        html_file = basicConfig.stageReport
    elif choose == basicConfig.finance:
        title = basicConfig.financeReportTitle
        html_file = basicConfig.financeReport
    else:
        title = basicConfig.otherReportTitle
        html_file = basicConfig.otherReport

    html_data = {
        # 标题
        "title": title + u" 时间: " + util.get_time(datetime.datetime.now()),
        # 测试统计
        "total": str(test_end_index - test_start_index),
        "pass": str(util.test_result_num(html, "Pass")),
        "skip": str(util.test_result_num(html, "Skip")),
        "fail": str(util.test_result_num(html, "Fail")),
        "time": u"%.0f 秒" % (end_time - start_time),
        # 失败个数统计
        "statistics": fail_total_item_num,
        # 失败详情数据
        "data": html_fail
    }

    createReport.create(
        choose,
        html_data,
        "%s/TestReports/%s" % (os.getcwd(), html_file),
        HTML
    )

    # 将生成的html测试报告上传到MySQL
    print "[%s] Push Report To MySQL" % util.get_time(datetime.datetime.now())
    if job != "test":
        if choose == basicConfig.stage:
            data_center.push_report(
                "compare_execute",
                job,
                str(util.test_result_num(html, "Pass")) + "/" + str(len(test_stocks)),
                os.getcwd() + "/TestReports/reportCompareWithStage.html"
            )
        if choose == basicConfig.other:
            data_center.push_report(
                "compare_execute_myself",
                job,
                str(util.test_result_num(html, "Pass")) + "/" + str(len(test_stocks)),
                os.getcwd() + "/TestReports/reportCompareWithOther.html"
            )
    else:
        print "[%s] Not Need Commit to MySQL" % util.get_time(datetime.datetime.now())
    print "[%s] End Test Time" % util.get_time(datetime.datetime.now())

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print "----------------------------------------------"
        print "-- Please input 4 parameters --"
        print "-- Parameter 1: qa/stage/live"
        print "-- Parameter 2: us/hk/hs/test"
        print "-- Parameter 3: job id/test"
        print "-- Parameter 4: other/stage/finance"
        print "----------------------------------------------"
    else:
        # ------------------ 外部参数 ------------------
        # 测试环境
        # qa: 测试环境
        # stage: 预发布环境
        # live: 生产环境
        test_env = sys.argv[1]

        # 测试市场:
        # us: 美股
        # hk: 港股
        # hs: 沪深
        # test: 质量中心->对比测试->股票管理
        test_market = sys.argv[2]

        # 执行任务编号 -> 用户将生成的测试报告上传到质量中心
        test_job = sys.argv[3]

        # 执行测试类型->对应测试用例
        # other: 第三方
        # stage: stage
        test_type = sys.argv[4]

        test(test_env, test_market, test_job, test_type)

