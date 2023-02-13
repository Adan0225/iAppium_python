import unittest
from appium import webdriver
from appium.webdriver.webdriver import By #導入appium定位的方法包
from HTMLTestRunner import HTMLTestRunner

class AppiumTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_click_element(self):
        self.driver.find_element(By.ID,'digit_2').click()
        self.driver.find_element(By.ID,'digit_0').click()
        self.driver.find_element(By.ID,'digit_1').click()
        self.driver.find_element(By.ID,'digit_8').click()
        # element = self.driver.find_element_by_accessibility_id('Graphics')
        # element.click()
        # sub_element = self.driver.find_element_by_accessibility_id('Arc')
        # sub_element.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTest)
    with open("appium_test_report.html", "w") as f:
        runner = HTMLTestRunner(stream=f, title="Appium Test Report", description="Sample Appium Test")
        runner.run(suite)
