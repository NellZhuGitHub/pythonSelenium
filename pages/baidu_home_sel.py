import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select        # select元素操作类

dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(dir)
chrome_driver_path = dir + '/tools/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://www.baidu.com")

# 找到元素
ele = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
# # 1、鼠标悬浮操作，实例化
ActionChains(driver).move_to_element(ele).pause(0.5).click(ele).perform()
# ele.click()

'''
# 下拉列表:非select元素
loc = (By.XPATH, '//a[text()="高级搜索"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 下拉列表:select元素  Select类
select_loc = (By.XPATH, '//*[@id="adv-setting-ft"]/div/div[1]/span')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(select_loc))
ele = driver.find_element(*select_loc)
'''
# Select(driver.find_element(*select_loc)).select_by_index(3)  # 从0开始
# time.sleep(3)
s = Select(ele)  # 实例化对象

# 三种方式选择下拉属性：
# 下标方式选元素，从0开始　　　　
s.select_by_index(3)
# s.deselect_by_index()     # 不选中
time.sleep(3)

# value属性选元素
s.select_by_value("all")
# s.deselect_by_value()     # 不选中
time.sleep(3)

# 文本内容选元素：下拉框文本值内容
s.select_by_visible_text("微软 Powerpoint (.ppt)")
# s.deselect_by_visible_text("下拉框文本内容")     # 不选中