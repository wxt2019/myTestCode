# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el1.send_keys("2514814691")
el2 = driver.find_element_by_accessibility_id("密码 安全")
el2.send_keys("2514814691s")
el3 = driver.find_element_by_accessibility_id("登录")
el3.click()

driver.quit()