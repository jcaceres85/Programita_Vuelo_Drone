# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:13:32 2021

@author: yessi
"""

import tkinter as tk
from tkinter.messagebox import showinfo

##Crear una instancia de Tkinter
ventana = tk.Tk()
ventana.geometry("990x700")

##Añadir color al fondo
ventana.config(bg='pink')

#Agregar etiqueta 1 DISTANCIA FOCAL
etiqueta1 = tk.Label(ventana, text='Distancia Focal', bg='black',  fg='yellow')
etiqueta1.grid(row = 0, column = 0)

#Agregar caja 1
entry1 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry1.grid(row = 1, column = 0)

#Agregar etiqueta 2 ANCHO DE IMAGEN
etiqueta2 = tk.Label(ventana, text=' Ancho de la Imagen(pixel)', bg='black',  fg='yellow')
etiqueta2.grid(row = 0, column = 1)

#Agregar caja 2
entry2 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry2.grid(row = 1, column = 1)

#Agregar etiqueta 3 ALTO DE IMAGEN
etiqueta2 = tk.Label(ventana, text=' Alto de la Imagen(pixel)', bg='black',  fg='yellow')
etiqueta2.grid(row = 0, column = 2)

#Agregar caja 3
entry3 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry3.grid(row = 1, column = 2)

#Agregar etiqueta 4 ANCHO DEL SENSOR
etiqueta4 = tk.Label(ventana, text=' Ancho del Sensor(mm)', bg='black',  fg='yellow')
etiqueta4.grid(row = 2, column = 0)

#Agregar caja 4
entry4 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry4.grid(row = 3, column = 0)

#Agregar etiqueta 5 ALTO DEL SENSOR
etiqueta5 = tk.Label(ventana, text=' Alto del Sensor(mm)', bg='black',  fg='yellow')
etiqueta5.grid(row = 2, column = 1)

#Agregar caja 5
entry5 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry5.grid(row = 3, column = 1)

#Agregar etiqueta 6 ALTURA DE VUELO
etiqueta6 = tk.Label(ventana, text=' Altura de Vuelo(m)', bg='black',  fg='yellow')
etiqueta6.grid(row = 2, column = 2)

#Agregar caja 
entry6 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry6.grid(row = 3, column = 2)

#Agregar etiqueta 7 SOLAPE LONGITUDINAL
etiqueta7 = tk.Label(ventana, text=' Solape Longitudinal', bg='black',  fg='yellow')
etiqueta7.grid(row = 4, column = 0)

#Agregar caja 7
entry7 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry7.grid(row = 5, column = 0)

#Agregar etiqueta 8 SOLAPE TRANSVERSAL
etiqueta8 = tk.Label(ventana, text=' Solape Transversal (%)', bg='black',  fg='yellow')
etiqueta8.grid(row = 4, column = 1)

#Agregar caja 8
entry8 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry8.grid(row = 5, column = 1)

#Agregar etiqueta 9 LARGO PARCELA
etiqueta8 = tk.Label(ventana, text=' Largo de Parcela (m)', bg='black',  fg='yellow')
etiqueta8.grid(row = 4, column = 2)

#Agregar caja 9
entry9 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry9.grid(row = 5, column = 2)

#Agregar etiqueta 10 ANCHO PARCELA
etiqueta8 = tk.Label(ventana, text=' Ancho de Parcela (m)', bg='black',  fg='yellow')
etiqueta8.grid(row = 6, column = 0)

#Agregar caja 10
entry10 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry10.grid(row = 7, column = 0)

#Agregar etiqueta 11 VELOCIDAD VUELO
etiqueta8 = tk.Label(ventana, text=' Velocidad de Vuelo', bg='black',  fg='yellow')
etiqueta8.grid(row = 6, column = 1)

#Agregar caja 11
entry11 = tk.Entry(ventana, font= 'Helvetica 20', justify = 'center')
entry11.grid(row = 7, column = 1)


#CAJA DE RESULTADOS
textResult = tk.Text(ventana)
textResult.grid(row = 13, column = 0, columnspan = 2)


#DATOS
def resultados():
    textResult.delete(1.0, tk.END)
    focal = float(entry1.get())
    ancho_img = float(entry2.get())
    alto_img = float(entry3.get())
    ancho_sensor = float(entry4.get())
    alto_sensor = float(entry5.get())
    alt_vuelo = float(entry6.get())
    solape_long = float(entry7.get())
    solape_trans = float(entry8.get())
    largo_parc = float(entry9.get())
    ancho_parc = float(entry10.get())
    v_vuelo = float(entry11.get())
    
    RSI= ancho_sensor / ancho_img
   
    #GDS
    GDS = (alt_vuelo * 100 / focal) * RSI
    textResult.insert(tk.END, f'GDS = {GDS}cm/pixel\n\n')
    
    #ESCALA DEL VUELO
    escala_vuelo = 1/((focal/1000)/alt_vuelo)
    textResult.insert(tk.END, f'Escala de vuelo = {escala_vuelo}\n\n')
    
    #ANCHO IMAGEN
    AnchoIST = (ancho_sensor*escala_vuelo)/1000
    textResult.insert(tk.END, f'Ancho de la Imagen Sobre el Terreno = {AnchoIST}m\n\n')
    
    #ALTO IMAGEN
    AltoIST = (alto_sensor*escala_vuelo)/1000
    textResult.insert(tk.END, f'Alto de la Imagen Sobre el Terreno = {AltoIST}m\n\n')
    
    #BASE AEREA
    b_area = ((ancho_img * GDS)/100)*(1-(solape_long/100))
    textResult.insert(tk.END, f'Base Aerea = {b_area}m\n\n')
    
    #DISTANCIA ENTRE PASADAS
    dist_pas = ((alto_img*GDS)/100) * (1-(solape_trans/100))
    textResult.insert(tk.END, f'Distancia entre Pasadas = {dist_pas}m\n\n')
    
    #TIEMPO ENTRE FOTOS Y VELOCIDAD DE VUELO
    t_fotos = b_area/v_vuelo
   
    textResult.insert(tk.END, f'Intervalo entre fotos = {t_fotos}s\n\n')
    textResult.insert(tk.END, f'Velocidad de Vuelo= {v_vuelo}m/s\n\n')
    
    #NUMERO DE PASADAS
    n_pasadas = ancho_parc/dist_pas
    textResult.insert(tk.END, f'Numero de Pasadas = {n_pasadas}\n\n')
    
    #NUMERO DE FOTOS POR PASADA 
    n_fotos = (largo_parc/b_area)+1
    textResult.insert(tk.END, f'Numero de Fotos por Pasadas = {n_fotos}\n\n')
    
    #NUMERO DE FOTOS POR VUELO 
    n_fvuelo= n_fotos*n_pasadas
    textResult.insert(tk.END, f'Numero de Fotos por Vuelo = {n_fvuelo}\n\n')
    
    #DISTANCIA DE VUELO
    d_vuelo = (n_pasadas*largo_parc)+ancho_parc
    textResult.insert(tk.END, f'Distancia de Vuelo = {d_vuelo}m\n\n')
    
    #DURACION DEL VUELO 
    t= (n_fotos*t_fotos)/60
    textResult.insert(tk.END, f'Duracion del Vuelo = {t}min\n\n')

    
    popup_showinfo()
    #VENTANA POP UP
def popup_showinfo():
    message ='Proceso Finalizado'
    showinfo(message)

      
#BOTON DE CALCULAR
botonCalcular = tk.Button(text = "CALCULAR", font= 'Helvetica 10', command = resultados)
botonCalcular.grid(row=10, column=1) 


##Añadir un título a la ventana
ventana.title("Calculadora de Parametros")

##Lanzar el GUI
ventana.mainloop()