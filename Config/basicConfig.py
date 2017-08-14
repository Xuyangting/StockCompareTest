# -*- coding: utf-8 -*-

# ---------------------- 错误码 ----------------------
# 统一request请求, 响应异常, 返回response数据无,或无回应
ResponseError = {"code": "ResponseError"}
# 统一解析request异常
ParserError = {"code": "ParserError"}
# 统一第三方未查找到数据
NotFound = {"code": "NotFound"}

# --------------------- 测试环境 ---------------------
env_qa = "qa"
env_qa_host = "https://market-qa.youyu.cn"
env_stage = "stage"
env_stage_host = "https://market-stage.youyu.cn"
env_live = "live"
env_live_host = "https://sh-market.youyu.cn"
# --------------------- 测试报告 ---------------------
# 竞品对比测试报告
otherReport = "reportCompareWithOther.html"
# 与stage对比测试报告
stageReport = "reportCompareWithStage.html"
# 财务数据对比测试报告
financeReport = "reportCompareFinance.html"
other_item = [u"有鱼股票", u"新浪财经", u"富途牛牛"]
stage_item = [u"有鱼 Stage", u"有鱼 Live"]
finance_item = [u"有鱼股票", u"自选股"]
# ---------------------- 报告标题 --------------------
# 竞品对比测试报告标题
otherReportTitle = u"有鱼股票 VS （新浪财经 and 富途牛牛） 测试报告"
# 与stage对比测试报告标题
stageReportTitle = u"有鱼股票 Live VS Stage 测试报告"
# 财务数据对比报告
financeReportTitle = u"有鱼股票 VS 自选股 财务模块 测试报告"

# ---------------------- 基础码 ----------------------
# 线程数量
thread_num = 100

# 测试通过
test_pass = "Pass"
# 测试不通过
test_fail = "Fail"
# 异常情况跳过
test_skip = "Skip"

# 测试通过  -> 数目
pass_num = 0
# 测试不通过 -> 数目
fail_num = 0
# 测试不通过 -> 数目
skip_num = 0

# ---------------------- 对比项目 --------------------
# 竞品对比测试
other = "other"
# 与stage对比测试
stage = "stage"
# 财务数据对比
finance = "finance"
# ---------------------- 个股行情 --------------------
# 三大市场下子分类
hk = (
    "hk"
)
hs = (
    "sh",
    "sz"
)
us = (
    "am",
    "ar",
    "ix",
    "ny",
    "oq"
)

# -------------------- 个股基础数据 --------------------
# 市场竞品对比测试数据
compare_other_data = [
    u"今开",
    u"昨收",
    u"最高",
    u"最低",
    u"成交量",
    u"成交额",
    u"最新价"
]
# 美股没有成交额
compare_other_data_us = [
    u"今开",
    u"昨收",
    u"最高",
    u"最低",
    u"成交量",
    u"最新价"
]

# ---------------------- 个股财务数据 ----------------------
finance_hk = [
    # 财务比率
    # u"每股收益",
    # u"每股净资产",
    # u"资产负债率",
    # u"净资产收益率(ROE)",
    # u"资产回报率(ROA)",

    # 利润表
    u"营业额",
    # u"经营溢利",
    # u"税前溢利",
    # u"股东应占溢利",
    # u"股东应占溢利增长",
    # u"每股盈利",

    # 资产负债表
    u"流动资产",
    u"流动负债",
    u"总资产",
    u"总负债",
    # u"股东权益",

    # 现金流量表
    u"经营活动现金流量",
    u"投资活动现金流量",
    u"融资活动现金流量"
]

finance_hk_ratio = [
    u"每股收益",
    u"每股净资产",
    u"资产负债率",
    u"净资产收益率",
    u"资产回报率",
    u"流动比率",
    u"速动比率",
    u"存货周转率",
    u"经营利润率",
    u"税前利润率"
]

finance_hk_income = [
    u"营业额",
    u"营业额增长",
    u"营业支出",
    u"其他营业收入",
    u"经营溢利",
    u"税前溢利",
    u"股东应占溢利",
    u"股东应占溢利增长",
    u"少数股东权益",
    u"每股盈利",
    u"税项",
    u"税率"
]

finance_hk_balance = [
    u"流动资产",
    u"流动负债",
    u"总资产",
    u"总负债",
    u"股东权益",
    u"固定资产",
    u"现金及短期资金",
    u"存款",
    u"存货",
    u"短期债项",
    u"长期债项"
]

finance_hk_cash = [
    u"经营活动现金流量",
    u"投资活动现金流量",
    u"融资活动现金流量",
    u"年终现金及等价物",
    u"现金及等价物增加",
    u"新增贷款",
    u"偿还贷款"
]













