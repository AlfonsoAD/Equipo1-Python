
n1 = input("Ingrese el primer número de tres dígitos: ")
n2 = input("Ingrese el segundo número de tres dígitos: ")
if not(n1.isdigit() and len(n1) == 3 and n2.isdigit() and len(n2) == 3):
    print("Por favor, ingrese dos números de tres dígitos.")
else:
    in1 = int(n1[::-1])
    in2 = int(n2[::-1])
    print("Pruebas")
    print(in1,in2);

    if in1 > in2:
        print(in1)
    else:
        print(in2)





