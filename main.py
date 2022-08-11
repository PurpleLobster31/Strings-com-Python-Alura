url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

'''
fatiamento:
texto = 'abcde'
texto[0] --> 'a'
texto[0:1] --> 'a'
texto[0:3] --> 'abc'
'''

indexInterrog = url.find('?')
url_base = url[:indexInterrog]
print(url_base)

url_paramentros = url[indexInterrog+1:]
print(url_paramentros)
