import unittest
import HTMLTestRunner

#相對路徑
testcase_path = ".\\testcase"
report_path = ".\\report\\appium_report.html"
def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            print(test_case)
            print('5555')
            uit.addTest(test_case)
    return uit

suite = creat_suite()
fp = open(report_path,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="測試結果",description="appium新建筆記測試结果")
runner.run(suite)
fp.close()

