# proxy_scraper/tasks.py

from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Proxy

@shared_task
def scrape_proxy_list():
    url = 'https://geonode.com/free-proxy-list'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    proxy_table = soup.find('table', class_='proxy__t')
    for row in proxy_table.find_all('tr')[1:]:
        columns = row.find_all('td')
        ip = columns[0].text.strip()
        port = columns[1].text.strip()
        protocol = columns[4].text.strip()
        country = columns[2].text.strip()
        uptime = columns[7].text.strip()
        Proxy.objects.create(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime)
