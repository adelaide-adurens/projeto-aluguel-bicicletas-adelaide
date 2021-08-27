import unittest
import datetime

from main import Bicicletaria, Cliente

class Testes(unittest.TestCase):
    
    def setUp(self):
        self.bicletaria1 = Bicicletaria(20, 5, 25, 100, 0)
        self.cliente1 = Cliente("João", 200)

    def testeFazerPedidoEmprestimoHora(self):
        print("Teste de Cliente - fazer pedido por HORA.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), (2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00)))

    def testeFazerPedidoEmprestimoDia (self):
        print("Teste de Cliente - fazer pedido por DIA.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(1, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), (1, "DIA", datetime.datetime(2021, 8, 22, 10, 00, 00)))

    def testeFazerPedidoEmprestimoSemana (self):
        print("Teste de Cliente - fazer pedido por SEMANA.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), (2, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00)))    

    def testeFazerPedidoEmprestimoQtdInvalida(self):
        
        print("Teste de Cliente- fazer pedido com quantidade inválida.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(-1, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), 0)

    def testeFazerPedidoEmprestimoQtdSupEstq(self):
        
        print("Teste de Cliente- fazer pedido com quantidade superior ao estoque.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(23, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), 0)

    def testeFazerPedidoEmprestimoLetra(self):
        
        print("Teste de Cliente- fazer pedido com letra ao invés de número.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo('y', "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), 0)

    def testeFazerPedidoEmprestimoModInvalida(self):
        
        print("Teste de Cliente- fazer pedido com modalidade inválida.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "MENSAL", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1), 0)

    def testeFazerPedidoEmprestimoBicilInvalida(self):
        
        print("Teste de Cliente- fazer pedido com bicicletaria inválida.\n")
        self.assertEqual(self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 22, 10, 00, 00), "string"), 0)

    def testeDevolverEmprestimo(self):
        print("Teste de Cliente - devolver empréstimo feito por SEMANA.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.devolverEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 10, 00, 00),self.bicletaria1), datetime.datetime(2021, 8, 22, 10, 00, 00))

    def testeDevolverEmprestimoQtdInval(self):
        print("Teste de Cliente - devolver empréstimo com quantidade inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.devolverEmprestimo(-2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 10, 00, 00),self.bicletaria1), 0)

    def testeDevolverEmprestimoQtdDifEmprest(self):
        print("Teste de Cliente - devolver empréstimo com quantidade diferente do emprestado.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.devolverEmprestimo(4, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 10, 00, 00),self.bicletaria1), 0)

    def testeDevolverEmprestimoModInval(self):
        print("Teste de Cliente - devolver empréstimo com modalidade inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.devolverEmprestimo(2, "SEMANAL", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 10, 00, 00),self.bicletaria1), 0)

    def testeDevolverEmprestimoHoraInval(self):
        print("Teste de Cliente - devolver empréstimo com horário inválido\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.devolverEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 22, 22, 00, 00), datetime.datetime(2021, 8, 15, 10, 00, 00),self.bicletaria1), 0)

    def testeDevolverEmprestimoBiciclInval(self):
        print("Teste de Cliente - devolver empréstimo com bicicletaria inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.devolverEmprestimo(2, "SEMANA", datetime.datetime(2021, 8, 15, 22, 00, 00), datetime.datetime(2021, 8, 22, 10, 00, 00),"string"), 0)

    def testeFazerPagamentoExato(self):
        print("Teste de Cliente - fazer pagamento exato.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.fazerPagamento(10, self.bicletaria1, 2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 11, 00, 00)), 190)

    def testeFazerPagamentoTroco (self):
        print("Teste de Cliente - fazer pagamento com troco.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.fazerPagamento(20, self.bicletaria1, 2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 11, 00, 00)), 190)

    def testeFazerPagamentoParcial (self):
        print("Teste de Cliente - fazer pagamento parcial.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.fazerPagamento(5, self.bicletaria1, 2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 11, 00, 00)), 195)    

    def testeFazerPagamentoPgtoNegat(self):
        print("Teste de Cliente - fazer pagamento negativo.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.fazerPagamento(-10, self.bicletaria1, 2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 11, 00, 00)), -1)

    def testeFazerPagamentoPgtoMaiorCart(self):
        print("Teste de Cliente - fazer pagamento maior do que a carteira.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.fazerPagamento(1000, self.bicletaria1, 2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 11, 00, 00)), -1)

    def testeFazerPagamentoBiciclInval(self):
        print("Teste de Cliente - fazer pagamento com bicicletaria inválida.\n")
        self.cliente1.fazerPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.bicletaria1)
        self.bicletaria1.receberPedidoEmprestimo(2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), self.cliente1)
        self.assertEqual(self.cliente1.fazerPagamento(10, 'string', 2, "HORA", datetime.datetime(2021, 8, 22, 10, 00, 00), datetime.datetime(2021, 8, 22, 11, 00, 00)), -1)

if __name__ == "__main__":
    unittest.main()