from requests import get
from bs4 import BeautifulSoup

proxies = {
  	"http": "10.11.44.217:8080",
  	"https": "10.11.44.217:8080",
          }

# OBTENCION DE LA PAGINA WEB
# https://celulares.mercadolibre.com.ar/accesorios/_Desde_1951_PriceRange_200-300
# https://celulares.mercadolibre.com.ar/_Desde_51_PriceRange_200-300
# https://celulares.mercadolibre.com.ar/accesorios/capital-federal/
# https://celulares.mercadolibre.com.ar/accesorios/lapices-opticos/    cantidad 1017

#def consulta(categoria, subcategoria, provincia, localidad)

url = 'https://celulares.mercadolibre.com.ar/accesorios/capital_federal'
response = get(url, proxies=proxies)

# PARSEAR EL CONTENIDO DE LA PAGINA
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

#total_articulo = html_soup.find_all('div', class_ = 'quantity-results').text
#print (total_articulo)

articulos = html_soup.find_all('li', class_ = 'results-item highlighted article stack ')
print("Cantidad de articulos encontrados en la consulta: ",len(articulos))

for cursor in articulos:
	descripcion = cursor.find('span', class_ = 'main-title').text
	precio = cursor.find('span', class_ = 'price__fraction').text
	cantidad = cursor.find('div', class_ = 'item__condition').text
	if cursor.find('div', class_ = 'item__info item--hide-right-col '):
		link = cursor.find('div', class_ = 'item__info item--hide-right-col ').h2.a['href']
		#print ("Link del Articulo: ",link)
	else:
        	link = ""
		#if cursor.find('span', class_ = 'item__pad'):
		#	promo = cursor.find('span', class_ = 'item__pad')
		#	print ("Este articulo contiene:  ",promo)

	print ("Descricpion:  ",descripcion)
	print ("Precio: ",precio)
	print ("Cantidad: ",cantidad)
	print ("Enlace: ",link)


total_articulo = html_soup.find_all('div', class_ = 'quantity-results')[0].text
total_articulo = str(total_articulo)
total_articulo = total_articulo[1::]
n = total_articulo.find(" ")
total_articulo = total_articulo[:n]
total_articulo = int(total_articulo)

print (n)
print (total_articulo)
