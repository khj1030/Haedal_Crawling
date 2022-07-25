from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


# Chrome Driver USB Error -----------------------------------------------------------------
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options) # webdriver을 통해 Chrome 웹 드라이버 객체 만들기
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

browser.implicitly_wait(5) # 웹 페이지가 로딩될 때까지 5초 기다리기
browser.get("https://www.coupang.com/") # Chrome 웹 드라이버 객체에게 get을 통하여 해당 url의 HTTP 요청
# browser.maximize_window()
time.sleep(3)
# --------------------------------------------------------------------------------------------

search = browser.find_element(By.ID, 'headerSearchKeyword')
search.send_keys('마스크')
browser.find_element(By.ID, 'headerSearchBtn').click()
time.sleep(3) # 추가!!

browser.find_element(By.XPATH, '//div[@id="searchSortingOrder"]/ul/li[4]/label').click()
time.sleep(3) # 추가!!

products_top10=[]
for i in range(1,11):
  product_name = browser.find_element(By.XPATH,'//ul[@class="search-product-list"]/li['+str(i)+']//dd[@class="descriptions"]//div[@class="name"]')  
  product_price = browser.find_element(By.XPATH,'//ul[@class="search-product-list"]/li['+str(i)+']//em/strong[@class="price-value"]')
  product_rating = browser.find_element(By.XPATH,'//ul[@class="search-product-list"]/li['+str(i)+']//div[@class="rating-star"]/span[@class="star"]/em[@class="rating"]') 
  product_rating_cnt = browser.find_element(By.XPATH,'//ul[@class="search-product-list"]/li['+str(i)+']//div[@class="rating-star"]/span[@class="rating-total-count"]') 
  dict ={}
  dict['상품명'] = product_name.text
  dict['가격'] = product_price.text
  dict['평점'] = product_rating.text
  dict['리뷰 수'] = product_rating_cnt.text
  products_top10.append(dict)

print(DataFrame(products_top10))

# -----------------------------------------------------------------------------

products_top10=[]
products_name = browser.find_elements(By.CSS_SELECTOR,'dd.descriptions > div.descriptions-inner > div.name')
products_price = browser.find_elements(By.CSS_SELECTOR,'em.sale > strong.price-value')
products_rating = browser.find_elements(By.CSS_SELECTOR,'div.rating-star > span.star > em.rating')
products_rating_cnt = browser.find_elements(By.CSS_SELECTOR,'div.rating-star > span.rating-total-count')

for i in range(0,10):
  dict ={}
  dict['상품명'] = products_name[i].text
  dict['가격'] = products_price[i].text
  dict['평점'] = products_rating[i].text
  dict['리뷰 수'] = products_rating_cnt[i].text
  products_top10.append(dict)

# print(DataFrame(products_top10))

browser.find_element(By.XPATH, '//ul[@class="search-product-list"]/li[1]').click()
browser.switch_to.window(browser.window_handles[-1])
time.sleep(3) 

# browser.find_element(By.XPATH, '//div[@class="tab"]/ul[@class="tab-titles"]/li[2]').click()
# time.sleep(3) 


# reviews=[]
# for i in range(1,6):
#   browser.find_element(By.XPATH, '//div[@class="sdp-review__article__page js_reviewArticlePagingContainer"]/button['+str(i+1)+']').click()
#   time.sleep(3) 

#   for j in range(1,6):
#     review_user = browser.find_element(By.XPATH, '//section[@class="js_reviewArticleListContainer"]/article['+str(j)+']//div[@class="sdp-review__article__list__info__user"]/span[@class="sdp-review__article__list__info__user__name js_reviewUserProfileImage"]')
#     review_content = browser.find_element(By.XPATH, '//section[@class="js_reviewArticleListContainer"]/article['+str(j)+']//div[@class="sdp-review__article__list__review js_reviewArticleContentContainer"]/div[@class="sdp-review__article__list__review__content js_reviewArticleContent"]')

#     dict ={}  
#     dict['유저'] = review_user.text
#     dict['내용'] = review_content.text
#     reviews.append(dict)

# print(DataFrame(reviews))
