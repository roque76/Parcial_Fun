import pandas as pd

#funcion 10
def primer_dig(num):
  if num>=10:
    num//=10
  return(num)


'''Parametro  con retorno
'''
def primer_dig():
  num=int(input("Ingresar numero: "))
  if num>=10:
    num//=10
  return(num)
#Sin parametro retorno

def primer_dig():
  num=59
  if num>=10:
    num//=10
  print(num)
# Sin parametro sin retorno

def primer_dig(num):
  if num>=10:
    num//=10
  print(num)

#Paremtro sin retorno

''' 
Función 20
'''

# vector=[]
# for i in range(5):
#   vector.append(int(input('Ingrese el elemento: ')))

def ident (lista):
    list1=pd.Series(lista)
    long = len(list1.unique())
    if long==1:
        return 1
    else:
        return 0
#Paremtro con retorno

def ident ():
  vector=[]
  for i in range(5):
    vector.append(int(input('Ingrese el elemento: ')))
  list1=pd.Series(vector)
  long = len(list1.unique())
  if long==1:
      return 1
  else:
      return 0
#Sin parametro con retorno


def ident ():
  vector=[]
  for i in range(5):
    vector.append(int(input('Ingrese el elemento: ')))
  list1=pd.Series(vector)
  long = len(list1.unique())
  if long==1:
      print(1)
  else:
    print(0)

# vector=[]
# for i in range(5):
#   vector.append(int(input('Ingrese el elemento: ')))

def ident (lista):
    list1=pd.Series(lista)
    long = len(list1.unique())
    if long==1:
        print(1, 'Íguales')
    else:
        print(0, 'No')

#Parametro sin retorno

#funcion 30
# vector=[]

# for i in range(10):
#   vector.append(int(input('Ingrese el elemento: ')))

def primoMayor(vector):
  vector_extra=[]
  primos=[]
  
  for i in range(2, len(vector)):
    for j in range(2,vector[i]):
      if vector[i]% j ==0:
       print('')
    vector_extra.append(vector[i])

  for x in range(len(vector_extra)):
    if vector_extra[x]%10:
      primos.append(vector_extra[x])

  return max(primos)

#Parametro con retorno

vector=[]


# vector=(9,12,2,3,17,31,13,24,79,97)

def primoMayor(vector):
  vector_extra=[]
  primos=[]
  
  for i in range(2, len(vector)):
    for j in range(2,vector[i]):
      if vector[i]% j ==0:
       print('')
    vector_extra.append(vector[i])

  for x in range(len(vector_extra)):
    if vector_extra[x]%10:
      primos.append(vector_extra[x])

  print(max(primos))

# primoMayor(vector)
#Con parametro sin retorno

def primoMayor():
  vector=[]

  for i in range(10):
    vector.append(int(input('Ingrese el elemento: ')))
    vector_extra=[]
    primos=[]
  
    for i in range(2, len(vector)):
      for j in range(2,vector[i]):
        if vector[i]% j ==0:
          print('')
      vector_extra.append(vector[i])

    for x in range(len(vector_extra)):
     if vector_extra[x]%10:
      primos.append(vector_extra[x])

     return max(primos)

# print('El numero primo mayor es:  ', primoMayor())
#Sin parametro con retorno

def primoMayor():
  vector=[]

  for i in range(10):
    vector.append(int(input('Ingrese el elemento: ')))
    vector_extra=[]
    primos=[]
  
    for i in range(2, len(vector)):
      for j in range(2,vector[i]):
        if vector[i]% j ==0:
          print('')
      vector_extra.append(vector[i])

    for x in range(len(vector_extra)):
     if vector_extra[x]%10:
      primos.append(vector_extra[x])

     print(max(primos))

# primoMayor()
#Sin parametro sin retorno