from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# def get_url(url):
#     response = requests.get(url)
#     return response.text

# def bs4_object(response):
#     html = get_url(response)
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup

# def main():
#     pass

# if __name__ == "__main__":
#     url = r"https://cellphones.com.vn/mobile.html"
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = r"https://cellphones.com.vn/mobile.html"