# coding:utf-8
import unittest
from selenium import webdriver
from sele.page.loginpage import LoginPage
from sele.page.editbug import JianLi
import sys

class TestNewBug(unittest.TestCase):
    u'''测试登录功能点'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage = LoginPage(cls.driver)
        cls.jianli = JianLi(cls.driver)

    def tearDown(self):
        self.loginpage.logout()

    def test_01(self):
        u'''测试登录:输入正确账号密码'''
        # 一.登录
        self.loginpage.login()

        # 1.1判断是否登录成功
        resu = self.loginpage.get_login_result()
        print("获取实际结果：%s" % resu)

        # 1.2期望结果
        xm = "伍善樟"

        # 1.3 断言：期望结果和实际结果对比
        self.assertEqual(resu, xm, msg="断言失败")
        self.assertTrue(resu == xm)

    def test_02(self):
        self.jianli.click_test_jl()
        self.jianli.click_bianji()
        self.jianli.input_qingchu()
        self.jianli.input_xing()
        self.jianli.click_shenri()
        self.jianli.click_nianfen()
        self.jianli.click_yuefen()
        self.jianli.click_reyue()
        self.jianli.click_xingbie()
        self.jianli.click_cs()
        self.jianli.click_hanz()
        self.jianli.youx()
        self.jianli.input_youxian()
        self.jianli.shenf()

    def test_03(self):
        '''判断'''
        # 1.判断姓名
        na = self.jianli.get_result_name()
        print("输入姓名：%s" % na, "成功")
        bm = "斑马"
        self.assertEqual(na, bm, msg="断言失败")

        # 2.判断生日,年
        sr = self.jianli.get_result_sri()
        print("输入年份：%s" % sr, "成功")
        sh = "2000"
        self.assertEqual(sr, sh, msg="断言失败")

        # 2.判断生日,月
        ye = self.jianli.get_result_yue()
        print("输入月份：%s" % ye, "成功")
        fen = "02"
        self.assertEqual(ye, fen, msg="断言失败")

        # # 2.判断性别,
        # xin = self.jianli.get_result_xbie()
        # print("输入：%s" % xin, "成功")
        # bie = "男"
        # self.assertEqual(xin, bie, msg="断言失败")

        # 2.判断杭州,
        hang = self.jianli.get_result_hzhou()
        print("选择城市：%s" % hang, "成功")
        zho = "杭州"
        self.assertEqual(hang, zho, msg="断言失败")

        # 2.判断邮箱,
        you = self.jianli.get_result_youxiang()
        print("输入邮箱：%s" % you, "成功")
        xian = "294350757@qq.com"
        self.assertEqual(you, xian, msg="断言失败")

        # # 2.判断身份,
        # sh = self.jianli.get_result_shenfeng()
        # print("输入：%s" % sh, "成功")
        # fen = "学生"
        # self.assertEqual(sh, fen, msg="断言失败")
        # self.jianli.clicl_baoc()
        # self.loginpage.logout()


if __name__ == "__main__":
    unittest.main()
