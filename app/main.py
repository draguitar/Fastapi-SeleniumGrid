from typing import Union

from fastapi import FastAPI

from selenium import webdriver

import time

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World",
    "Amber": "!!!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/selenium/{item_id}")
def selenium(item_id: int):
    try:
        browser = webdriver.Remote(
        command_executor='http://xxx.xxx.xx.xx:14444/wd/hub',
        options=webdriver.ChromeOptions()
        )
        browser.get('https://www.google.com')
        browser.save_screenshot("./app/chrome.png")
        print(browser.title)


    except Exception as error:
        print(error)
    finally:
        time.sleep(30)
        browser.quit()


    return {"item_id": item_id}





