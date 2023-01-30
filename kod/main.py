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

#1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
#wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
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

#x=1.3

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

#strututu

#PEP8
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

#3. Niech użytkownik poda jakąś liczbę.
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


#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
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

#przerwa do 11:36
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

#5. Wyświetl 20 kolejnych potęg liczby 2
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

#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta
#
# for x in range(1,101,2):
#     print(x)
print(11%2)
print(10%2)