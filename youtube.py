from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class YouTubeTester:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )

    def search_video(self, query):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "video-title"))
        )

    def play_first_video(self):
        first_video = self.driver.find_element(By.ID, "video-title")
        first_video.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "html5-video-player"))
        )

    def pause_video(self):
        video_player = self.driver.find_element(By.CLASS_NAME, "html5-video-player")
        video_player.send_keys("k")  # 'k' is the play/pause

    def close_browser(self):
        self.driver.quit()