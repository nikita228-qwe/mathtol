import math
import sys
m=10000
def cr():

    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print("")
    print(F"Коэффициенты A, B, C — целые числа, по модулю не превышающие {m}")
cr()
zn = " ".join(sys.argv[1:]) 
if zn == "":
    cr()
if zn == "--help":
    cr()
if zn == "solve":

    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом")
    else:
        if abs(a) > m or abs(b) > m or abs(c) > m:
            print(f"ОШИБКА: коэффициенты должны быть целыми числами, по модулю не превышающими {m}")
        else:
            if a!=0:
                d = b**2 - 4*a*c 
                if d>0:
                    x1= (-b + math.sqrt(d)) / (2*a)
                    x2= (-b - math.sqrt(d)) / (2*a)
                    print("Уравнение квадратное")
                    print(f"D = {d}")
                    print(f"x1 = {x1:.3f}")
                    print(f"x2 = {x2:.3f}")
                elif d==0:
                    x = -b / (2*a)
                    print("Уравнение квадратное")
                    print(f"D = {d}")
                    print(f"x = {x:.3f}")
                else:
                    print ("Уравнение квадратное не имеет действительных корней")
                    print(f"D = {d}")
                    print("Действительных корней нет")

            if a==0 and b!=0:
                x = c*(-1)/b
                print("Уравнение линейное")
                print(f"x = {x:.3f}")
            if a==0 and b==0:
                print("ОШИБКА: это не уравнение, неизвестное отсутствует")

            


