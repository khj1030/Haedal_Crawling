from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(5)
# browser.maximize_window() # 브라우저 화면 최대화
browser.get("https://smartstore.naver.com/naturalfactory/products/4094549653?")
browser.implicitly_wait(5)  # 로딩이 끝날 때까지 5초까지는 기다려

# 리뷰 페이지로 이동
browser.find_element(By.CSS_SELECTOR,'#content > div > div.z7cS6-TO7X > div._27jmWaPaKy > ul > li:nth-child(2) > a').click()
browser.implicitly_wait(5)  # 로딩이 끝날 때까지 5초까지는 기다려

# 최신 리뷰 페이지로 이동
browser.find_element(By.CSS_SELECTOR,'#REVIEW > div > div._2y6yIawL6t > div > div._1jXgNbFhaN > div.WiSiiSdHv3 > ul > li:nth-child(2) > a').click()
browser.implicitly_wait(5)  # 로딩이 끝날 때까지 5초까지는 기다려

c = browser.find_element(By.CSS_SELECTOR,'#REVIEW > div > div._2y6yIawL6t > div > div._1jXgNbFhaN > div.WiSiiSdHv3 > strong > span').text

print(c)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# browser=webdriver.Chrome()
# browser.get("https://www.naver.com/")
# WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.header")))



