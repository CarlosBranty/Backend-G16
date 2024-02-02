def sumar(num1,num2):
    return num1+num2

resultado=sumar(num1=5,num2=7)
print(resultado)

data = {
    'num1':10,
    'num2':20
}
resultado == sumar(**data)