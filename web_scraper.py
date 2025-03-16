from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebScraper:
    def __init__(self,driver):
        self.driver = driver

    def scrape_movie_urls(self, url,search_text):
        self.driver.get(url)
        search_box = self.driver.find_element(By.CLASS_NAME, "aratxt")
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)

        delay = 3 
        try:
            # = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'blok-baslik')))
            time.sleep(1)
            results = self.driver.find_elements(By.CLASS_NAME, "tt")
            movie_links = [r.get_attribute("href") for r in results if r.get_attribute("href")]
            self.driver.quit()
            if not movie_links:
                return None
            return movie_links
        except TimeoutException:
            return None
        
    def __del__(self):
        self.driver.quit()

