# print('cośtam')
# print("cośtam")
# print("Mc'Donalds")
# #przerwa do 10:22
# owoc='banan'
# kolor='żółty'
# print(owoc)
# print('owoc='+owoc)
# print('owoc={}'.format(owoc))
# zmienna='whatever'
# print('owoc={} kolor={}'.format(owoc,kolor,zmienna))
# print('owoc={} kolor={}'.format(owoc,kolor))
# print('owoc='+owoc+" kolor="+kolor)
# print(f'owoc={owoc} kolor={kolor}')
# x=1.2
# #print('x='+x)
# print('x='+str(x))
# print('x={}'.format(x))
# print(f'x={x}')
#
# owoc=input('podaj ulubiony owoc:')
# print(f'Twój ulubiony owoc to {owoc}')
#
# owoc=input('podaj ulubiony owoc:\n')
# print(f'Twój ulubiony owoc to {owoc}')

# 1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
#
# first_name=input('podaj imię:\n')
# last_name=input('podaj nazwisko:\n')
# print("Witaj "+first_name+" "+last_name+"!")
# print("Witaj {} {}!".format(first_name,last_name))
# print(f"Witaj {first_name} {last_name}!")
#
# x=1
# y=3.14
# z='tekst'
# print(type(x),type(y),type(z))
#
# x=input('podaj x:\n')
# x=float(x)
# print(x/2)


# x=float(input('podaj x:\n'))
# print(x/2)

# print(pow(2,10))
# print(round(10/3,2))
# x=float(input('dej x:\n'))
# print(x)

# x=input('podaj x:\n')
# try:
#     print(float(x))
# except ValueError:
#     print('podales cos innego niz liczba')

# x=1.3

# 2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę w kilogramach
# i wzrost w metrach, wyliczy i wypisze BMI zaokraglone do 2 miejsc po przecinku

# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'Twoje BMI={bmi}')

# x=10
# if x==10:
#     print('x jest równe 10')
# print('koniec')
#
# x=11
# if x==10:
#     print('x jest równe 10')
# print('koniec')


# x=10
# if x==10:
#     print('x jest równe 10')
#     print('x jest równe 10')
#     print('x jest równe 10')
# print('koniec')

#
# x=11
# if x==10:
#     print('x jest równe 10')
# else:
#     print('x NIE jest równe 10')
# print('koniec')

#
# x=3
# if x==1:
#     print('jeden')
# elif x==2:
#     print('dwa')
# elif x==3:
#     print('trzy')
# elif x==4:
#     print('cztery')
# else:
#     print('poza zakresem')

# strututu

# PEP8
#
# nazwa_zmiennej='costam' #python
# nazwaZmiennej="costam" #java,C#
#
# x='a'
# tekst="siała baba mak"
# if x in tekst:
#     print('tak, jest')
#
# x='a'
# lista=['a','b','c']
# if x in lista:
#     print('jest')
# else:
#     print('nie ma')

# 3. Niech użytkownik poda jakąś liczbę.
# Jeśli poda dodatnią to chcemy wyświetlić tę wartość z informacją
# "wartość dodatnia", jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".
#
# x!=1
# x<>1

# number=float(input('podaj jakąś liczbę:\n'))
# if number>0:
#     print(f'{number} jest dodatnie')
# elif number==0:
#     print(f'{number} jest zerem')
# else:
#     print(f'{number}  jest ujemne')


# 4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.


# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'Twoje BMI={bmi}')
# if bmi<16:
#     print('wygłodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa ok')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('I stopień przypakowania')
# elif bmi<40:
#     print('II stopień przypakowania')
# else:
#     print('III stopień przypakowania')

# przerwa do 11:36
#
# for x in range(10):
#     print('siema!')

#
# lista=[1,2,3,4]
# for e in lista:
#     print(e)


# for x in range(10):
#     print(f'siema po raz {x}!')


# for x in range(1,11):
#     print(f'siema po raz {x}!')
#
# for x in range(1,11):
#     print(x*1000)
# print(f'x na koniec wynosi {x}')

# 5. Wyświetl 20 kolejnych potęg liczby 2
#
# for p in range(1,21):
#     print(pow(2,p))

# for x in range(-10,11):
#     if x>0:
#         print(f'{x} jest dodatnie')
#     elif x==0:
#         print(f'{x} jest zerem')
#     else:
#         print(f'{x} jest ujemne')

# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta
#
# for x in range(1,101,2):
#     print(x)
# print(11%2)
# print(10%2)
#
# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzysta')
#     else:
#         print(f'{x} jest nieparzysta')

# 7.  Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna
#
# account=100000
# interest=0.08
# months=24
# for m in range(1,months+1):
#     account=round(account+(account*interest/12),2)
#     print(m, account)

#
# account=100000
# interest=-0.20
# months=60
# for m in range(1,months+1):
#     account=round(account+(account*interest/12),2)
#     print(m, account)

#
# while 1==1:
#     print('działam....')

#
# while True:
#     print('działam....')
#
# x=2
# while x<1000:
#     x=x*2
#     print(x)
#
# i=i+1
# i+=1
# #i++
# x=2
# while x<1000:
#     print(x)
#     x*=2
#
# import random
# print(random.random())
# print(random.randint(1,100))
#
# def funkcja():
#     print('siema!')
#
# funkcja()
#
# import my_lib
# my_lib.funkcja_w_innnym_module()

#
# import my_lib as ml
# ml.funkcja_w_innnym_module()

#
# from my_lib import funkcja_w_innnym_module
# funkcja_w_innnym_module()

# import requests

# 8. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od wartosci podanej przez uzytkownika

# import random
# limit=int(input('podaj maksymalną wartość:\n'))
# suma=0
# while suma<limit:
#     print(suma)
#     suma += random.randint(1, 10)
#
# while True:
#     pass
#
# def funkcja():
#     pass
#
# funkcja()

# import psycopg2

# przerwa obiadowa do 13:02

# text="siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.replace('a','X'))
# print(text.lower().replace('a','X'))
# print(text)
# text=text.upper()
# print(text)

# text="siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# print(len(text))
# list=[1,2,3,4,5]
# print(len(list))
# print(text.count('a'))
# print(text.lower().count('a'))

# text="\n                siała BABA mak i dostała 10 lat bo nie płaciła VAT\n"
# print(text)
# print(text.strip())
# print(text.replace(' ',''))
#
# text="siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# # for l in text:
# #     print(l)
# if 'BABA' in text:
#     print('jest')
# else:
#     print('nie ma')


# text="siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# if 'baba' in text:
#     print('jest')
# else:
#     print('nie ma')
#
# text="siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# if 'bAba'.lower() in text.lower():
#     print('jest')
# else:
#     print('nie ma')

# print('baba'*10)
# value=input('podaj wartość\n')
# print(value*10)
#
# value=float(input('podaj wartość\n'))
# print(value*10)
#
# if "Java">"Python":
#     print('chyba Cię gnie')
# else:
#     print('no rejczel')

# lista=['1','2','11','22']
# lista.sort()
# print(lista)
#
# lista=[1,2,11,22]
# lista.sort()
# print(lista)
#
# text="siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# print(text[0:11])
# print(text[0:11:2])
#
# text = "siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# print(text.index("BABA"))
# #CTRL+ALT+L - formatowanie
#
# text = "siała BABA mak i dostała 10 lat bo nie płaciła VAT"
# print(text.replace(' ','    '))

# if "Java">"A":
#     print('chyba Cię gnie')
# else:
#     print('no rejczel')

#
# print(f"du{chr(120)}pa")
# print(ord("x"))

# 9. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z niego
# znaki ,.!? i wyświetli powiększony do dużych liter na konsoli

# text=input('dej tekst:\n')
# print(text.replace(',','').replace('.','').replace('!','').replace('?','').lower())

# Tadeusz
# Tadeusz.
# Tadeusz,

#
# text=input('dej tekst:\n')
# unwanted=['!','?','.',',']
# for u in unwanted:
#     text=text.replace(u,'')
# print(text)

# for line in open('tadzio.txt',encoding='utf-8'):
#     print(len(line),line)

# for line in open('tadzio.txt',encoding='utf-8'):
#     print(len(line.strip()),line.strip())

# variable='tadzio.txt'
# for line in open(variable,encoding='utf-8'):
#     print(len(line.strip()),line.strip())

# 10. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik

#
# file_name=input('podaj nazwę pliku\n')
# for line in open(file_name,encoding='utf-8'):
#     if len(line.strip())>0:
#         print(line.strip())


# file_name=input('podaj nazwę pliku\n')
# x=0
# for line in open(file_name,encoding='utf-8'):
#     x+=1
#     if len(line.strip())>0:
#         print(x,line.strip())
#
# all=open('tadzio.txt',encoding='utf-8').read()
# print(all.replace('a','X'))

# 11. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.
#
# text="siała baba"
# print(text.count('a'))

# file_name=input('podaj nazwę pliku:\n')
# phrase=input('podaj szukaną frazę:\n')
# all=open(file_name,encoding='utf-8').read()
# print(all.lower().count(  phrase.lower()  ))
#
# file_name=input('podaj nazwę pliku:\n')
# phrase=input('podaj szukaną frazę:\n')
# print(open(file_name,encoding='utf-8').read().lower().count(  phrase.lower()  ))


# file_name=input('podaj nazwę pliku:\n')
# phrase=input('podaj szukaną frazę:\n')
# all=open(file_name,encoding='utf-8').read()
# print(open(file_name,encoding='utf-8').
#       read().
#       lower().
#       count(  phrase.lower()  ))


# 12.Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka po
#    odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#  i w jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.

# file_name=input('Podaj nazwę pliku w którym chcesz szukać:\n')
# phrase=input('Podaj frazę którą chcesz znaleźć:\n')
# x=0
# for line in open(file_name,encoding='utf-8'):
#     x+=1
#     if phrase.lower() in line.lower():
#         print(x,line.strip())

# przerwa do 14:20

# lista=[]
# lista=list()
# lista=[1,1,1,1,1,2,2,2,2,2,3,4,5]
# lista.append(6)
# lista.append(7)
# for e in lista:
#     print(e)
#
# lista=[1,2,"nietoperz",['A','B'] ]
# for e in lista:
#     print(e,type(e))

# 13. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

# list=[]
# for x in range(1,11):
#     list.append(pow(2,x))
#
# for e in list:
#     print(e)
#
# lista=[1,2,3,4,5]
# print(lista[2])
# print(lista[0:3])
# lista.insert(3,'dodane')
# print(lista)

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=list1+list2
# print(list3)
#
# def funkcja(*args):
#     pass
#
# list1=[1,2,3,4]
# print(list1)
# print(*list1)
#
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=[*list1,*list2]
# print(list3)


# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=[list1,list2]
# print(list3)
# print(list3[0][2])

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=[*list1,*list2]
#
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=list1+list2
#
#
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list1.extend(list2)
# print(list1)
#
# lista=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
# zbior=set(lista)
# print(zbior)
#
# lista=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
# obrobione=list(set(lista))
# print(obrobione)

# 14. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)
#
#
# import random
#
# l1 = []
# l2 = []
# for _ in range(10):
#     l1.append(random.randint(1, 10))
#     l2.append(random.randint(1, 10))
# print(l1)
# print(l2)
# l3=[*l1,*l2]
# print(l3)
# l3=l1+l2
# print(l3)
# l1.extend(l2)
# print(l1)

#List<String> lista=....
#
# x=1.5
# x='whatever'
# if type(x)==float:
#     print('przyjmuję')
# else:
#     print('nie przyjmuję')
#
# l=[]
# for x in range(1,11):
#     podlista=[x,x*10]
#     l.append(podlista)
#
# print(l)
# for e in l:
#     print(e)

#15. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.

#pandas
#
# l=[]
# for x in range(1,10):
#     podlista=[x,pow(2,x)]
#     l.append(podlista)
# print(l)

#
# l=[]
# for x in range(1,10): l.append([x,pow(2,x)])
# print(l)
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
#
# lista=[x for x in range(1,11)]
# print(lista)


# lista=[x*100 for x in range(1,11)]
# print(lista)
#
# lista=[]
# for x in range(1,101):
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,101) if x%2==0]
# print(lista)
#

#
# print([x for x in range(1,101) if x%2==0])


# import random
# lista=[]
# for _ in range(10):
#     lista.append(random.randint(1,10))
# print(lista)


# import random
# lista=[random.randint(1,10) for x in range(10)]
# print(lista)
# odfiltrowana=[e for e in lista if e%2==0]
# print(odfiltrowana)
# import random
# def fun(x):
#     if x%2==0:
#         return x*2
#     else:
#         return x*4
#
# lista=[random.randint(1,10) for x in range(10) ]
# przetworzone=[fun(e) for e in lista]
# print(przetworzone)


#16. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2
#
# l=[pow(2,e) for e in range(1,11)]
# print(l)
#print([pow(2,e) for e in range(1,11)])
# import matplotlib.pyplot as plt
# data=[pow(2,e) for e in range(1,11)]
# plt.plot(data)
# plt.show()
#
# lista=[1,2,3,4]
# lista2=lista.copy()
# lista.clear()
# print(lista)
# print(lista2)

#matplotlib, seaborn

# import matplotlib.pyplot as plt
# data=[pow(2,e) for e in range(1,11)]
# plt.plot(data,label="dane")
# plt.legend()
# plt.grid()
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.savefig('wykres.png')
# plt.show()

#17. Korzystając z list składanych wygeneruj listę 10 elementow której
# każdy element również będzie listą.
# Pierwszy element tej podlisty to numer potegi,
# a drugi to wartosc tej potegi dla liczby 2
#[ [x,x*100] for x .... ]
#
# lista=[ [e,pow(2,e)] for e in range(1,11)]
# print(lista)
#
# for line in open('dane.csv',encoding='utf-8'):
#     print(line.strip())
#
# line='2;Ferdynand;Kiepski;1.74;80'
# list=line.split(';')
# print(list)
# print(list[3],float(list[3])/2)

#18. Napisz program który z pliku dane.csv wyświetli powiekszone
# imiona i nazwiska oraz wzrost i masę
#list[2].lower()

# for line in open('dane.csv',encoding='utf-8'):
#     list=line.strip().split(';')
#     print(list[1].upper(),list[2].upper(),list[3],list[4])

#19. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv w taki sposób
# by linie oczyścic z bialych znaków i rozbić na listy. Każdy z elementów listy sam
# powinien byc listą. Następnie przeiteruj po wyniku i wyświetl wszystkie elementy
# listy   linia po linii.
#
# result=[]
# for line in open('dane.csv',encoding='utf-8'):
#     list=line.strip().split(';')
#     result.append(list)
# #
# result=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# for r in result:
#     print(r)

#
# for r in [line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]:
#     print(r)
# #
# for r in [line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]:
#     print(r[3],type(r[3]),float(r[3])/2)

#20. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
#   id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika
#
# for r in [line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]:
#     bmi=round(float(r[4])/pow(float(r[3]),2),2)
#     print(*r,bmi)

#
# for r in [line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]:
#     r.append(round(float(r[4])/pow(float(r[3]),2),2))
#     print(*r)
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# print(lista)
# print(max(lista),min(lista),sum(lista),sum(lista)/len(lista))
#
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# lista.sort()
# print(lista)

#
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# lista.sort()
# lista.reverse()
# print(lista)

#
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# lista.sort(reverse=True)
# print(lista)


# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# posortowana=sorted(lista)
# print(lista)
# print(posortowana)
# krotka=(2,3,1,4)
# krotka=sorted(krotka)
#
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# posortowana=sorted(lista,reverse=True)
# print(lista)
# print(posortowana)

#
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# posortowana=sorted(lista)
# posortowana.reverse()
# print(lista)
# print(posortowana)
# import random
# lista=[random.randint(1,1000) for _ in range(100)]
# #lista.sort()
# kopia=sorted(lista)

#21. Umieść w liście kwadraty losowych wartości z zakresu 1-100. Chcemy mieć w liście
#50 elementów. Na konsoli wyświetl różnicę pomiędzy najwyższą a najniższą wartością w liście
# Całą listę zaprezentuj na wykresie w postaci liniowej

# import matplotlib.pyplot as plt
# lista=[1,2,3,4]
# lista2=[2,4,6,8]
# plt.plot(lista)
# plt.plot(lista2)
# plt.show()

#anaconda, jupiter
#import tensorflow

# def funkcja(x,y):
#     print(x,y)
#
# funkcja('koza','nietoperz')

# def funkcja2(*args):
#     for a in args:
#         print(a)
#
# funkcja2('koza','nietoperz','toperz','banan')

# def funkcja(**params):
#     for k in params:
#         print(k,params[k])
#
# funkcja(param1='cośtam',imie='Andrzej',waluta='PLN')

#import time

# def mierzczas(fun):
#     def wewnetrzna(*args,**kwargs):
#         start=time.time()
#         fun(*args,**kwargs)
#         koniec=time.time()
#         print(f'funkcja trwała {koniec-start}s')
#     return wewnetrzna
# @mierzczas
# def funkcja():
#     time.sleep(3)
#     print('siema')

#funkcja()

# f=mierzczas(funkcja)
# f()
#
# import matplotlib.pyplot as plt
# wartosci=[2,4,8,16,32,64]
# osx=['01-2023','02-2023','03-2023','04-2023','05-2023','06-2023']
# plt.plot(osx,wartosci)
# plt.show()

#21. Umieść w liście kwadraty losowych wartości z zakresu 1-100. Chcemy mieć w liście
#50 elementów. Na konsoli wyświetl różnicę pomiędzy najwyższą a najniższą wartością w liście
# Całą listę zaprezentuj na wykresie w postaci liniowej

# import random
# import matplotlib.pyplot as plt
# kwadraty=[pow(random.randint(1,100),2) for _ in range(50)]
# print(kwadraty)
# print(max(kwadraty)-min(kwadraty))
# plt.plot(kwadraty)
# plt.show()
#
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B'],
#     [4,'D']
# ]
# lista.sort()
# print(lista)
#
# from operator import itemgetter
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B'],
#     [4,'D']
# ]
# lista.sort(key=itemgetter(1))
# print(lista)

#
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B'],
#     [4,'D']
# ]
# lista.sort(key=lambda x:x[1])
# print(lista)
#
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#     def __str__(self):
#         return str(self.__dict__)
#
# p1=Person('Andrzej','Klusiewicz')
# p2=Person('Monika','Bożko')
#
# lista=[p1,p2]
# lista.sort(key=lambda x:x.last_name)#,reverse=True)
# for e in lista:
#     print(e)

#22. Wczytaj do listy kolejne wiersze z pliku dane.csv.
# Dane posortuj po masie malejąco i wyswietl linia po linii na konsoli.
#
# data=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# data.sort(key=lambda x:float(x[4]),reverse=True)
# for d in data:
#     print(d)

# lista=['1','22','2','11']
# lista.sort()
# print(lista)

# lista=[1,22,2,11]
# lista.sort()
# print(lista)

#przerwa do 10:25

#23. Wyświetl na konsoli linia po linii dane z pliku dane.csv
# ale posortowane malejąco wg. bmi

#przypisanie danych do listy
#dodanie bmi do kazdego wiersza
#sortujemy listę po bmi
#iterujemy po liście wyswietlajac jej elementy

#
# data=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for d in data:
#     d.append(round(float(d[4])/pow(float(d[3]),2),2))
# data.sort(key=lambda e:e[5], reverse=True)
# for e in data:
#     print(e)

# import os
# os.mkdir("d:\\mapet")
#

#
# import os
# for w in os.walk("e:\\"):
#     print(w)
#
# import os
# for w in os.walk("e:\\"):
#     print(w[0])

#24. Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę
# - wraz ze ścieżkami. Wyszukiwarka ma być nieczuła na wielkość liter

# tekst="siała baba mak"
# if "bab" in tekst:
#     print('jest w tekście')
# else:
#     print('nie ma w tekście')
#
# lista=['siała','baba','mak']
# if "bab" in lista:
#     print('jest w liście')
# else:
#     print('nie ma w liście')
#
# for e in lista:
#     if "BAB".lower() in e.lower():
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')
#
# import os
# phrase="oracle"
# start_dir="e:\\"
# for w in os.walk(start_dir):
#     for c in w[1]:
#         if phrase.lower() in c.lower():
#             print(os.path.join(w[0],c))
#     for f in w[2]:
#         if phrase.lower() in f.lower():
#             print(os.path.join(w[0],f))
#

# import os
# phrase=input('podaj szukaną frazę:\n')
# start_dir=input('podaj katalog startowy:\n')
# for w in os.walk(start_dir):
#     for c in w[1]:
#         if phrase.lower() in c.lower():
#             print(os.path.join(w[0],c))
#     for f in w[2]:
#         if phrase.lower() in f.lower():
#             print(os.path.join(w[0],f))
#
# import re
# text="siała baba mak i dostała 10 lat bo nie płaciła vat"
# print(re.findall('\d{2}',text))
#
# import re
# text="email do mnie to klusiewicz@jsystems.pl jakbyście potrzebowali pomocy po szkoleniu"
# print(re.findall("\w{1,}@\w{1,}\.[a-zA-Z]{2,4}",text))

#pandas

#przerwa do 11:29
#
# lista=[1,2,3,4]
# krotka=(1,2,3,4)
# lista[2]='zmienione'
# print(lista)
# krotka[2]='zmienione'
# print(krotka)

# krotka=(6,7,12,1,2,3,4,1,1,1,1,1,1)
# lista=list(krotka)
# lista.sort()
# krotka=tuple(lista)
# print(krotka)
# for e in krotka:
#     print(e)
# if 12 in krotka:
#     print('jest')
# else:
#     print('nie ma')
#
# print(f'1 w krotce pojawia się {krotka.count(1)} razy')
#
# krotka=(6,7,12,1,2,3,4,1,1,1,1,1,1)
# posortowane=tuple(sorted(krotka))
# print(posortowane)


#25. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
# druga 10 losowych liczb zakresu 11-20. Stwórz trzecią krotkę która ma zawierać dane z obu krotek.
# Trzecią krotkę wypisz na konsoli posortowaną rosnąco.
#
# import random
# k1=tuple([random.randint(1,10) for _ in range(10)])
# print(k1)
# k2=tuple([random.randint(11,20) for _ in range(10)])
# print(k2)
# k3=(*k1,*k2)
# print(k3)
# print(sorted(k3))
# print(tuple(sorted(k3)))

#26.Napisz kod ktory wyświetli w postaci listy krotek zawartość pliku dane.csv

# data=[tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# print(data)
# for d in data:
#     print(d,type(d))

# z1={1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3}
# z1.add(4)
# print(z1)
#
# z1={1,2,3,4}
# z2={3,4,5,6}
# print("część wspólna:",z1.intersection(z2))
# print("suma zbiorów:",z1.union(z2))
# print("z1-z2:",z1.difference(z2))
# print("z2-z1:",z2.difference(z1))
# krotka=(1,2,3)
# print(sum(z1))
# print(sum(krotka))

# lista=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
# print(lista)
# zestaw=set(lista)
# print(zestaw)
# lista=list(zestaw)
# print(lista)
#
# result=list(set([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]))
# print(result)
# if len(result)==0:
#     print('jest pusta')

#27. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną

# import random
# z1={random.randint(1,40) for _ in range(20)}
# print(z1,len(z1))

# import random
# z1=set([random.randint(1,40) for _ in range(20)])
# print(z1,len(z1))


# import random
# z1={random.randint(1,40) for _ in range(20)}
# z2={random.randint(1,40) for _ in range(20)}
# print(z1)
# print(z2)
# print("suma:",z1.union(z2))
# print("część wspólna:",z1.intersection(z2))
# print("różnica z1-z2:",z1.difference(z2))
# print("różnica z2-z1:",z2.difference(z1))


#28. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.

#unhashable type list
#
# data=set([tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8') if ....])
# print(data)
# for d in data:
#     print(d)


#29. Przetwórz plik dane.csv w taki sposób by w efekcie umieścić w pliku output.csv znalazly się
# dane z pliku dane.csv wzbogacone o obliczone BMI, bez duplikatów i rozwiązując problem
# podania przecinka w miejsce kropki we wzroście i masie oraz problem z pustymi wierszami.

# plik=open('plik.txt',encoding='utf-8',mode='w')
# for x in range(1,11):
#     plik.write(f"linia numer {x}\n")
# plik.close()
#
# with open('plik.txt',encoding='utf-8',mode='w') as plik:
#     for x in range(1,11):
#         plik.write(f"linia numer {x}\n")
# print('koniec')
#
# lista=['1','Andrzej','Klusiewicz','1.76','72']
# print(f"{lista[0]};{lista[1]};{lista[2]}")
# print(";".join(lista))

#
# lista=['1','Andrzej','Klusiewicz','1.76','72',str(19.5)]
# print(f"{lista[0]};{lista[1]};{lista[2]}")
# print(";".join(lista))

#29. Przetwórz plik dane.csv w taki sposób by w efekcie umieścić w pliku output.csv znalazly się
# dane z pliku dane.csv wzbogacone o obliczone BMI, bez duplikatów i rozwiązując problem
# podania przecinka w miejsce kropki we wzroście i masie oraz problem z pustymi wierszami.
#
# data=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in data:
#     d.append(round(float(d[4])/pow(float(d[3]),2),2))
#     d=tuple(d)
#     print(d)

#
# data=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in data:
#     d.append(round(float(d[4])/pow(float(d[3]),2),2))
# tuples_data=[tuple(e) for e in data]
# for td in tuples_data:
#     print(td)
#
# data=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in data:
#     d.append(round(float(d[4])/pow(float(d[3]),2),2))
# tuples_data=[tuple(e) for e in data]
# data=list(set(tuples_data))
# for d in data:
#     print(d)


# data=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in data: d.append(str(round(float(d[4])/pow(float(d[3]),2),2)))
# with open('output.csv',encoding='utf-8',mode='w') as file:
#     for d in list(set([tuple(e) for e in data])):
#         line=";".join(d)+"\n"
#         file.write(line)
#
# data=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in data: d.append(str(round(float(d[4])/pow(float(d[3]),2),2)))
# with open('output.csv',encoding='utf-8',mode='w') as file:
#     for d in list(set([tuple(e) for e in data])): file.write(";".join(d)+"\n")

#przerwa obiadowa do 13:25

# sl=dict()
# sl['key1']='value 1'
# sl['key2']=1234
# sl['list']=[1,2,3,4]

# sl={
#     "key1":'value1',
#     "key2":1234
# }

# sl=dict()
# sl['key1']='value 1'
# sl['key2']=1234
# sl['list']=[1,2,3,4]
# print(sl['key1'])
# print(sl['key2'])
# print(sl['list'])
# for k in sl.keys():
#     print(k,sl[k])
# for k in sl:
#     print(k,sl[k])
#
# for v in sl.values():
#     print(v)

#30. Stwórz plik config.conf i umieść w nim poniższe dane
# encoding=utf-8
# timezone=-2
# color=black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna
# stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości


# sl=dict()
# for f in [e.strip().split('=') for e in open('config.conf',encoding='utf-8')]:
#     sl[f[0]]=f[1]
# # print(sl)
# #
# # for k in sl:
# #     print(k,sl[k])
#
# print(sl['encoding'])

#31. Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone z
# nazwiskiem rozdzielone spacja (powiększone obie wartości),
# a cały wiersz znajdzie się w wartości
#   jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.

# sl=dict()
# for f in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]: sl[f[1].upper()+" "+f[2].upper()]=f
# for k in sl: print(k,sl[k])
#
# print(sl['BABKA KIEPSKA'])

#32. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
# #
# Tadeusz
# Tadeusz.
# Tadeusz,
# Tadeusz!
#
# Wiosna
# wiosna
# import re
# print(set(re.findall("\W",open('tadzio.txt',encoding='utf-8').read())))

# unwanted=['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']
# text="siała !!!!???...,,"
# for u in unwanted:
#     text=text.replace(u,'')
# print(text)
# slowa=['cos','cos innego','cos']

# for s in slowa:
#     print(s,slowa.count(s))

# import time
# start=time.time()
# file_name='tadzio.txt'
# all=open(file_name,encoding='utf-8').read().lower()
# unwanted=['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']
# for u in unwanted:
#     all=all.replace(u,'')
# words=all.split()
# for w in words:
#     print(w,words.count(w)) #fuuuuuuu
# end=time.time()
# print(f'proces trwał {end-start}s')

# import time
# start=time.time()
# file_name='tadzio.txt'
# all=open(file_name,encoding='utf-8').read().lower()
# unwanted=['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']
# for u in unwanted:
#     all=all.replace(u,'')
# words=all.split()
# for w in words:
#     x=words.count(w) #fuuuuu
# end=time.time()
# print(f'proces trwał {end-start}s')

#przerwa do 14:38

# import time
# start=time.time()
# file_name='tadzio.txt'
# all=open(file_name,encoding='utf-8').read().lower()
# unwanted=['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']
# for u in unwanted:
#     all=all.replace(u,'')
# words=all.split()
# end=time.time()
# print(f'proces trwał {end-start}s')

# sl=dict()
# sl['key1']='value'
# if 'key2' in sl:
#     print('jest w słowniku')
# else:
#     print('nie ma w słowniku')



#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1

# import time
# start=time.time()
# file_name='tadzio.txt'
# all=open(file_name,encoding='utf-8').read().lower()
# unwanted=['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']
# for u in unwanted:
#     all=all.replace(u,'')
# words=all.split()
# sl=dict()
# for w in words:
#     if w in sl:
#         sl[w]+=1
#     else:
#         sl[w]=1
# for k in sl:
#     print(k,sl[k])
# end=time.time()
# print(f'proces trwał {end-start}s')


#    c) Przepakuj dane ze słownika do listy i posortuj a nastepnie wyswietl.
# import time
# start=time.time()
# file_name='tadzio.txt'
# all=open(file_name,encoding='utf-8').read().lower()
# unwanted=['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']
# for u in unwanted:
#     all=all.replace(u,'')
# words=all.split()
# sl=dict()
# for w in words:
#     if w in sl:
#         sl[w]+=1
#     else:
#         sl[w]=1
# result=[]
# for k in sl:
#     result.append([k,sl[k]])
# result.sort(key=lambda r:r[1],reverse=True)
# for e in result:
#     print(e)
# end=time.time()
# print(f'proces trwał {end-start}s')


# import time
# start=time.time()
# file_name='tadzio.txt'
# all=open(file_name,encoding='utf-8').read().lower()
# for u in ['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']:
#     all=all.replace(u,'')
# sl=dict()
# for w in all.split():
#     if w in sl:sl[w]+=1
#     else:sl[w]=1
# result=[[k,sl[k]] for k in sl]
# result.sort(key=lambda r:r[1],reverse=True)
# for e in result:  print(e)
# end=time.time()
# print(f'proces trwał {end-start}s')

# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for u in ['.', ')', '«', ',', '(', '?', ':', '*', '-', '…', '!', '/', '»', ';', '—']:
#     all=all.replace(u,'')
# sl=dict()
# for w in all.split():
#     if w in sl:sl[w]+=1
#     else:sl[w]=1
# result=[[k,sl[k]] for k in sl]
# result.sort(key=lambda r:r[1],reverse=True)
# for e in result:  print(e)

#import this

#33. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.

# for x in range(-10,11):
#     print(x,1/x)

#GIL

# print(1/0)
# print('coś jeszcze')

# try:
#     print(1/0)
#     print('druga czynność')
# except:
#     print('Jakaś muka...')
# print('coś jeszcze')
#
# try:
#     print(1/0)
#     print('druga czynność')
# except Exception as e :
#     print('Jakaś muka...',e,type(e))
# print('coś jeszcze')


# try:
#     filename="nieistniejacyplik.txt"
#     file=open(filename)
#     print(1/0)
#     print('druga czynność')
# except FileNotFoundError:
#     print('nie ma takiego pliku: ',filename)
# except ZeroDivisionError:
#     print('nie dziel przez zero!')
# except Exception as e:
#     print('jakiś inny wyjątek...',e,type(e))
# print('coś jeszcze')

#34. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10
# w taki sposob by w przypadku wyjatku nie przerywac dzialania petli
# a po prostu wyswietlic na konsoli informację o błędzie i przejsc
# do dalszego przetwarzania
