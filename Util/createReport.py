# -*- coding:utf-8 -*-
import os
import sys
import datetime
from Util import util
from Config import basicConfig

reload(sys)
sys.setdefaultencoding('utf-8')


def choose_input_data(report_type, f, input_txt):
    if report_type == basicConfig.stage:
        for item in basicConfig.stage_item:
            f.write(input_txt % item)
    elif report_type == basicConfig.finance:
        for item in basicConfig.finance_item:
            f.write(input_txt % item)
    else:
        for item in basicConfig.other_item:
            f.write(input_txt % item)


# 测试报告统计
def statistic_test_result(f, test_data):
    f.write("<div class=\"my_data\">")
    f.write("<h2>%s</h2>" % test_data.get("title"))
    f.write("<table class=\"my_table\">")
    f.write("<tr>")
    f.write("<th>总计</th>")
    f.write("<th>通过</th>")
    f.write("<th>跳过</th>")
    f.write("<th>失败</th>")
    f.write("<th>耗时</th>")
    f.write("</tr>")
    f.write("<tr>")
    f.write("<td>%s</td>" % test_data.get("total"))
    f.write("<td>%s</td>" % test_data.get("pass"))
    f.write("<td>%s</td>" % test_data.get("skip"))
    f.write("<td>%s</td>" % test_data.get("fail"))
    f.write("<td>%s</td>" % test_data.get("time"))
    f.write("</tr>")
    f.write("</table>")
    f.write("</div>")


# 失败个数统计
def statistic_test_fail(f, test_data):
    f.write("<div class=\"my_data\">")
    f.write("<table class=\"my_table\">")
    f.write("<tr>")
    for item in test_data:
        f.write("<th>%s</th>" % item[0])
    f.write("</tr>")
    f.write("<tr>")
    for item in test_data:
        f.write("<td>%s</td>" % item[1])
    f.write("</tr>")
    f.write("</table>")
    f.write("</div>")


# 测试报告一级数据
def report_first_page(f, test_data, report_type):
    test_data = test_data.get("data")
    f.write("<div class=\"my_data\">")
    f.write("<table class=\"my_table\" id=\"my_table\">")
    f.write("<tr>")
    f.write("<th>股票市场</th>")
    f.write("<th>股票代码</th>")
    f.write("<th>股票类型</th>")
    f.write("<th>测试结果</th>")
    f.write("<th>相关操作</th>")
    f.write("</tr>")
    # 插入数据
    for i in xrange(0, len(test_data)):
        # 错误情况下显示红色字体
        if test_data[i].get("result") == basicConfig.test_pass:
            f.write("<tr>")
        else:
            f.write("<tr style=\"color:red\">")
        f.write("<td>%s</td>" % test_data[i].get("stock_market"))
        f.write("<td>%s</td>" % test_data[i].get("stock_code"))
        f.write("<td>%s</td>" % test_data[i].get("stock_type"))
        f.write("<td>%s</td>" % test_data[i].get("result"))
        # 错误信息查看
        if test_data[i].get("result") == basicConfig.test_pass:
            f.write("<td><button onclick=\"show_data_detail('%s')\">点击查看详情</button></td>") % test_data[i].get("stock_market") + test_data[i].get("stock_code")
        else:
            fail_txt = ""
            for info in test_data[i].get("data"):
                if str(info[len(info) - 1]) == basicConfig.test_fail:
                    if report_type == basicConfig.stage:
                        fail_txt += "------%s------<br/>[Stage]%s<br/>[Live]%s <br/>" % (str(info[0]), str(info[1]), str(info[2]))
                    elif report_type == basicConfig.finance:
                        fail_txt += u"------%s------<br/>[有鱼股票]%s<br/>[自选股]%s<br/>" % (str(info[0]), str(info[1]), str(info[2]))
                    else:
                        fail_txt += u"------%s------<br/>[有鱼股票]%s<br/>[新浪财经]%s<br/>[富途牛牛]%s <br/>" % (str(info[0]), str(info[1]), str(info[2]), str(info[3]))
            f.write("<td><button onclick=\"show_data_detail('" + test_data[i].get("stock_market") + test_data[i].get("stock_code") + "')\">点击查看详情</button>"
                    "<button onclick=\"openShutManager(this, 'p" + test_data[i].get("stock_market") + test_data[i].get("stock_code") + "', false, '关闭错误信息', '查看错误信息')\">查看错误信息</button>"
                    "<p id=\"p" + test_data[i].get("stock_market") + test_data[i].get("stock_code") + "\" style=\"display:none; color:red\">" + fail_txt + "</p></td>")
        f.write("</tr>")
    f.write("</table>")


# 测试报告二级数据z
def report_second_page(f, test_data, report_type):
    test_data = test_data.get("data")
    for i in xrange(0, len(test_data)):
        f.write("<table class=\"my_table_detail\" id=\"my_table_detail_" + test_data[i].get("stock_market") + test_data[i].get("stock_code") + "\">")
        f.write("<tr>")
        f.write("<th><button onclick=\"show_data('" + test_data[i].get("stock_market") + test_data[i].get("stock_code") + "')\">返回上一级</button></th>")
        choose_input_data(report_type, f, "<th>%s</th>")
        f.write("<th>Test Result</th>")
        f.write("</tr>")
        for item in test_data[i].get("data"):
            if str(item[len(item) - 1]) in [basicConfig.test_pass, basicConfig.test_skip]:
                f.write("<tr>")
            else:
                f.write("<tr style=\"color:red\">")
            if report_type == basicConfig.stage:
                for n in range(len(basicConfig.stage_item) + 2):
                    f.write("<td>%s</td>" % str(item[n]))
            elif report_type == basicConfig.finance:
                for n in range(len(basicConfig.finance_item) + 2):
                    f.write("<td>%s</td>" % str(item[n]))
            else:
                for n in range(len(basicConfig.other_item) + 2):
                    f.write("<td>%s</td>" % str(item[n]))
            f.write("</tr>")
        f.write("</table>")
    f.write("</div>")


def create(report_type, test_data, html_file, start_file):
    html_report = html_file
    if os.path.exists(html_report):
        os.remove(html_report)
    f = open(html_report, "a+")
    # 读取HTML头部信息
    f_start = open(start_file, "r")
    start = f_start.readlines()
    for start_item in start:
        f.write(start_item)
    f_start.close()
    f.write("<body>")
    # 测试报告统计
    statistic_test_result(f, test_data)
    # 失败个数统计
    statistic_test_fail(f, test_data.get("statistics"))
    # 测试报告一级数据
    report_first_page(f, test_data, report_type)
    # 测试报告二级数据
    report_second_page(f, test_data, report_type)
    f.write("</body></html>")
    print "[%s] Report Address = %s" % (util.get_time(datetime.datetime.now()), html_file)


if __name__ == '__main__':
    print os.path.dirname(os.getcwd())















