from __future__ import annotations
from datetime import *

class CashRegister:
    id = 0 

    def __init__(self):
        self.movimientos = []

    def add(self, cantidad, concepto):
        CashRegister.id += 1 # el id sale de la clase CashRegister y no tiene sentido que lo mande el usuario al igual que al fecha
        nuevo_movimiento = Movimiento(CashRegister.id , datetime.now(), cantidad, concepto)
        if len(self.movimientos) > 0:
            lista_temporal = []
            for item in self.movimientos:
                lista_temporal.append(item.date_time)
            if datetime.now() >= max(lista_temporal): #probar en casa
                if self.balance() + cantidad  > 0:
                    print("movimiento añadido correctamente")
                    self.movimientos.append(nuevo_movimiento)   
                else:
                    print("No se puede efectuar un movimiento que deje el balance en negativo")
            else:
                print("No se puede registrar un movimiento con fecha menor o igual a la ultima fecha")    
        else:
            if cantidad > 0:                
                self.movimientos.append(nuevo_movimiento)
                print("movimiento añadido correctamente")
            else:
                print("El primer movimiento no puede ser 0 o negativo")

    def balance(self):
        if len(self.movimientos) > 0:
            return sum(movimiento.amount for movimiento in self.movimientos) #me lo ha enseñado Ivan, aprender
        
            # balance_total = 0
            # for item in self.movimientos:
            #     balance_total += item.amount
            # return balance_total
        else:
            (print("La lista de movimientos esta vacia"))

    def delete_last(self):
        if len(self.movimientos) > 0:
            self.movimientos.pop()
            print("Movimiento borrado correctamente")
        else:
            print("La lista de movimientos esta vacia")
            # raise Exception("la lista de movimientos esta vacia")

    def save(self):
        for item in self.movimientos:
            print(f"{item.number}, {item.concept}, {item.date_time.strftime('%X %d/%m/%Y')}, {item.amount}")
        



    def __str__(self):
        for item in self.movimientos:
            print(item)



class Movimiento:
    def __init__(self, number, date_time, amount, concept):
        self.number = number
        self.date_time = date_time
        self.amount  = amount   
        self.concept = concept  

    def __str__(self):
        return f"ID: {self.number} Concepto: {self.concept} Fecha: {self.date_time.strftime('%X %d/%m/%Y')} Cantidad: {self.amount}"
        # poner comillas simples para evitar errorres en las cadenas F 

nuevo_registro = CashRegister()
nuevo_registro.add (100 , "ingreso")
nuevo_registro.add (200 , "ingreso")
nuevo_registro.add (300 , "ingreso")
nuevo_registro.delete_last()

nuevo_registro.save()

nuevo_registro.__str__() #esto tambien hay que mirarlo para el jueves




        
    

