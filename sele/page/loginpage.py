from sele.common.base import Base
import sys
loginurl = "https://www.lagou.com"

class LoginPage(Base):
    '''登录页面'''
    click_city = ("link text", "杭州站")  # 点击杭州站
    click_login_de = ("link text", "登录")   # 点击 登录
    user_loc = ("css selector", "input.input.input_white")  # 输入账号
    psw_loc = ("xpath", "//div[@class='form-content']/div[2]/form/div[2]/input")    # 输入密码
    sub_loc = ("xpath", "//div[@class='form-content']/div[2]/form/div[5]/input")    # 点登录
    zhanghao_loc = ("css selector", "li.user_dropdown")

    def open_login_page(self):
        self.driver.get(loginurl)

    def logout(self):
        '''登出'''
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()

    def click_hangzhou(self):
        '''点击杭州站'''
        self.click(self.click_city)

    def click_login_dl(self):
        '''点击登录'''
        self.click(self.click_login_de)

    def input_username(self,usrname):
        '''输入账号'''
        self.sendKeys(self.user_loc, usrname)

    def input_psw(self, psw):
        '''输入密码'''
        self.sendKeys(self.psw_loc, psw)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click(self.sub_loc)

    def login(self, username="16657128731", psw="13975943593"):
        '''登录流程:'''
        self.open_login_page()
        self.click_hangzhou()
        self.click_login_dl()
        self.input_username(username)
        self.input_psw(psw)
        self.click_login_button()

    def get_login_result(self):
        '''获取登录的结果'''
        try:
            t = self.findElement(self.zhanghao_loc).text
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""

    def is_alert(self):
        '''判断是否有弹窗，有的话点确定，没有的话就pass
        有缺陷：如果页面卡，出现alert慢就判断不到了
        '''
        try:
            alert = self.driver.switch_to_alert()  # 这一步不会报错
            print(alert.text)     # 这一步，没有获取到alert文本就报错了
            alert.accept()  # 点确定按钮
        except:
            pass

    def is_alert_exsits_base(self):
        try:
            alert = self.is_alert_exsit()
            alert.accept()
        except:
            pass
