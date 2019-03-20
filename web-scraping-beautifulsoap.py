import re
import string
from urllib.request import urlopen

import nltk
from bs4 import BeautifulSoup

ctrl_page = set()
url = 'https://www.letras.mus.br'


def get_links(band):
    '''
    Captura todos os links de uma banda, grupo ou artista a partir 
    da página www.letras.com.br/{banda}.
    args
    ----
        * band: banda, grupo ou artista que será capturado.
    '''
    try:
        html = urlopen(f"{url}/{band}")
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'href' in link.attrs:
                if link.attrs['href'] not in ctrl_page:
                    ctrl_page.add(f"{link.attrs['href']}")
                    get_music(link.attrs['href'])
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')


music = ' '


def get_music(new_page):
    '''
    Captura todas as músicas de uma banda, grupo ou artista a partir 
    da página www.letras.com.br/{banda}/{nome_da_música}.
    args
    ----
        * new_page: recebe a página capturada pela função get_links().
    '''
    global music
    try:
        html = urlopen(f"{url}/{new_page}")
        bs = BeautifulSoup(html, 'html.parser')
        for verse in bs.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            music += ' '.join(verse.stripped_strings)
            music += ' '
            print(music)
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')


if __name__ == "__main__":

    get_links('skank')

    stopwords = nltk.corpus.stopwords.words('portuguese')
    stopwords.append('gotta')
    list_word = []

    for m in music.split():
        m = ''.join(p for p in m if p not in string.punctuation)
        if len(m) >= 3:
            if m.lower() not in stopwords:
                list_word.append(
                    re.sub('[^çãááA-Za-z0-9+Á-Úá-ú]+', '', m.lower()))

    print(list_word[:10])
