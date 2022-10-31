import pandas as pd 
import matplotlib.pyplot as plt

arc_ex = pd.read_excel('data_ventas_video_juegos_1 1.xlsx')
v_mill = arc_ex['Venta Millones']
p_col = arc_ex['Plataforma']
a_col = arc_ex['Año']




def v_tot ():
  v_tot=arc_ex['Venta Millones'].sum() #Toma todos los valores de la columna.
  return v_tot #Los suma y retorna el valor en la variable.

def av_tot ():
    df = arc_ex
    df2 = df.groupby('Año').sum('Venta Millones')
    print(df2)

def v_plat (plat):

  df =arc_ex[arc_ex['Plataforma']==plat][['Venta Millones','Plataforma']]
  df2 = df.groupby('Plataforma').sum('Venta Millones')
  print(df2)

def ap_max (i):
    
    df = arc_ex[arc_ex['Año']==i][['Plataforma','Venta Millones']]
    df2 = df.groupby('Plataforma').sum('Venta Millones')
    max_df2 = df2['Venta Millones'].max()
    print(df2[df2['Venta Millones']==max_df2])

# i=int(input('Año: '))
# ap_max(i)

def jc_max (j):
  df = arc_ex[arc_ex['Nombre']==j][['Región','Venta Millones']]
  df2 = df.groupby('Región').sum('Venta Millones')
  print(df2)
  print(a)
# j=str(input('Ingresar nombre del juego: '))
# jc_max(j)

def rj_max (r):
  df = arc_ex[arc_ex['Región']==r][['Nombre','Venta Millones']]
  df2 = df.groupby('Nombre').sum('Venta Millones')
  max_df2 = df2['Venta Millones'].max()
  print(df2[df2['Venta Millones']==max_df2])

def cv_tot ():
  df= arc_ex[['Región','Venta Millones']]
  df2 = df.groupby('Región').sum('Venta Millones')
  # print(df2)
  region=['Europa','Japón','Norte America', 'Otros']
  venta =[937.84,456.02,1708.37,322.19]
  explode = (0.05, 0.05, 0.05, 0.05)

  plt.pie(venta , labels=region, explode=explode)
  centre_circle = plt.Circle((0, 0), 0.70, fc='white')
  fig = plt.gcf()
  fig.gca().add_artist(centre_circle)

  plt.show
# cv_tot()

def av_tot_chart ():
    df = arc_ex
    df1 = arc_ex[['Año', 'Venta Millones']]
    df2 = df.groupby('Año').sum('Venta Millones')
    l_a = list(df1['Año'].unique())
    l_a = sorted(l_a)
    l_v = list(df2['Venta Millones'])

    plt.bar(l_a,l_v)
    plt.xlabel('Años ')
    plt.ylabel('Venta Millones')
    plt.title('Venta en Años')
# av_tot_chart()

def vp_tot ():
    df = arc_ex[['Plataforma','Venta Millones']]
    df3 = df.groupby('Plataforma').sum('Venta Millones')
    l_a = list(df['Plataforma'].unique())
    l_v = list(df3['Venta Millones'])
    pl=['2600A', 'PS', 'N64', 'PS2', 'DS', '3DS', 'Wii', 'PS3', 'X360', 'PS4', 'WiiU', 'XOne', 'PSP', 'PSV', 'XB', 'PC', 'GBA', 'GC', 'SNES', 'NES', 'SAT', 'GEN', 'DC', 'GB', '3DO', 'TG16', 'NG', 'SCD']
    pl.sort()
    # print(l_v)
    print(pl)
    print(df3)
    plt.barh(pl,l_v)
    plt.xlabel('Venta Millones')
    plt.ylabel('Plataforma')
    plt.title('Venta en Años')
# vp_tot()

def