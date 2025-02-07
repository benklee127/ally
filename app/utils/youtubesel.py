from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
import re

def youtubescrape (url):

    if 'watch?' in url :

        driver = webdriver.Chrome()
        driver.implicitly_wait(6)


        driver.get(url)
        expand = driver.find_element(By.ID,"expand")
        expand.click()

        title = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager watch-root-element hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='title']/h1[@class='style-scope ytd-watch-metadata']/yt-formatted-string[@class='style-scope ytd-watch-metadata']")
        print(title)
        # transcript_button = driver.find_element(By.CSS_SELECTOR,"[aria-label='Show transcript']")
        transcript_button = driver.find_element(By.XPATH,"/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager watch-root-element hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']/div[@id='description-inner']/ytd-text-inline-expander[@id='description-inline-expander']/div[@class='style-scope ytd-watch-metadata']/ytd-structured-description-content-renderer[@id='structured-description']/div[@id='items']/ytd-video-description-transcript-section-renderer[@class='style-scope ytd-structured-description-content-renderer']/div[@id='button-container']/div[@id='primary-button']/ytd-button-renderer[@class='style-scope ytd-video-description-transcript-section-renderer']/yt-button-shape/button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--outline yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m']/yt-touch-feedback-shape/div[@class='yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response']/div[@class='yt-spec-touch-feedback-shape__fill']")
        transcript_button.click()
        print(transcript_button)
        print("clicked transcript")
        # element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.TAG_NAME, "ytd-menu-service-item-renderer")))
        print(expand.text)
        # text = driver.find_element(By.XPATH,"/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager watch-root-element hide-skeleton']/div[@id='columns']/div[@id='secondary']/div[@id='secondary-inner']/div[@id='panels']/ytd-engagement-panel-section-list-renderer[@class='style-scope ytd-watch-flexy'][7]/div[@id='content']/ytd-transcript-renderer[@class='style-scope ytd-engagement-panel-section-list-renderer']/div[@id='content']/ytd-transcript-search-panel-renderer[@class='style-scope ytd-transcript-renderer']/div[@id='body']/ytd-transcript-segment-list-renderer[@class='style-scope ytd-transcript-search-panel-renderer']")
        # print(text.text)
        segments = driver.find_element(By.ID, "segments-container")
        segmentArray = segments.text.splitlines()
        # print(segmentArray)


        timeArr = []
        captionArr = []
        section = ""
        for item in segmentArray :
            if re.search('^(?:\d+(?::[0-5][0-9]:[0-5][0-9])?|[0-5]?[0-9]:[0-5][0-9])$', item):
                timeArr.append(item)
                captionArr.append(section)
                section = ""
            else:
                section = section + item

        captionArr.append(section)    

        print(len(timeArr))
        print(len(captionArr))

        if len(captionArr) > len(timeArr) : 
            captionArr.pop(0)

        # print(len(timeArr))
        # print(len(captionArr))

        # print(captionArr)
        # print(timeArr)
        # # content = {'captions':captionArr, 'timestamps': timeArr }
        # print(content)
        # meta = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']")
        meta = driver.find_element(By.CLASS_NAME,"ytd-watch-info-text" )
        # print(mesta.text)
        metadata = meta.text.split("views")
        views = metadata[0].strip()
        date = metadata[1].strip()
        print(views, date)
        channel = driver.find_element(By.CLASS_NAME, "ytd-channel-name")
        print(title.text)
        print(channel.text)
        # print(expand.tag_name)
        # views = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']/div[@id='description-inner']/ytd-watch-info-text[@id='ytd-watch-info-text']/div[@id='info-container']/yt-formatted-string[@id='info']/span[@class='style-scope yt-formatted-string bold']")
        # date = driver.find_element(By.XPATH, "/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='below']/ytd-watch-metadata[@class='watch-active-metadata style-scope ytd-watch-flexy style-scope ytd-watch-flexy']/div[@id='above-the-fold']/div[@id='bottom-row']/div[@id='description']/div[@id='description-inner']/ytd-watch-info-text[@id='ytd-watch-info-text']/div[@id='info-container']/yt-formatted-string[@id='info']/span[@class='style-scope yt-formatted-string bold'][3]")
        video = {
            "title": title.text,
            # "meta": meta.text,
            "views": views,
            "date": date,
            "creator": channel.text,
            "captions": captionArr,
            "timestamps": timeArr,

        }

        with open(f"./temp/youtube/{title.text}", 'w') as f:
            json.dump(video, f)

        driver.quit()
        return video
    
    else :
        return "Bad Youtube URL"
    



# youtubescrape('https://www.youtube.com/watch?v=LVI8veUnSLQ')
    # spider = webdriver.Chrome()
