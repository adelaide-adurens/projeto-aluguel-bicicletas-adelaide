import unittest
import datetime

from main import Bicicletaria, Cliente

class Testes(unittest.TestCase):
    
    def setUp(self):
        self.bicletaria1 = Bicicletaria(20, 5, 25, 100, 0)
        self.cliente1 = Cliente("João", 200)
    
    def testeReceberPedidoEmprestimoHora (self):
        
        print("Teste de Bicicletaria - receber pedido por HORA.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), ("HORA", 18))
        
    def testeReceberPedidoEmprestimoDia (self):
        print("Teste de Bicicletaria - receber pedido por DIA.\n")
        self.cliente1.fazerPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), ("DIA", 19))
        
    def testeReceberPedidoSemana (self):
        print("Teste de Bicicletaria - receber pedido por SEMANA.\n")
        self.cliente1.fazerPedidoEmprestimo(3, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(3, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), ("SEMANA", 17))

    def testeReceberPedidoEmprestimoQtdInvalida(self):
        
        print("Teste de Bicicletaria - receber pedido com quantidade inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(-2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), 0)

    def testeReceberPedidoEmprestimoQtdSupEstq(self):
        
        print("Teste de Bicicletaria - receber pedido com quantidade superior ao estoque.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(22, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), 0)
    
    def testeReceberPedidoEmprestimoLetra(self):
        
        print("Teste de Bicicletaria - receber pedido com letra ao invés de número.\n")
        self.cliente1.fazerPedidoEmprestimo(3, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo('z', "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), 0)

    def testeReceberPedidoEmprestimoModInvalida(self):
        
        print("Teste de Bicicletaria - receber pedido com modalidade inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(3, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.assertEqual(self.bicletaria1.receberPedidoEmprestimo(3, "SEMANAL", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1), 0)

    def testeCalcularContaHora (self):
        
        print("Teste de Bicicletaria - calcular conta por HORA.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 120)

    def testeCalcularContaDia (self):

        print("Teste de Bicicletaria - calcular conta por DIA.\n")
        self.cliente1.fazerPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(1, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 25)
        
    def testeCalcularContaSemana (self):

        print("Teste de Bicicletaria - calcular conta por SEMANA.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 200)

    def testeCalcularContaHoraFamilia (self):

        print("Teste de Bicicletaria - calcular conta por HORA com desconto FAMILIA.\n")
        self.cliente1.fazerPedidoEmprestimo(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 168)
    
    def testeCalcularContaDiaFamilia (self):

        print("Teste de Bicicletaria - calcular conta por DIA com desconto FAMILIA.\n")
        self.cliente1.fazerPedidoEmprestimo(3, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(3, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00),self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(3, "DIA", datetime.datetime(2021, 8, 21, 22, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 52.5)
    
    def testeCalcularContaSemanaFamilia (self):

        print("Teste de Bicicletaria - calcular conta por SEMANA com desconto FAMILIA.\n")
        self.cliente1.fazerPedidoEmprestimo(5, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(5, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00),self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(5, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 350)
    
    def testeCalcularContaQtdInvalida(self):

        print("Teste de Bicicletaria - calcular conta com quantidade inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00),self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(-2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 0)

    def testeCalcularContaDevQtdErrada(self):

        print("Teste de Bicicletaria - calcular conta com devolução com quantidade diferente da emprestada.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(4, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 0)

    def testeCalcularContaModInvalida(self):

        print("Teste de Bicicletaria - calcular conta com modalidade inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(2, "DIARIA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 0)

    def testeCalcularContaLetraQtd(self):

        print("Teste de Bicicletaria - calcular conta com letra na quantidade.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta('z', "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1), 0)
    
    def testeCalcularContaDeltaNeg(self):

        print("Teste de Bicicletaria - calcular conta com delta negativo.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.bicletaria1.calcularConta(2, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 21, 10, 00, 00), self.cliente1), 0)

    def testeReceberPagamentoExato(self):

        print("Teste de Bicicletaria - receber pagamento exato. \n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.cliente1)
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1)
        self.assertEqual(self.bicletaria1.receberPagamento(200,200),0)

    def testeReceberPagamentoTroco (self):
        print("Teste de Bicicletaria - receber pagamento com troco. \n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.cliente1)
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1)
        self.assertEqual(self.bicletaria1.receberPagamento(200,250), -50)

    def testeReceberPagamentoParcial (self):
        print("Teste de Bicicletaria - receber pagamento parcial. \n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.cliente1)
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1)
        self.assertEqual(self.bicletaria1.receberPagamento(200,100), 100)

    def testeReceberPagamentoValorPgtInval(self):

        print("Teste de Bicicletaria - receber pagamento com valor pagamento inválido. \n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.cliente1)
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1)
        self.assertEqual(self.bicletaria1.receberPagamento(200,-20),0)

    def testeReceberPagamentoValorTotInv (self):
        print("Teste de Bicicletaria - receber pagamento com valor total inválido. \n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), self.cliente1)
        self.bicletaria1.calcularConta(2, "SEMANA", datetime.datetime(2021, 8, 15, 23, 00, 00), datetime.datetime(2021, 8, 22, 21, 35, 32), self.cliente1)
        self.assertEqual(self.bicletaria1.receberPagamento(-20,200),0)


if __name__ == "__main__":
    unittest.main()