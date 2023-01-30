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



for r in [line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]:
    print(r)