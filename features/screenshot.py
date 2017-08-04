from selenium import webdriver
import time, sys


num = "1"

url = "http://fornax:8080/job/M4_PowerBI_BDD_Tests/"+sys.argv[1]+"/cucumber-html-reports/overview-features.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.find_element_by_xpath(".//*[@id='j_username']").send_keys("esrimaps")
driver.find_element_by_xpath("//*[contains(@type,'password')]").send_keys("esrimaps")
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='yui-gen1-button']").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.save_screenshot('cucumber_image.png')
time.sleep(1)
driver.quit()