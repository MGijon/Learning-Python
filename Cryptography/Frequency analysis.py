text = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'

# creo un diccionario con las letras, para analizar sus frecuencias no distinguiré entre mayúsculas ni minúsculas

clean_text = text.lower()

letters = [chr(j) for j in range(ord('a'), ord('z') + 1)]
sizes = [0 for i in range(0, len(letters))]

warehouse = dict(zip(letters, sizes))


for l in clean_text:
    # modifico algunos caracteres que pueden ser molestos en castellano
    if l == 'á' or l == 'à':
        l = 'a'
    if l == 'é' or l == 'è':
        l = 'e'
    if l == 'í' or l == 'ì':
        l = 'i'
    if l == 'ó' or l == 'ò':
        l = 'o'
    if l == 'ú' or l == 'ù':
        l = 'u'
    if l.isalpha() and l != 'ñ':
        warehouse[l] += 1

# lo mostraré en porcentajes, creo otro diccionario por si acaso vuelvo a usar los datos:

warehouse_per = warehouse

total = sum(warehouse[j] for j in warehouse)
print(total)
for j in warehouse_per:
    warehouse_per[j] = warehouse_per[j] * 100 / total


from matplotlib.pylab import hist, show

data = []
for j in warehouse_per:
    data.append(warehouse_per[j])

hist(data, len(warehouse_per))
show()


