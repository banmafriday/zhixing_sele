# coding:utf-8
import unittest
import time
from sele.common.HTMLTestRunner_yo import HTMLTestRunner

discover1 = unittest.defaultTestLoader.discover("E:\\daima\\sele\\case",
                                               "test*.py")

nowtime = time.strftime("%Y_%m_%d_%H_%M")
reportpath = "E:\\daima\\sele\\case"+"report%s.html" % nowtime
fp = open(reportpath, "wb")
runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title="测试报告",
                        description="报告内容如下",
                        retry=1)
runner.run(discover1)