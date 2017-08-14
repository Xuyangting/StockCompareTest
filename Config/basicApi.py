# -*- coding: utf-8 -*-

# ---------------------- 有鱼股票 ----------------------
# 基础数据,如: 今开,昨收,最高,最低等
basic = "/app/v2/quote/user/query/stockdetail"


def get_basic_payload(market_code, stock_code, stock_type):
    return {
        "marketcode": market_code,
        "stockcode": stock_code,
        "graph_tab_index": "0",
        "k_not_refresh": "0",
        "stock_type": stock_type
    }
# 财务1级数据
finance = "/app/v2/information/user/query/finance"


def get_finance_payload(market_code, stock_code):
    return {
        "marketcode": market_code,
        "stockcode": stock_code
    }

# 财务2级数据 -> 现金流量表, 资产负债表, 利润表, 财务比率
finance_second = "/app/v2/information/user/query/financedetail"
# 港股 - 新股日历
hk_new_stock_calendar = "/app/v2/quote/user/query/stockcalendarlist?marketid=hk&item=all"
# 公司简介
stock_company_introduce = "/app/v2/information/user/query/companyintro"
# ---------------------- 新浪财经 ----------------------


# ---------------------- 富图牛牛 ----------------------


# ----------------------- 自选股 -----------------------
basic_tc = "http://ifzq.gtimg.cn"
request_info = "&_appName=android" \
               "&_dev=HUAWEI+NXT-AL10" \
               "&_devId=5fe469c8bfef80504719b5bf4eedddebb17ea4cd" \
               "&_mid=5fe469c8bfef80504719b5bf4eedddebb17ea4cd" \
               "&_md5mid=E7FD5EDEC16084EEAF5729D7BDEE1318" \
               "&_omgid=" \
               "&_omgbizid=" \
               "&_appver=5.5.0" \
               "&_ifChId=96" \
               "&_screenW=1080" \
               "&_screenH=1812" \
               "&_osVer=7.0" \
               "&_uin=10000" \
               "&_wxuin=20000" \
               "&_net=WIFI" \
               "&__random_suffix=87888"


# 财务1级数据
def get_finance_tc(stock_market, stock_code):
    url = "/stock/corp/hkmoney/sumary?symbol=%s&type=sum" % (stock_market + stock_code)
    return basic_tc+url+request_info


# 财务2级数据 -> 现金流量表
def get_finance_tc_money(stock_market, stock_code):
    url = "/stock/corp/hkcwbb/detail?symbol=%s&type=xjll&rttype=all&_rndtime=1501142240" % (stock_market + stock_code)
    return basic_tc+url+request_info