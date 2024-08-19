#definicion de clase
class Calculadora:
#calculadora estandar que opera con 2 nros 
    numero1=None
    numero2=None
    resultado=None
#constrcutor
    def __init__(self,x,y):
        self.numero1=x
        self.numero2=y
    def sumar(self):
        self.resultado=self.numero1+self.numero2
        return self.resultado
    def restar(self):
        self.resultado=self.numero1-self.numero2
        return self.resultado
    def multiplicar(self):
        self.resultado=self.numero1*self.numero2
        return self.resultado
    def dividir(self):
        self.resultado=self.numero1/self.numero2
        return self.resultado
    def setValores(self, x ,y ):
        self.numero1=x
        self.numero2=y
if __name__ == "__main__":
    x=int(input("ingrese el primer nro: "))
    y=int(input("ingrese el segundo nro: "))
    miCasio= Calculadora(x,y)

    print(f"la suma es: {miCasio.sumar()}")
    print(f"la resta es: {miCasio.restar()}")
    print(f"La multiplicacion es:{miCasio.multiplicar()}")
    print(f"la disivion es: {miCasio.dividir()}")
    x=int(input("ingrese el primer nro nuevo: "))
    y=int(input("ingrese el segundo nro nuevo: "))
    miCasio.setValores(x,y)

    print(f"la suma es: {miCasio.sumar()}")
    print(f"la resta es: {miCasio.restar()}")
    print(f"La multiplicacion es:{miCasio.multiplicar()}")
    print(f"la disivion es: {miCasio.dividir()}")
    texas= Calculadora(4,5)
    print(f"la suma es: {texas.sumar()}")
    print(f"la resta es: {texas.restar()}")