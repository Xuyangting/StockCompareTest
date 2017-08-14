# -*- coding:utf-8 -*-
import MySQLdb


def basic_method(host, port, user, password, db, sql):
        conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset="utf8"
        )
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return result


def get_stock(table):
    return "SELECT market,raw_symbol,third_class FROM %s where is_visible=1;" % table


def get_single_stock(table, stock_code):
    return "SELECT market,raw_symbol,third_class FROM %s where is_visible=1 AND raw_symbol='%s';" % (table, stock_code)


class PullData:
    def __init__(self):
        self.qa_basic_host = "*:*:*:*"
        self.qa_basic_port = 7776
        self.qa_basic_user = "marketserverread"
        self.qa_basic_password = "marketserverread"
        self.qa_db_hk = "hkdb"
        self.qa_table_hk = "t_hk_secu_basic_info"
        self.qa_db_us = "usdb"
        self.qa_table_us = "t_us_secu_basic_info"
        self.qa_db_hs = "hushendb"
        self.qa_table_hs = "t_hushen_secu_basic_info"
        self.test_basic_host = "10.9.8.20"
        self.test_basic_port = 3306
        self.test_basic_user = "monitor"
        self.test_basic_password = "monitor123"
        self.test_db_app = "app"

    # 获取数据库中的stock market, stock code, stock type
    def get_data(self, market):
        if market == "hs":
            return basic_method(
                self.qa_basic_host,
                self.qa_basic_port,
                self.qa_basic_user,
                self.qa_basic_password,
                self.qa_db_hs,
                get_stock(self.qa_table_hs)
            )
        elif market == "hk":
            return basic_method(
                self.qa_basic_host,
                self.qa_basic_port,
                self.qa_basic_user,
                self.qa_basic_password,
                self.qa_db_hk,
                get_stock(self.qa_table_hk)
            )
        elif market == "us":
            return basic_method(
                self.qa_basic_host,
                self.qa_basic_port,
                self.qa_basic_user,
                self.qa_basic_password,
                self.qa_db_us,
                get_stock(self.qa_table_us)
            )
        else:   # 质量中心->自定义股票
            result = []
            test_stocks = basic_method(
                self.test_basic_host,
                self.test_basic_port,
                self.test_basic_user,
                self.test_basic_password,
                self.test_db_app,
                "select stock_code, stock_type from compare_stock"
            )
            for item in test_stocks:
                if item[1] == "hk":
                    temp = basic_method(
                            self.qa_basic_host,
                            self.qa_basic_port,
                            self.qa_basic_user,
                            self.qa_basic_password,
                            self.qa_db_hk,
                            get_single_stock(self.qa_table_hk, item[0])
                        )
                    if len(temp) > 0:
                        result.append(temp[0])
                elif item[1] == "hs":
                    temp = basic_method(
                        self.qa_basic_host,
                        self.qa_basic_port,
                        self.qa_basic_user,
                        self.qa_basic_password,
                        self.qa_db_hs,
                        get_single_stock(self.qa_table_hs, item[0])
                    )
                    if len(temp) > 0:
                        result.append(temp[0])
                else:
                    temp = basic_method(
                        self.qa_basic_host,
                        self.qa_basic_port,
                        self.qa_basic_user,
                        self.qa_basic_password,
                        self.qa_db_us,
                        get_single_stock(self.qa_table_us, item[0])
                    )
                    if len(temp) > 0:
                        result.append(temp[0])
            return result

    # 将测试报告上次到质量中心数据库中
    def push_report(self, choose, test_job_id, test_result, file_path):
        f = open(file_path, "r")
        html_data = f.readlines()
        f.close()
        html = ""
        for data in html_data:
            html += data
        basic_method(
            self.test_basic_host,
            self.test_basic_port,
            self.test_basic_user,
            self.test_basic_password,
            self.test_db_app,
            "update %s set result='%s',report='%s' where id=%s" % (
                choose,
                test_result,
                html.replace("'", "''"),
                test_job_id
            )
        )

if __name__ == '__main__':
    pull = PullData()
    print(pull.get_data("test"))













