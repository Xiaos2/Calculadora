Tipo = input("Você quer conta de + - ou /")
Numero1 = float(input("Digite um numero"))
Numero2 = float(input("Digite outro numero"))
if Tipo == ("+"):
   print('{} + {} = '.format(Numero1, Numero2))
   print(Numero1 + Numero2)
elif Tipo == ("-"):
    print('{} - {} = '.format(Numero1, Numero2))
    print(Numero1 - Numero2)
elif Tipo == ("/"):
    print('{} / {} = '.format(Numero1, Numero2))
    print(Numero1 / Numero2)
else:
    print("invalido")