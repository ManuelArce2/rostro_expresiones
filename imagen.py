from PIL import Image
import numpy as np
import plotly.express as px

imagen_gr = Image.open("/home/manuel/Documentos/Graficacion/308952.jpg").convert('L')  
imagen_mat = np.array(list(imagen_gr.getdata(band=0)), float) # ESTRAE LOS DATOS

# Ajustar el tamaño de la matriz
imagen_mat.shape = (imagen_gr.size[1], imagen_gr.size[0])

# Mostrar la matriz y su forma
print(imagen_mat)
print(imagen_mat.shape)

# Visualizar la imagen usando Plotly
fig = px.imshow(imagen_mat, color_continuous_scale='gray')
fig.show()
