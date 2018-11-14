from sele.common.base import Base

class JianLi(Base):
    '''我的简历页面'''
    click_jianli = ("link text", "我的简历")  # 点击我的简历
    title = ("xpath", ".//*[@id='baseInfo']/div[2]/em")  # 点击编辑
    input_name = ("name", "name")     # 姓名输入框
    input_sri = ("name", "birthyear")  # 生日 年
    input_nian = ("xpath", "//div[@id='birthYearInput']//li[.='2000']")  # 点击2000年
    input_yue = ("name", "birthmonth")  # 点击月份后面的输入框
    click_yue = ("xpath", "//div[@id='birthMonthInput']//li[.='02']")  # 点击二月
    click_xbie = ("xpath", "//div[@id='sexInput']//div[.='男']")  # 点击姓别 男
    click_hang = ("id", "mrWokrCity")    # 点击所在城市
    click_hzhou = ("css selector", "li.mr_on")  # 点击杭州
    input_youxiang = ("id", "email")  # 联系邮箱
    click_shenfeng = ("xpath", "//div[@id='identityInput']//div[.='学生']")  # 当前身份
    click_shijian = ("css selector", "li.today")  # 点击工作时间
    click_sj = ("xpath", "//div[@id='workYearInput']//span[.='5月']")  # 选择月份
    click_baocun = ("css selector", "div.mr_save")  # 点击保存按钮
    xb = ("xpath", ".//*[@id='sexInput']/ul/li[1]/div")  # 性别
    seh = ("xpath",".//*[@id='identityInput']/ul/li[1]/div") # 身份

    def click_test_jl(self):
        '''点击我的简历'''
        self.click(self.click_jianli)

    def click_bianji(self):
        '''点击编辑按钮'''
        self.click(self.title)

    def input_qingchu(self):
        '''清空姓名输入框文本'''
        self.clear(self.input_name)

    def input_xing(self):
        '''输入姓名'''
        self.sendKeys(self.input_name, "斑马")
        # na = self.get_result_name()
        # n = "斑马"
        # print("获取实际结果： %s" % na)

    def click_shenri(self):
        '''点击生日按钮'''
        self.click(self.input_sri)

    def click_nianfen(self):
        '''点击2000年份'''
        self.click(self.input_nian)

    def click_yuefen(self):
        '''点击月份'''
        self.click(self.input_yue)

    def click_reyue(self):
        '''点击2月'''
        self.click(self.click_yue)

    def click_xingbie(self):
        '''性别，点击男'''
        self.click(self.click_xbie)

    def click_cs(self):
        '''点击所在城市'''
        self.click(self.click_hang)

    def click_hanz(self):
        '''点击杭州'''
        self.click(self.click_hzhou)

    def youx(self):
        '''清空邮箱输入框内容'''
        self.clear(self.input_youxiang)

    def input_youxian(self):
        '''输入邮箱'''
        self.sendKeys(self.input_youxiang, "294350757@qq.com")

    def shenf(self):
        '''当前身份，点击学生'''
        self.click(self.click_shenfeng)

    def click_shij(self):
        '''点击工作时间'''
        self.click(self.click_shijian)

    def click_yuef(self):
        '''选择月份'''
        self.click(self.click_sj)

    def clicl_baoc(self):
        '''点击保存'''
        self.click(self.click_baocun)

    def get_result_name(self):
        '''判断输入姓名是否成功'''
        try:
            a = self.findElement(self.input_name).get_attribute("value")
            return a
        except:
            return ""

    def get_result_sri(self):
        '''判断输入年份是否成功'''
        try:
            a = self.findElement(self.input_sri).get_attribute("value")
            return a
        except:
            return ""

    def get_result_yue(self):
        '''判断月份是否输入成功'''
        try:
            a = self.findElement(self.input_yue).get_attribute("value")
            return a
        except:
            return ""


    def get_result_xbie(self):
        '''判断输入姓别是否成功'''
        try:
            a = self.findElement(self.click_xbie).get_attribute("value")
            return a
        except:
            return ""


    def get_result_hzhou(self):
        '''判断输入姓名是否成功'''
        try:
            a = self.findElement(self.click_hang).get_attribute("value")
            return a
        except:
            return ""


    def get_result_youxiang(self):
        '''判断输入姓名是否成功'''
        try:
            a = self.findElement(self.input_youxiang).get_attribute("value")
            return a
        except:
            return ""

    def get_result_shenfeng(self):
        '''判断输入姓名是否成功'''
        try:
            a = self.findElement(self.click_shenfeng).get_attribute("value")
            return a
        except:
            return ""

    def get_jianli_title(self):
        '''获取返回结果'''
        try:
            t = self.findElement(self.title).text
            return t
        except:
            return ""

