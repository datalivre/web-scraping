# Web Scraping com Beaultifulsoap
Raspando o site letras.com.br em busca de letras musicais.
-----
Este script capitura todas os links de uma banda, grupo ou artista a partir da página www.letras.com.br/{banda}, em seguida, ele acessa cada um dos links e capitura todas as músicas. O Tratamento começa com o método "punctuation" que remove todos os caracteres especiais do texto. Por fim, usando NLTK, este script remove todas as stopwords e retorna uma lista com as palavras restantes.  
