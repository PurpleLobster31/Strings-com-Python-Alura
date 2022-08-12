url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

'''
fatiamento:
texto = 'abcde'
texto[0] --> 'a'
texto[0:1] --> 'a'
texto[0:3] --> 'abc'
'''
# Separa base e os parâmetros
indexInterrog = url.find('?')
url_base = url[:indexInterrog]
print(url_base)
url_parametros = url[indexInterrog+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)    
tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if (indice_e_comercial == -1):
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

