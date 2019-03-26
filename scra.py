# _*_ coding:utf-8 _*_
# @author Robert Carlos                                 #
# email robert.carlos@linuxmail.org                     #
# 2019-Mar (CC BY 3.0 BR)                               # 

import string
import sys
from urllib.request import urlopen

import nltk
from bs4 import BeautifulSoup

url = 'https://www.letras.mus.br'
music = ' '


def get_links(band):
    '''
    Captura todos os links de uma banda, grupo ou artista a partir 
    da página www.letras.com.br/{banda}.
    args
    ----
        * band: banda, grupo ou artista que terá os links capturados.
    '''
    try:
        print('Obtendo links/músicas')
        ctrl_page = set()
        html = urlopen(f"{url}/{band}")
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'href' in link.attrs:
                if link.attrs['href'] not in ctrl_page:
                    ctrl_page.add(f"{link.attrs['href']}")
                    get_music(link.attrs['href'])
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')


def get_music(new_page):
    '''
    Captura todas as músicas de uma banda, grupo ou artista a partir 
    da página www.letras.com.br/[banda/nome_da_música].
    args
    ----
        * new_page: recebe os links capturados pela função get_links().
    '''
    global music
    try:
        html = urlopen(f"{url}/{new_page}")
        bs = BeautifulSoup(html, 'html.parser')
        for verse in bs.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            music += ' '.join(verse.stripped_strings)
            music += ' '
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')


def clean_write(preview=100):
    '''
    Adiciona à variável plain_text todas as palavras maiores que X letras 
    e que não estão na lista stopwords. Em seguida, grava todo o resultado em um 
    arquivo de texto.
    args
    ----
        * preview: total de caracteres que serão exibidos como "preview" 
        após a limpeza e gravação dos dados. Por padrão, 100 caracteres
        são exibidos.
    '''
    print('Finalizando...')
    stopwords = nltk.corpus.stopwords.words('portuguese')
    plain_text = ''
    for m in music.split():
        if len(m) >= 3:
            m = ''.join(p for p in m if p not in string.punctuation)
            if m.lower() not in stopwords:
                plain_text += m.lower()+' '
    try:
        print(plain_text, file=open('filename.txt', 'w'))
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar gravar o arquivo. {e}')
    return plain_text[:preview]


if __name__ == "__main__":
    get_links(sys.argv[1])
    print(clean_write(int(sys.argv[2]))) if len(
        sys.argv) > 2 else print(clean_write())
