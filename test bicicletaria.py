import unittest
import datetime

from main import Bicicletaria, Cliente

class Testes(unittest.TestCase):
    
    def setUp(self):
        self.bicletaria1 = Bicicletaria(20, 5, 25, 100, 0)
        self.cliente1 = Cliente("João", 200)
    
    def testeReceberPedidoEmprestimo (self):
        
        print("Teste de Bicicletaria - receber pedido por HORA.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime.now()), ("HORA", 18))
        
        print("Teste de Bicicletaria - receber pedido por DIA.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(1, "DIA", datetime.datetime.now()), ("DIA", 17))
        
        print("Teste de Bicicletaria - receber pedido por SEMANA.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(3, "SEMANA", datetime.datetime.now()), ("SEMANA", 14))

    def testeReceberPedidoEmprestimoQtdInvalida(self):
        
        print("Teste de Bicicletaria - receber pedido com quantidade inválida.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(-2, "HORA", datetime.datetime.now()), 0)

    def testeReceberPedidoEmprestimoQtdSupEstq(self):
        
        print("Teste de Bicicletaria - receber pedido com quantidade superior ao estoque.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(22, "DIA", datetime.datetime.now()), 0)
    
    def testeReceberPedidoEmprestimoLetra(self):
        
        print("Teste de Bicicletaria - receber pedido com letra ao invés de número.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo('z', "SEMANA", datetime.datetime.now()), 0)

    def testeReceberPedidoEmprestimoModInvalida(self):
        
        print("Teste de Bicicletaria - receber pedido com modalidade inválida.\n")
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(3, "SEMANAL", datetime.datetime.now()), 0)

    def testeCalcularConta (self):
        
        '''
        Nesses testes é importante sempre se atentar aos horários e valores de retorno antes de iniciá-los,
        pois em alguns lugares deixei datetime.datetime.now().
        '''
        print("Teste de Bicicletaria - calcular conta por HORA.\n")
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime.now()), 130)
        
        print("Teste de Bicicletaria - calcular conta por DIA.\n")
        self.bicletaria1.receberPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(1, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), datetime.datetime.now()), 50)
        
        print("Teste de Bicicletaria - calcular conta por SEMANA.\n")
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime.now()), 400)
        
        print("Teste de Bicicletaria - calcular conta por HORA com desconto FAMILIA.\n")
        self.bicletaria1.receberPedidoEmprestimo(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime.now()), 182)
        
        print("Teste de Bicicletaria - calcular conta por DIA com desconto FAMILIA.\n")
        self.bicletaria1.receberPedidoEmprestimo(3, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(3, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), datetime.datetime.now()), 105)
        
        print("Teste de Bicicletaria - calcular conta por SEMANA com desconto FAMILIA.\n")
        self.bicletaria1.receberPedidoEmprestimo(5, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(5, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime.now()), 700)

    def testeCalcularContaQtdInvalida(self):

        print("Teste de Bicicletaria - calcular conta com quantidade inválida.\n")
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(-2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime.now()), 0)

    def testeCalcularContaDevSupEstoq(self):

        print("Teste de Bicicletaria - calcular conta com devolução superior ao estoque.\n")
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime.now()), 0)

    def testeCalcularContaModInvalida(self):

        print("Teste de Bicicletaria - calcular conta com modalidade inválida.\n")
        self.bicletaria1.receberPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta(2, "DIARIA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime.now()), 0)

    def testeCalcularContaLetraQtd(self):

        print("Teste de Bicicletaria - calcular conta com letra na quantidade.\n")
        self.bicletaria1.receberPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00))
        self.assertEqual(self.bicletaria1.calcularConta('z', "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime.now()), 0)

    def testeReceberPagamento(self):

        print("Teste de Bicicletaria - receber pagamento exato. \n")
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00))
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime.now())
        self.assertEqual(self.bicletaria1.receberPagamento(200,200),0)

        print("Teste de Bicicletaria - receber pagamento com troco. \n")
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00))
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime.now())
        self.assertEqual(self.bicletaria1.receberPagamento(200,250), -50)

        print("Teste de Bicicletaria - receber pagamento parcial. \n")
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00))
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime.now())
        self.assertEqual(self.bicletaria1.receberPagamento(200,100), 100)

if __name__ == "__main__":
    unittest.main()