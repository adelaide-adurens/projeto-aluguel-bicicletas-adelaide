import datetime
import math

'''
Por orientação do professor, considerei somente duas classes - Loja e Cliente. 
Por isso, alguns atributos do empréstimo estão dados à loja.
'''

class Bicicletaria(object):
    def __init__(self, estoque, precoHora, precoDia, precoSemana, caixa):

        self.estoque = estoque
        self.precoHora = precoHora
        self.precoDia = precoDia
        self.precoSemana = precoSemana
        self.caixa = caixa
        self.modalidade = " "
        self.horaInicial = datetime.datetime.now()

    def receberPedidoEmprestimo(self,quantidade, modalidade, horaInicial):
        try:
            if quantidade <= 0:
                raise ValueError ("Quantidade inválida.\n")

            if quantidade > self.estoque:
                raise SystemError ("Estoque Indisponível.\n")
            
            '''
            Existe no escopo do projeto um desconto para locações acima de 3 bicicletas.
            O tratamento dessa regra será dado no módulo de Calcular a conta.
            '''

            if modalidade != "HORA" and modalidade != "DIA" and modalidade != "SEMANA":
                raise NameError ("Modalidade inválida.\n")

            self.estoque -= quantidade
            self.horaInicial = horaInicial
            self.modalidade = modalidade
            print (f"Bicicletaria - Pedido de {quantidade} bicicleta(s), alugada(s) por {modalidade}. Empréstimo iniciado em {self.horaInicial}. Estoque: {self.estoque}.\n")
            return self.modalidade, self.estoque 
        
        except ValueError:
            print(f"Bicicletaria - Pedido de {quantidade} bicicleta(s), alugada(s) por {modalidade} não efetuado por quantidade invalida. Estoque: {self.estoque}.\n")
            return 0
        except SystemError:
            print(f"Bicicletaria - Pedido de {quantidade} bicicleta(s), alugada(s) por {modalidade} não efetuado por falta de estoque. Estoque: {self.estoque}.\n")
            return 0
        except NameError:
            print(f"Bicicletaria - Pedido de {quantidade} bicicleta(s), alugada(s) por {modalidade} não efetuado por modalidade invalida. Estoque: {self.estoque}.\n")
            return 0
        except:
            print(f"Bicicletaria - Pedido de {quantidade} bicicleta(s), alugada(s) por {modalidade} não efetuado. Estoque: {self.estoque}.\n")
            return 0

    def calcularConta (self, quantidade, modalidade, horaInicial, horaDevolucao):
        try:
            if quantidade <= 0:
                raise ValueError ("Quantidade inválida.\n")

            if self.estoque + quantidade > 20:
                raise SystemError ("Quantidade devovlida superior à emprestada.\n")

            if modalidade != "HORA" and modalidade != "DIA" and modalidade != "SEMANA":
                raise NameError ("Modalidade inválida.\n")
            
            self.estoque += quantidade

            '''
            Estou sempre arredondando para cima os períodos de locação.
            '''

            if modalidade == "HORA":
                preco = self.precoHora
                delta = math.ceil((horaDevolucao - horaInicial).total_seconds()/3600)
            if modalidade == "DIA":
                preco = self.precoDia
                delta = math.ceil((horaDevolucao - horaInicial).total_seconds()/86400)
            if modalidade == "SEMANA":
                preco = self.precoSemana
                delta = math.ceil((horaDevolucao - horaInicial).total_seconds()/604800)

            '''
            Aqui aplico o deconto 'Família' para locações superiores à 3 bicicletas.
            '''
            if quantidade >= 3:
                valorTotal = (delta * preco * quantidade) * 0.7
                print(f"Bicicletaria - O aluguel de {quantidade} bicicleta(s), por {modalidade} teve duração de {delta} {modalidade}(S), com o valor de R${preco} por {modalidade}. Valor total de R$ {valorTotal}, com desconto de 30% por 'Aluguel Família' superior à 3 bicicletas. Estoque: {self.estoque}.\n")
                return valorTotal
            
            valorTotal = delta * preco * quantidade

            print(f"Bicicletaria - O aluguel de {quantidade} bicicleta(s), por {modalidade} teve duração de {delta} {modalidade}(S), com o valor de R${preco} por {modalidade}. Valor total de R$ {valorTotal}. Estoque: {self.estoque}.\n")

            return valorTotal

        except ValueError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) não puderam ser realizados por quantidade inválida. Estoque: {self.estoque}.\n")
            return 0
        except SystemError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) não puderam ser realizados por quantidade superior à emprestada. Estoque: {self.estoque}.\n")
            return 0
        except NameError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) na modalidade {modalidade} não puderam ser realizados por modalidade inválida. Estoque: {self.estoque}.\n")
            return 0
        except:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) bicicleta(s) não puderam ser realizados. Estoque: {self.estoque}.\n")
            return 0

    def receberPagamento(self, valorTotal, valorPgto):
        try:
            if valorTotal <= 0 or valorPgto <= 0:
                raise ValueError("Valor(es) inválido(s).\n")

            if valorTotal == valorPgto:
                self.caixa+= valorPgto
                print(f"Bicicletaria - Conta paga totalmente, recebido R${valorPgto}, conta R${valorTotal}. Caixa: R${self.caixa}.\n")
                return 0

            elif valorTotal < valorPgto:
                self.caixa += valorTotal
                print(f"Bicicletaria - Conta paga totalmente, com troco de R${valorPgto - valorTotal}. Recebido R${valorPgto}, conta R${valorTotal}. Caixa: R$ {self.caixa}.\n")
                return -(valorPgto -  valorTotal)

            else:
                self.caixa += valorPgto
                print(f"Bicicletaria - Conta paga parcialmente, restam R${valorTotal - valorPgto}. Recebido R${valorPgto}, conta R${valorTotal}. Caixa: R$ {self.caixa}.\n")
                return valorTotal - valorPgto

        except ValueError:
            print(f"Bicicletaria - Erro ao pagar conta. Valor(es)inválido(s). Recebido R${valorPgto}, conta R${valorTotal}. Caixa: R$ {self.caixa}.\n")
            return valorTotal
        except:
            print(f"Bicicletaria - Erro ao pagar conta. Recebido R${valorPgto}, conta R${valorTotal}. Caixa: R$ {self.caixa}.\n")
            return valorTotal



class Cliente(object):

    def __init__(self, nome, carteira):
        self.nome = nome
        self.carteira = carteira
        self.conta = 0

    def fazerPedidoEmprestimo(self, quantidade, modalidade, horaInicial, objBicicletaria):

        estoque = objBicicletaria.estoque
        try:
            if quantidade <= 0:
                raise ValueError ("Quantidade inválida.\n")
            
            if quantidade > estoque:
                raise SystemError ("Quantidade indisponível.\n")

            if modalidade != "HORA" and modalidade != "DIA" and modalidade != "SEMANA":
                raise NameError ("Modalidade inválida.\n")

            if not isinstance (objBicicletaria, Bicicletaria):
                raise TypeError ("Não recebeu uma Bicicletaria.\n")

            print(f"Cliente {self.nome} - Pedido de {quantidade} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial}, feito.\n")
            return quantidade, modalidade, horaInicial

        except ValueError:
            print(f"Cliente {self.nome} - Pedido de {quantidade} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado por quantidade inválida.\n")
            return 0
        except SystemError:
            print(f"Cliente {self.nome} - Pedido de {quantidade} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado por quantidade indisponível.\n")
            return 0
        except NameError:
            print(f"Cliente {self.nome} - Pedido de {quantidade} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado por modalidade inválida.\n")
            return 0
        except TypeError:
            print(f"Cliente {self.nome} - Pedido de {quantidade} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado. Não recebeu bicicletaria válida.\n")
            return 0
        except:
            print(f"Cliente {self.nome} - Pedido de {quantidade} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado.\n")
            return 0

    def devolverEmprestimo(self, quantidade, modalidade, horaInicial, horaDevolucao, objBicicletaria):
        pass

    def fazerPagamento(self, valroPgto, objSorveteria):
        pass