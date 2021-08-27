import unittest
import datetime

from main import Bicicletaria, Cliente

class Testes(unittest.TestCase):
    
    def setUp(self):
        self.bicletaria1 = Bicicletaria(20, 5, 25, 100, 0)
        self.cliente1 = Cliente("João", 200)
        self.cliente2 = Cliente("Maria", 250)

    def testeBicicletaria2Clientes(self):
        print("Teste de 2 Clientes e Bicicletaria efetuando empréstimo no mesmo dia.")
        self.cliente1.fazerPedidoEmprestimo(3, 'HORA',datetime.datetime(2021, 8, 25, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(3, 'HORA', datetime.datetime(2021, 8, 25, 10, 00, 00), self.cliente1)
        self.cliente2.fazerPedidoEmprestimo (1, 'DIA', datetime.datetime(2021, 8, 25, 11, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(1, 'DIA', datetime.datetime(2021, 8, 25, 11, 00, 00), self.cliente2)
        self.cliente1.devolverEmprestimo(3, 'HORA', datetime.datetime(2021, 8, 25, 10, 00, 00), datetime.datetime(2021, 8, 25, 12, 20, 00), self.bicletaria1)
        self.assertEqual(self.cliente1.fazerPagamento(50, self.bicletaria1, 3, 'HORA', datetime.datetime(2021, 8, 25, 10, 00, 00), datetime.datetime(2021, 8, 25, 12, 20, 00)), 168.5)

if __name__ == "__main__":
    unittest.main()