from bs4 import BeautifulSoup
import requests

def main(url: str):
    requests.get(url)