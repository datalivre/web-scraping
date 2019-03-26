# Web Scraping com Beaultifulsoap
Raspando o site letras.com.br em busca de letras musicais.
-----
### O que é
Este script captura todas os links de uma banda, grupo ou artista a partir da página www.letras.com.br/{banda}, em seguida, ele acessa cada um dos links e captura todas as músicas. O Tratamento começa com o método "punctuation" que remove todos os caracteres especiais do texto. Por fim, usando NLTK, este script remove todas as stopwords e retorna uma lista com as palavras restantes.
### Finalidade
Com este script é possível capturar grande massa de palavras a fim de trabalhar com análise de sentimentos ou simplesmente criar uma nuvem de tags.
