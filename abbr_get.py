import csv
import requests
from bs4 import BeautifulSoup

with open('sample_data_test.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    count = 0
    country_list = {}
    abbr_data_list = {}
    full_name_url = requests.get("https://abbreviations.yourdictionary.com/articles/country-abbreviations.html")
    soup = BeautifulSoup(full_name_url.content, 'html.parser')
    section = soup.find('div', id='article_body')
    abbr_text = section.find_next('ul').find_all('li')
    for abbr_data in abbr_text:
        abbr_data_list[abbr_data.text[0:3].strip()] = abbr_data.text[4:].strip()
    for csv_country in data:
        if csv_country['Country'] in abbr_data_list and csv_country['Country'] not in country_list:
            # print(abbr_data_list[csv_country['Country']])
            country_list[csv_country['Country']] = abbr_data_list[csv_country['Country']]

for country_name, full_name in country_list.items():
    print(f"Country Name In Excel Is = {country_name} Full Name Is = {full_name}")
