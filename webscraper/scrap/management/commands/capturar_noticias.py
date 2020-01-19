import requests
import pandas as pd
import json
import sqlite3
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Get news from a defined website'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        response = requests.get('https://www.tecmundo.com.br/')

        soup = BeautifulSoup(response.content, 'html.parser')

        data = {
            'Headlines': [],
            'News_content': []
        }

        headlines = soup.find_all('a', class_='tec--carousel__item__title__link')

        for headline in headlines:
            data['Headlines'].append(headline.get_text())
            
            content_url = headline.get('href')
            content_page = requests.get(content_url)
            
            soup = BeautifulSoup(content_page.content, 'html.parser')
            
            p_tags = soup.find_all('p')

            p_tags_text = [tag.get_text() for tag in p_tags]

            sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
            sentence_list = [sentence for sentence in sentence_list if '.' in sentence]

            article = ' '.join(sentence_list)
            data['News_content'].append(article)

        table = pd.DataFrame(data)
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE contents(Headlines, News_content)
        """)

        for row in table.itertuples():
            insert_table = """
            INSERT INTO contents(Headlines, News_content) \
            VALUES (?,?)
        """
            cursor.execute(insert_table, row[1:])

        conn.commit()
        conn.close()