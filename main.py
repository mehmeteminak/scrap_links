from selenium import webdriver
from web_scraper import WebScraper
from url_selector import UrlSelector
from langchain_ollama.llms import OllamaLLM
from fastapi import FastAPI , HTTPException
from model.api_response import ApiResponse
import json


app = FastAPI()

@app.get("/search/{search_text}")
async def search(search_text: str) -> ApiResponse:
    url = find_movie_url(search_text)
    if url is None:
        raise HTTPException(404,'Url not found')
    
    return ApiResponse(production_url=url,search_text=search_text,source_website='fullhdfilmizlesene.de')
    
    

def find_movie_url(search_text):

    driver = webdriver.Safari()
    scraper = WebScraper(driver)


    urls = scraper.scrape_movie_urls(url='https://www.fullhdfilmizlesene.de',search_text=search_text)

    if urls:
        model = OllamaLLM(model='llama3.2')
        url_selector = UrlSelector(model=model)
        selected_url = url_selector.select_best_url(urls, search_text)
        return selected_url
    else:
        return None
