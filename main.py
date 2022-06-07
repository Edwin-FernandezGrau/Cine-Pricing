# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:55:34 2022

@author: 0xEwin (Ed Fernández)
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title= "Cine OBK",layout="wide")


import streamlit as st


st.markdown("## Variables a tomar en cuenta")
with st.expander("Variables"):
    st.markdown("## Variables para definir precios y segmentación de demanda 🎯")
    st.sidebar.header("Caso Cines OBK ")
    col1, col2,col3,col4 = st.columns([1,2,2,1])
    with col2:
        st.markdown("##### ")
        st.markdown("##### ")
        st.markdown("##### ")
        st.markdown("###### 1. Momento de compra")
        st.markdown("###### 2. Hora y día de la sesión")
        st.markdown("###### 3. Según la fila de butaca")
        st.markdown("###### 4. Según la película (Estrenos y early adopters)")
        st.markdown("##### ")
    with col3:
        st.markdown("##### ")
        st.markdown("##### ")
        st.markdown("##### ")
        st.markdown("###### 5. Elasticidad precio demanda")
        st.markdown("###### 6. Canibalización")
        st.markdown("###### 7. Demanda por canal")



st.markdown("## Esquema propuesto")
#st.sidebar.markdown("# Esquema propuesto")
st.markdown("##### ")
st.write("""
     La nueva estructura de precios dependerá de la **fila de ubicación de la butaca**,\n 
     la **fecha de compra** del tickets y de la **demanda esperada de la película** (early adopter / estrenos).\n 
          """)

st.markdown("""---""")
st.markdown("##### Días Normales ")  #--------------------                                     PROPUESTA DIAS NORMALES
     
col6, col7 ,col1, col2,col3,col4, col5,col8 = st.columns(8)


   # col1.markdown("**% Ventas x Mom compra**    # PORCENTAJE DE VENTAS POR MOMENTO DE COMPRA
prob_a = col2.slider('', 0, 20, 15)
prob_b = col3.slider('', 1, 30, 25)
prob_c = col4.slider('', 0, 30, 25)
limite =  100-prob_a-prob_b-prob_c
prob_d = col5.slider('',0 ,limite, min(35,limite))

 #                                              PORCENTAJE DE FILAS POR NIVEL
col6.write(""" """)
col6.write(""" """)
col6.write(""" """)
col6.write(""" """)
col6.write(""" """)
col6.write(""" """)
col6.markdown("**% Filas x nivel**")
cap_d1 = col6.slider('', 0.00, 15.00, 12.50)
cap_d2 = col6.slider("",0.00,70.00,50.00)
cap_d3 = col6.slider("",0.00,15.00,7.50)


with col1:
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.markdown("**Fila butaca/ Momento de compra**")


    st.write("""Arriba""")
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write("""Centro""")
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write(" ")
    st.write("""Abajo""")


col2.write("    4-2 días antes")
number_a1 = col2.number_input("",10,30,22)
number_a2 = col2.number_input("",10,30,18)
number_a3 = col2.number_input("",10,30,17)



col3.write("    1 día antes")
number_b1 = col3.number_input("",10,33,22)
number_b2 = col3.number_input("",10,32,20)
number_b3 = col3.number_input("",10,31,19)

col4.write("Hrs antes (online)")
number_c1 = col4.number_input("",10,36,22)
number_c2 = col4.number_input("",10,35,21)
number_c3 = col4.number_input("",10,34,19)

col5.write("Hrs antes")
number_d1 = col5.number_input("",13,36,23)
number_d2 = col5.number_input("",12,35,21)
number_d3 = col5.number_input("",11,34,20)





# resultados ----------------------------------------------------------------------------------------------------
t_pa = (number_a1*cap_d1 + number_a2*cap_d2 + number_a3*cap_d3)/(cap_d1 + cap_d2 + cap_d3)
t_pb = (number_b1*cap_d1 + number_b2*cap_d2 + number_b3*cap_d3)/(cap_d1 + cap_d2 + cap_d3)
t_pc = (number_c1*cap_d1 + number_c2*cap_d2 + number_c3*cap_d3)/(cap_d1 + cap_d2 + cap_d3)
t_pd = (number_d1*cap_d1 + number_d2*cap_d2 + number_d3*cap_d3)/(cap_d1 + cap_d2 + cap_d3)
t_fi = (t_pa*prob_a + t_pb*prob_b +t_pc*prob_c +t_pd*prob_d)/100
col1.write(" ")
col1.write(" ")
col1.write(" ")
col1.markdown("Ticket prom :")

col2.write(" ")
col2.write(" ")
col2.write(str(round(t_pa,2)))
col3.write(" ")
col3.write(" ")
col3.write(str(round(t_pb,2)))
col4.write(" ")
col4.write(" ")
col4.write(str(round(t_pc,2)))
col5.write(" ")
col5.write(" ")
col5.write(str(round(t_pd,2)))

col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(" ")
col8.write(str(round(t_fi,2)))

st.write("Capacidad de la sala al ", str(cap_d1+cap_d2+cap_d3), " % ")
st.markdown("""---""")


st.markdown("##### Películas Especiales ")   # -------------------DIAS ESPECIALES

col6, col7 ,col1, col2,col3,col4, col5,col8 = st.columns(8)

                                          # PORCENTAJE DE FILAS POR NIVEL
col6.write(""" """)
col6.write(""" """)
col6.markdown("**% Filas x nivel**")
cap_de1 = col6.slider('', 0.00, 15.00, 15.00)
cap_de2 = col6.slider("",0.00,70.00,70.00)
cap_de3 = col6.slider("",0.01,15.00,7.50)


with col1:
    st.markdown("**Fila butaca**")

    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write("""Arriba""")
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write("""Centro""")
    st.write(""" """)
    st.write(""" """)
    st.write(""" """)
    st.write("""Abajo""")


col2.write("Estrenos / early adopters")
number_e1 = col2.number_input("",10,30,24)
number_e2 = col2.number_input("",11,32,22)
number_e3 = col2.number_input("",11,31,21)

#                              RESULTADOS
t_pe = (number_e1*cap_de1 + number_e2*cap_de2 + number_e3*cap_de3)/(cap_de1 + cap_de2 + cap_de3)
col1.write(" ")
col1.write(" ")
col1.write(" ")
col1.markdown("Ticket prom :")
col2.write(" ")
col2.write(" ")
col2.write(str(round(t_pe,2)))
st.write("Capacidad de la sala al ", str(cap_de1+cap_de2+cap_de3), " % ")
st.markdown("""---""")

#####################################################RESUMEN Y SUPUESTOS
st.markdown("**Resumen: **")
d_esp = st.number_input("Seleccione número de días especiales al año.",5,48,28)
st.markdown("**Supuestos **")
col1, col2,col3,col4, col5,col6,col7 = st.columns([2,1,1,1,1,1,1])
n_sal = col1.number_input("Número de salas.",1,10,5)
n_fun = col1.number_input("Número de funciones.",1,6,3)
cap_su = col1.number_input("Capacidad max x sala.",100,200,150)

resultado = (d_esp*(cap_de1 + cap_de2 + cap_de3)*t_pe + (365-d_esp)*(cap_d1+cap_d2+cap_d3)*t_fi)*n_fun*cap_su*n_sal/100
   #col1.write("Resultado : " + str(round(resultado,2)))
df = pd.DataFrame()
df['Ingreso Anual'] = [round(resultado,2)]

st.dataframe(df)
######################################################## COMPARATIVO
st.markdown("""---""")
st.markdown("## Comparativo")
with st.expander("Enfoque actual vs Revenue Management"):
    col1, col2,col3,col4, col5,col6,col7 = st.columns([2,1,1,1,1,1,1])
    
    
    c_act= col1.number_input("Clientes año",350000,500000,400000)
    t_act= col1.number_input("Ticket prom anterior",0,39,20)
  


    dc = pd.DataFrame()
    
    dc['Index'] = ['Ventas', 'Costos', 'Utilidad']
    dc['Enfoque Anterior'] = [c_act*t_act,-c_act*t_act*1.1,-0.1*c_act*t_act ]
    dc['Enfoque RM'] = [round(resultado,2),-c_act*t_act*1.1, round(resultado,2)-c_act*t_act*1.1]
    dc.set_index("Index",inplace=True)
    st.markdown(""" """)
    st.write(""" """)
    st.write(""" """)
    st.dataframe(dc)

   
st.markdown("""---""")
st.markdown("## Elasticidad Precio Demanda")
with st.expander("El caso de los martes"):
    col1, col2,col3,col4, col5,col6,col7 = st.columns([2,1,1,1,1,1,1])
    
    
    elasticidad= col1.number_input("Elasticidad precio demanda",-1.50,2.0,1.50)
    pre_prom= col1.number_input("Precio promedio",0,40,20)
    tot_cli= col1.number_input("Total de clientes",750,2500,1350)
    cli_obj= col1.number_input("Clientes objetivo",750,2501,1650)
    
    var_q = (cli_obj-tot_cli)/tot_cli
    #elasticidad = var_q/var_p
    var_p = var_q/elasticidad
    st.write("El precio debe reducirse en " + str(round(var_p*100,2)) + " % ")



