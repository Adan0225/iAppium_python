from appium import webdriver
import unittest
from appiumframework.PO.creat_page import CreatPage
import time
import HTMLTestRunner


class Appium_test(unittest.TestCase):
    """appium测试类"""

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',  # 可有可無，這裡是指我的模擬器
            'platformVersion': '9.0',
            # apk包名
            'appPackage': 'com.smartisan.notes',
            # apk的launcherActivity
            'appActivity': 'com.smartisan.notes.NewNotesActivity',
            # 如果存在activity之间的切换可以用这个
            # 'appWaitActivity':'.MainActivity',
            'unicodeKeyboard': True,
            # 隐藏手机中的软键盘
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        self.verificationErrors = "今天天氣不錯在家學習！"  # 设置的断言

    def tearDown(self):
        time.sleep(10)
        assertt = self.driver.find_element_by_id("com.smartisan.notes:id/list_rtf_view").text
        print(assertt)   #调试用
        print('4235432')
        self.assertEqual(assertt, self.verificationErrors, msg="驗證失敗!")
        # 断言：实际结果，预期结果，错误信息
        self.driver.quit()

    def test_saveedittext(self):
        """保存编辑的文本"""
        sp = CreatPage(self.driver)
        sp.add_button_link()
        sp.run_case("今天天氣不錯在家學習!")
        # 断言：实际结果，预期结果，错误信息
        self.assertEqual(sp.get_finish_button_text(), self.verificationErrors, msg="验证失败！")

    # def test_creat(self):
    #     print('112233')
    #     """记事本中新增一条记录"""
    #     els = self.driver.find_element_by_id("com.smartisan.notes:id/new_note_button")
    #     self.assertIsNotNone(els)
    #     els.click()
    #     #self.driver.find_element(By.ID,"com.smartisan.notes:id/new_note_button").click()
    #     #self.driver.find_element_by_id("com.smartisan.notes:id/add_button").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_class_name("android.widget.EditText").send_keys("今天天氣不错在家學習！")
    #     self.driver.find_element_by_id("com.smartisan.notes:id/send_finish_button").click()


suite = unittest.TestSuite()
suite.addTest(Appium_test('test_saveedittext'))

report_file = ".\\appium_report.html"
fp = open(report_file, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="appium测试报告", description='新增一条笔记并保存')
runner.run(suite)
fp.close()

# class Test(unittest.TestCase):
#     """自動化"""
#     def setUp(self):
#
#         desired_caps = {
#             'platformName': 'Android',
#             'deviceName': '127.0.0.1:62001',#可有可無
#             'platformVersion': '7.1.2',
#             # apk包名
#             'appPackage': 'com.smartisan.notes',
#
#             #'appPackage': 'com.android.calculator2',
#             # apk的launcherActivity
#             'appActivity': 'com.smartisan.notes.NewNotesActivity',
#             #'appActivity' : '.Calculator',
#             #如果存在activity之間的切換可以用這個
#             # 'appWaitActivity':'.MainActivity',
#             'unicodeKeyboard': True,
#             #隐藏手機中的軟键盤
#             'resetKeyboard': True
#
#         }
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#         time.sleep(5)
#         self.verificationErrors = "今天天氣不錯在家學習！"

# def tearDown(self):
#     print('52356235623')
#     time.sleep(10)
#    # self.driver.find_element_by_id("com.smartisan.notes:id/android:id/button1").click()
#     self.driver.quit()
#
# def test_saveedittext(self):
#     """保存编辑的文本"""
#     sp = CreatPage(self.driver)
#     sp.add_button_link()
#     sp.run_case("123234")
#     #断言：实际结果，预期结果，错误信息
#     self.assertEqual(sp.get_finish_button_text(),self.verificationErrors,msg="验证失败！")
