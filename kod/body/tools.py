def bmi(weight,height):
    '''Funkcja przyjmuje masę jako pierwszy argument a wzrost jako drugi argument.
    Zwraca obliczone BMI lub wartość <0 w przypadku jakiegoś błedu'''
    try:
        return round(weight/pow(height,2),2)
    except ZeroDivisionError:
        print(f'Podałeś zerowy wzrost')
        return -1
    except TypeError:
        print('Podałeś wartość która nie jest liczbą')
        return -2
    except Exception as e:
        print(f'wyjątek {str(type(e))}: {str(e)}')
        return -3
