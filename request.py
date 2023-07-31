from requests_html import HTMLSession

sessao = HTMLSession ()

url ='https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

resposta = sessao.get (url)

anuncios  = []

links = resposta.html.find ('#id-list li a')

for link in links :

    url_iphone = link.attrs ['href']

    resposta_iphone = sessao.get (url_iphone)

    titulo = resposta_iphone ('h1',first = True).text
    preco = resposta_iphone ('h2', first = True).text

    anuncios.append ({'url':url_iphone , 'titulo':titulo, 'preco': preco})

    print (anuncios)

