from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.get("https://www.youtube.com/watch?v=xQqsvRHjas4&ab_channel=MorningBrewDaily")
expand = driver.find_element(By.ID,"expand")
expand.click()
title = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='title']/h1[@class='style-scope ytd-watch-metadata']/yt-formatted-string[@class='style-scope ytd-watch-metadata']/span[@class='style-scope yt-formatted-string']")
# transcript_button = driver.find_element(By.CSS_SELECTOR,"[aria-label='Show transcript']")
transcript_button = driver.find_element(By.XPATH,"/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']/div[@id='description-inner']/ytd-text-inline-expander[@id='description-inline-expander']/div[@class='style-scope ytd-watch-metadata']/ytd-structured-description-content-renderer[@id='structured-description']/div[@id='items']/ytd-video-description-transcript-section-renderer[@class='style-scope ytd-structured-description-content-renderer']/div[@id='button-container']/div[@id='primary-button']/ytd-button-renderer[@class='style-scope ytd-video-description-transcript-section-renderer']/yt-button-shape/button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--outline yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m']/yt-touch-feedback-shape/div[@class='yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response']/div[@class='yt-spec-touch-feedback-shape__fill']")
transcript_button.click()
# element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.TAG_NAME, "ytd-menu-service-item-renderer")))
print(expand.text)
text = driver.find_element(By.XPATH,"/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='secondary']/div[@id='secondary-inner']/div[@id='panels']/ytd-engagement-panel-section-list-renderer[@class='style-scope ytd-watch-flexy'][6]/div[@id='content']/ytd-transcript-renderer[@class='style-scope ytd-engagement-panel-section-list-renderer']/div[@id='content']/ytd-transcript-search-panel-renderer[@class='style-scope ytd-transcript-renderer']/div[@id='body']/ytd-transcript-segment-list-renderer[@class='style-scope ytd-transcript-search-panel-renderer']")
print(text.text)
meta = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']")
channel = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='top-row']/div[@id='owner']/ytd-video-owner-renderer[@class='style-scope ytd-watch-metadata']/div[@id='upload-info']/ytd-channel-name[@id='channel-name']/div[@id='container']/div[@id='text-container']/yt-formatted-string[@id='text']/a[@class='yt-simple-endpoint style-scope yt-formatted-string']")
print(title.text)
print(meta.text)
# print(expand.tag_name)
views = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']/div[@id='description-inner']/ytd-watch-info-text[@id='ytd-watch-info-text']/div[@id='info-container']/yt-formatted-string[@id='info']/span[@class='style-scope yt-formatted-string bold']")
date = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']/div[@id='description-inner']/ytd-watch-info-text[@id='ytd-watch-info-text']/div[@id='info-container']/yt-formatted-string[@id='info']/span[@class='style-scope yt-formatted-string bold'][3]")
video = {
    "title": title.text,
    "meta": meta.text,
    "views": views.text,
    "date": date.text,
    "creator": channel.text,
    "transcript": text.text
}

with open("youtube.json", 'w') as f:
    json.dump(video, f)




driver.quit()
# spider = webdriver.Chrome()
