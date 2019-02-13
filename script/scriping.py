from requests import get
from bs4 import BeautifulSoup

proxies = {
  "http": "10.11.44.217:8080",
  "https": "10.11.44.217:8080",
          }

# OBTENCION DE LA PAGINA WEB
url = 'https://celulares.mercadolibre.com.ar/accesorios/'
response = get(url, proxies=proxies)

# PARSEAR EL CONTENIDO DE LA PAGINA
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

#image-content

#print(response.text[:500])

articulos = html_soup.find_all('li', class_ = 'results-item highlighted article stack ')
#print(type(articulos))
print("Cantidad de articulos encontrados en la consulta: ",len(articulos))


###        PRIMER ARTICULO
#primer_articulo = articulos[0]
#descripcion = primer_articulo.find('span', class_ = 'main-title').text
#precio = primer_articulo.find('span', class_ = 'price__fraction').text
#cantidad = primer_articulo.find('div', class_ = 'item__condition').text
#link = primer_articulo.find('div', class_ = 'item__info item--hide-right-col ').h2.a['href']

#print ("Descricpion:  ",descripcion)
#print ("Precio: ",precio)
#print ("Cantidad: ",cantidad)
#print ("Link del Articulo: ",link)



for cursor in articulos:
	descripcion = cursor.find('span', class_ = 'main-title').text
	precio = cursor.find('span', class_ = 'price__fraction').text
	cantidad = cursor.find('div', class_ = 'item__condition').text
	if cursor.find('div', class_ = 'item__info item--hide-right-col '):
		link = cursor.find('div', class_ = 'item__info item--hide-right-col ').h2.a['href']
		print ("Link del Articulo: ",link)
	#else:
        	#if cursor.find('span', class_ = 'item__pad'):
		#	promo = cursor.find('span', class_ = 'item__pad')
		#	print ("Este articulo contiene:  ",promo)

	#print ("Item numero: ", cursor)
	print ("Descricpion:  ",descripcion)
	print ("Precio: ",precio)
	print ("Cantidad: ",cantidad)
	#print ("Link del Articulo: ",link)


