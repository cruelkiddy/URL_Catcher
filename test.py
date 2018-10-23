from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
f = open('2016_2.txt','w')
pre = 'http://www.cninfo.com.cn/'
r_url = "http://www.cninfo.com.cn/cninfo-new/index"
driver=webdriver.Firefox(executable_path="C:\\Users\\84368\\PycharmProjects\\Get_urls\\geckodriver.exe")
driver.get(r_url)
direct = driver.find_element_by_xpath('//*[@id="common_top_input_obj"]')
direct.send_keys('投资者关系活动')
confirm = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/a')
confirm.click()
time.sleep(2)
#Part one finished
time.sleep(20)
while True:
    for counter in range(1,11):
        show = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li['+str(counter)+']/div[1]/a')
        f.write(str(show.get_attribute('href'))+'\n')
    current = driver.find_element_by_class_name('current')
    print('Page '+current.text)
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/div[5]/a[5]').click()
    WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[1]/div[1]/a"))



