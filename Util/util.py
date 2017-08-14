# -*- coding:utf-8 -*-
import sys
import uuid
import json
from collections import Counter
from Config import basicConfig

reload(sys)
sys.setdefaultencoding('utf8')


# 检查返回的结果是否在错误码中
def check_error_code(code):
    code = str(code)
    if code in basicConfig.ResponseError["code"] \
        or code in basicConfig.ParserError["code"] \
            or code in basicConfig.NotFound["code"]:
        return True
    else:
        return False


# 获取http请求request id,方便后台查找
def get_request_id():
    return "AT-" + str(uuid.uuid1()).replace("-", "")


# 显示时间: 2016-11-12 12:02:34
def get_time(now):
    return now.strftime("%Y-%m-%d %H:%M:%S")


# 显示时间: 20161112120234
def get_log_time(now):
    return now.strftime("%Y%m%d%H%M%S")


# 清空文件内容
def clear_file(file_path):
    f = open(file_path, "w")
    f.close()


# 追加内容
def add_message_file(file_path, message):
    f = open(file_path, "a")
    f.write(message + "\n")
    f.close()


# Json数据格式化输出，方便查看数据
def view_json(content):
    print json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=1)


# 测试结果
def test_result(data):
    message = []
    for item in data:
        message.append(item[len(item)-1])
    if basicConfig.test_fail in message:
        return basicConfig.test_fail
    elif basicConfig.test_skip in message:
        return basicConfig.test_skip
    else:
        return basicConfig.test_pass


# 测试结果统计
def test_result_num(data, check_type):
    pass_num = 0
    skip_num = 0
    fail_num = 0
    for item in data:
        if item.get("result") == basicConfig.test_pass:
            pass_num += 1
        if item.get("result") == basicConfig.test_skip:
            skip_num += 1
        if item.get("result") == basicConfig.test_fail:
            fail_num += 1
    if check_type == basicConfig.test_skip:
        return skip_num
    elif check_type == basicConfig.test_fail:
        return fail_num
    else:
        return pass_num


# 判断一个字符串中是否含有中文字符
def check_not_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return False
    return True


# 将数据进行统一,向有鱼股票数据看齐
def decimal_format(start, end):
    length_start = len(start)
    length_end = len(end)
    try:
        if length_start >= length_end:
            result = end + "0" * (length_start - length_end)
        else:
            next_num = end[length_start: length_start+1]
            if int(next_num) >= 5:
                result = start[:length_start-1] + str(int(end[length_start-1: length_start]) + 1)
            else:
                result = start
    except:
        result = end
    return result


# 根据环境组装请求url
def pack_url(env, url):
    if env == basicConfig.env_qa:
        return basicConfig.env_qa_host + url
    elif env == basicConfig.env_stage:
        return basicConfig.env_stage_host + url
    else:
        return basicConfig.env_live_host + url


# 获取列表中重复数据的个数
def get_reply_num(test_list):
    temp = Counter(test_list)
    return temp.most_common()

if __name__ == '__main__':
    print get_reply_num([2, 3, 2])



