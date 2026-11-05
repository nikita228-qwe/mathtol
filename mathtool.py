import math
import sys
m=500000000000
def cr():

    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print("")
    print(F"Коэффициенты A, B, C — целые числа, по модулю не превышающие {m}")
zn = sys.argv[1:]
if not zn:
    cr()
    sys.exit(0)
elif zn[0] == "--help":
    cr()
    sys.exit(0)
elif zn[0] == "solve" or zn[0] == "sol":
     
     
    try:
        if len(zn) == 1:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        elif len(zn) == 7:
            if zn[1] != "-a" or zn[3] != "-b" or zn[5] != "-c":
                print("ОШИБКА: неизвестный параметр, ожидаются -a, -b, -c", file=sys.stderr)
                sys.exit(1)
            a = int(zn[2])
            b = int(zn[4])
            c = int(zn[6])
        else: 
            print("ОШИБКА: неверный набор параметров", file=sys.stderr)
            sys.exit(1)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)
    else:
        if abs(a) > m or abs(b) > m or abs(c) > m:
            print(f"ОШИБКА: коэффициенты должны быть целыми числами, по модулю не превышающими {m}", file=sys.stderr)
            sys.exit(1)
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
                    sys.exit(0)

            if a==0 and b!=0:
                x = c*(-1)/b
                print("Уравнение линейное")
                print(f"x = {x:.3f}")
            if a==0 and b==0:
                print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
                sys.exit(1)
else:
    print("ОШИБКА: неизвестная команда, ожидается solve",file=sys.stderr )
    sys.exit(1)
