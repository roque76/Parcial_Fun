import pandas as pd 
import matplotlib.pyplot as plt

arc_ex = pd.read_excel('data_ventas_video_juegos_1 1.xlsx')
v_mill = arc_ex['Venta Millones']
p_col = arc_ex['Plataforma']
a_col = arc_ex['Año']

def v_tot ():
  v_tot=arc_ex['Venta Millones'].sum() #Toma todos los valores de la columna.
  return v_tot #Los suma y retorna el valor en la variable.

def av_tot (A):
  s_tot=0
  for x in range(len(a_col)):
    val = arc_ex.loc[x,'Año']
    if A == val:
        m = arc_ex.loc[x,'Venta Millones']
        s_tot=s_tot+m
  return s_tot

def v_plat (plat):
  s_tot =0
  for x in range (len(p_col)):
    v_str = arc_ex.loc[x,'Plataforma']
    if v_str == plat:
      i_int=arc_ex.loc[x,'Venta Millones']
      s_tot =s_tot+i_int
      
  return s_tot

def ap_max (A):
    ac_v=0
    mx_v=0
    pl1 = 0
    for x in range(len(a_col)):
        v_s = arc_ex.loc[x,'Año']
        if A==v_s:
            plat=arc_ex.loc[x,'Plataforma']
            pl1 = plat
            if A==v_s and pl1 == plat:
              v_m=arc_ex.loc[x,'Venta Millones']
              ac_v=ac_v+v_m
    return ac_v
    return pl1
x = ap_max(2000)  
print(f'{x}')



#i= str(input('Plataforma en mayusculas: '))
#v_plat(i)


