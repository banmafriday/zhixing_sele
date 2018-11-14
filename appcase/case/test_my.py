import unittest
from appium import webdriver
import time
from appcase.common.base import BaseApp
from appcase.pages.mypage import MyPage
from appcase.pages.mypage import YaoQingHaoYou
from appcase.common.start import start_app
from appcase.common.logger import Log
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.yipiao",
                "noReset": True,
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }
class TestYaoQing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)
        cls.app = BaseApp(cls.driver)
        cls.app.click(MyPage.loc1)   # 点击我的
        cls.log = Log()

    def test_01(self):
        '''我的-邀请好友'''
        self.log.info("---开始测试：test_01:我的-邀请好友---")
        # self.app.click({"name": "我的", "by": "text", "value": "我的"})
        time.sleep(3)
        self.log.info("第一步：我的——邀请好友")
        self.app.click(MyPage.loc3)
        self.log.info("获取弹出框文本，用做断言")
        els = self.app.finds(YaoQingHaoYou.tanchu)
        result = []
        for i in els:
            t = i.text
            result.append(t)
        print("获取结果：%s" % result)

        self.log.info("点取消分享")
        self.app.click(YaoQingHaoYou.quxiao)

        self.log.info("断言")
        qiwang = ['微信', '朋友圈', 'QQ', 'QQ空间', '短信']
        self.assertEqual(result, qiwang)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()