import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver):
  video_div_tag = 'ytd-video-renderer'
  video = driver.find_elements(By.TAG_NAME, video_div_tag)
  return video

def parse_videos(video):
  title_tag = video.find_element(By.ID,'video-title')
  title = title_tag.text
  
  url= title_tag.get_attribute('href')
  
  thumbnail_url = video.find_element(By.TAG_NAME,'img')
  thumbnail = thumbnail_url.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME,'ytd-channel-name')
  channel = channel_div.text

  description = video.find_element(By.ID,'description-text').text

  return {
    'Title:':title,
    'URL:':url,
    'Thumbnail:':thumbnail,
    'Channel:':channel,
    'Description:':description
  }
  


if __name__ == '__main__':
  print("Creating driver ")
  driver = get_driver()

  print("Fetching the Page")
  driver.get(YOUTUBE_TRENDING_URL)
  print('page title: ', driver.title)

  print("Get the trending videos")
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')

  print("Parsing the first twenty video")
  #title,url,thumbnail_url,channel,views,descriptions
  videos_data = [parse_videos(video) for video in videos[:20]]
  #print(videos_data)

  print("saving the data to a csv file")
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv',index=None)

  