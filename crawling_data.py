from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# webdriver을 통해 Chrome 웹 드라이버 객체 만들기
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# 웹 페이지가 로딩될 때까지 5초 기다리기
browser.implicitly_wait(5) 
browser.get("https://smartstore.naver.com/naturalfactory/products/4094549653?")

# 리뷰 페이지로 이동
browser.find_element(By.CSS_SELECTOR,'#content > div > div.z7cS6-TO7X > div._27jmWaPaKy > ul > li:nth-child(2) > a').click()

browser.implicitly_wait(5)  # 로딩이 끝날 때까지 5초까지는 기다려
# 최신 리뷰 페이지로 이동
browser.find_element(By.CSS_SELECTOR,'#REVIEW > div > div._2y6yIawL6t > div > div._1jXgNbFhaN > div.WiSiiSdHv3 > ul > li:nth-child(2) > a').click()

browser.implicitly_wait(5)  # 로딩이 끝날 때까지 5초까지는 기다려
c = browser.find_element(By.CSS_SELECTOR,'#REVIEW > div > div._2y6yIawL6t > div > div._1jXgNbFhaN > div.WiSiiSdHv3 > strong > span').text

print(c)


# Chrome 웹 드라이버 객체에게 get을 통하여 해당 url의 HTTP 요청
browser.get("https://smartstore.naver.com/naturalfactory/products/4094549653?")