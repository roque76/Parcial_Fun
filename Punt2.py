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

# r=str(input('Ingresar región: '))
# rj_max(r)

def cv_tot ():
  df= arc_ex[['Región','Venta Millones']]
  df2 = df.groupby('Región').sum('Venta Millones')
  # print(df2)
  region=list(df['Región'].unique())
  region.sort()
  venta = list(df2['Venta Millones'])
  explode = (0.05, 0.05, 0.05, 0.05)

  print(df2)
  plt.pie(venta , labels=region, explode=explode)
  centre_circle = plt.Circle((0, 0), 0.70, fc='white')
  fig = plt.gcf()
  fig.gca().add_artist(centre_circle)

  plt.show
# cv_tot()

def av_tot_chart ():
    df = arc_ex
    df2 = df.groupby('Año').sum('Venta Millones')
    l_a = list(df['Año'].unique())
    l_a = sorted(l_a)
    l_v = list(df2['Venta Millones'])

    print(df2)
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
    print(df3)
    plt.barh(pl,l_v)
    plt.xlabel('Venta Millones')
    plt.ylabel('Plataforma')
    plt.title('Venta en Años')
# vp_tot()

def g_tot ():
  df = arc_ex[['Genero', 'Venta Millones']]
  df1 = df.groupby('Genero').sum('Venta Millones')
  print(df1)
  l_g = list(df['Genero'].unique())
  l_g.sort()
  l_vm = list(df1['Venta Millones'])
  explode = (0.05, 0.05, 0.05, 0.05, 0.05)
  
  plt.pie(l_vm , labels=l_g, explode=explode)
  centre_circle = plt.Circle((0, 0), 0.70, fc='white')
  fig = plt.gcf()
  fig.gca().add_artist(centre_circle)

  plt.show
# g_tot()

def r_tot ():
  df = arc_ex[['Región','Venta Millones']]
  df1 = df.groupby('Región').sum('Venta Millones')
  l_r = list(df['Región'].unique())
  l_r.sort()
  l_vm = list(df1['Venta Millones'])
  explode = (0.05, 0.05, 0.05, 0.05)
  
  plt.pie(l_vm , labels=l_r, explode=explode)
  print(df1)
# r_tot()