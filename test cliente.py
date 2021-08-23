import unittest
import datetime

from main import Bicicletaria, Cliente

class Testes(unittest.TestCase):
    
    def setUp(self):
        self.bicletaria1 = Bicicletaria(20, 5, 25, 100, 0)
        self.cliente1 = Cliente("João", 200)

    def testeFazerPedidoEmprestimo(self):
        print("Teste de Cliente - fazer pedido por HORA.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), (2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00)))

        print("Teste de Cliente - fazer pedido por DIA.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), (1, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00)))

        print("Teste de Cliente - fazer pedido por SEMANA.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), (2, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00)))

    def testeFazerPedidoEmprestimoQtdInvalida(self):
        
        print("Teste de Cliente- fazer pedido com quantidade inválida.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(-1, "SEMANA", datetime.datetime.now(), self.bicletaria1), 0)

    def testeFazerPedidoEmprestimoQtdSupEstq(self):
        
        print("Teste de Cliente- fazer pedido com quantidade superior ao estoque.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(23, "SEMANA", datetime.datetime.now(), self.bicletaria1), 0)
    
    def testeFazerPedidoEmprestimoLetra(self):
        
        print("Teste de Cliente- fazer pedido com letra ao invés de número.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo('y', "SEMANA", datetime.datetime.now(), self.bicletaria1), 0)

    def testeFazerPedidoEmprestimoModInvalida(self):
        
        print("Teste de Cliente- fazer pedido com modalidade inválida.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "MENSAL", datetime.datetime.now(), self.bicletaria1), 0)
    
    '''
    Teste de Bicicletaria Inválida não é possível de ser feito, 
    pois ele diz que não reconhece se colocar uma bicicletaria inválida como argumento.
    def testeFazerPedidoEmprestimoBicilInvalida(self):
        
        print("Teste de Cliente- fazer pedido com bicicletaria inválida.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime.now(), bicletaria2), 0)
    '''
    

if __name__ == "__main__":
    unittest.main()