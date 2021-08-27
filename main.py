import datetime
import math

'''
Por orientação do professor, considerei somente duas classes - Loja e Cliente. 
'''

class Bicicletaria(object):
    def __init__(self, estoque, precoHora, precoDia, precoSemana, caixa):

        self.estoque = estoque
        self.precoHora = precoHora
        self.precoDia = precoDia
        self.precoSemana = precoSemana
        self.caixa = caixa

    def receberPedidoEmprestimo(self,quantidade, modalidade, horaInicial, objCliente):
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
            objCliente.horaInicial = horaInicial
            objCliente.modalidade = modalidade
            print (f"Bicicletaria - Pedido de {quantidade} bicicleta(s), alugada(s) por {modalidade}. Empréstimo iniciado em {horaInicial}. Estoque: {self.estoque}.\n")
            return modalidade, self.estoque 
        
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

    def calcularConta (self, quantidade, modalidade, horaInicial, horaDevolucao, objCliente):
        try:
            if quantidade <= 0:
                raise ValueError ("Quantidade inválida.\n")

            if quantidade != objCliente.quantidade:
                raise SystemError ("Quantidade devolvida diferente da emprestada.\n")

            if modalidade != "HORA" and modalidade != "DIA" and modalidade != "SEMANA":
                raise NameError ("Modalidade inválida.\n")
            
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

            if delta <= 0:
                raise ArithmeticError

            self.estoque += quantidade

            '''
            Aqui aplico o deconto 'Família' para locações superiores à 3 bicicletas.
            '''
            if quantidade >= 3:
                valorTotal = round(((delta * preco * quantidade) * 0.7),2)
                print(f"Bicicletaria - O aluguel de {quantidade} bicicleta(s), por {modalidade} teve duração de {delta} {modalidade}(S), com o valor de R${preco} por {modalidade} por bicicleta. Valor total de R$ {valorTotal}, com desconto de 30% por 'Aluguel Família' superior à 3 bicicletas. Estoque: {self.estoque}.\n")
                return valorTotal
            
            valorTotal = delta * preco * quantidade

            print(f"Bicicletaria - O aluguel de {quantidade} bicicleta(s), por {modalidade} teve duração de {delta} {modalidade}(S), com o valor de R${preco} por {modalidade} por bicicleta. Valor total de R$ {valorTotal}. Estoque: {self.estoque}.\n")

            return valorTotal

        except ValueError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) não puderam ser realizados por quantidade inválida. Estoque: {self.estoque}.\n")
            return 0
        except SystemError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) não puderam ser realizados por quantidade diferente da emprestada. Estoque: {self.estoque}.\n")
            return 0
        except NameError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) na modalidade {modalidade} não puderam ser realizados por modalidade inválida. Estoque: {self.estoque}.\n")
            return 0
        except ArithmeticError:
            print(f"Bicicletaria - O cálculo da conta e a devolução da(s) {quantidade} bicicleta(s) na modalidade {modalidade} não puderam ser realizados por horários inválidos. Estoque: {self.estoque}.\n")
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
            return 0
        except:
            print(f"Bicicletaria - Erro ao pagar conta. Recebido R${valorPgto}, conta R${valorTotal}. Caixa: R$ {self.caixa}.\n")
            return 0

class Cliente(object):

    def __init__(self, nome, carteira):
        self.nome = nome
        self.carteira = carteira
        self.quantidade = 0
        self.modalidade = " "
        self.horaInicial = datetime.datetime.now()

    def fazerPedidoEmprestimo(self, quantidadeSolic, modalidade, horaInicial, objBicicletaria):

        
        try:
            if quantidadeSolic <= 0:
                raise ValueError ("Quantidade inválida.\n")
            
            if quantidadeSolic > objBicicletaria.estoque:
                raise SystemError ("Quantidade indisponível.\n")

            if modalidade != "HORA" and modalidade != "DIA" and modalidade != "SEMANA":
                raise NameError ("Modalidade inválida.\n")

            if not isinstance (objBicicletaria, Bicicletaria):
                raise AttributeError ("Não recebeu uma Bicicletaria.\n")

            print(f"Cliente {self.nome} - Pedido de {quantidadeSolic} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial}, feito.\n")
            self.quantidade = quantidadeSolic
            return quantidadeSolic, modalidade, horaInicial

        except ValueError:
            print(f"Cliente {self.nome} - Pedido de {quantidadeSolic} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado por quantidade inválida.\n")
            return 0
        except SystemError:
            print(f"Cliente {self.nome} - Pedido de {quantidadeSolic} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado por estoque indisponível.\n")
            return 0
        except NameError:
            print(f"Cliente {self.nome} - Pedido de {quantidadeSolic} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado por modalidade inválida.\n")
            return 0
        except AttributeError:
            print(f"Cliente {self.nome} - Pedido de {quantidadeSolic} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado. Não recebeu bicicletaria válida.\n")
            return 0
        except:
            print(f"Cliente {self.nome} - Pedido de {quantidadeSolic} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizado.\n")
            return 0

    def devolverEmprestimo(self, quantidadeDevolv, modalidade, horaInicial, horaDevolucao, objBicicletaria):
        try:
            if quantidadeDevolv <= 0:
                raise ValueError ("Quantidade inválida.\n")
            
            if quantidadeDevolv != self.quantidade:
                raise SystemError ("Quantidade devolvida diferente da emprestada.\n")
    
            if modalidade != "HORA" and modalidade != "DIA" and modalidade != "SEMANA":
                raise NameError ("Modalidade inválida.\n")

            if not isinstance (objBicicletaria, Bicicletaria):
                raise AttributeError ("Não recebeu uma Bicicletaria.\n")

            if (horaDevolucao - horaInicial).total_seconds() <= 0:
                raise ArithmeticError ("Horários inválidos.\n")

            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial}, finalizado em {horaDevolucao} com sucesso.\n")
            return horaDevolucao

        except ValueError:
            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizada por quantidade inválida.\n")
            return 0
        except SystemError:
            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizada por quantidade diferente da emprestada.\n")
            return 0
        except NameError:
            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizada por modalidade inválida.\n")
            return 0
        except AttributeError:
            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizada. Não recebeu bicicletaria válida.\n")
            return 0
        except ArithmeticError:
            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizada. Horário de devolução {horaDevolucao} inválido.\n")
            return 0
        except:
            print(f"Cliente {self.nome} - Devolução de {quantidadeDevolv} bicicleta(s), na modalidade {modalidade}, iniciado em {horaInicial} não realizada.\n")
            return 0

    def fazerPagamento(self, valorPgto, objBicicletaria, quantidadeDevolv, modalidade, horaInicial, horaDevolucao):
            try:
                if valorPgto <= 0:
                    raise ValueError("Valor inválido.\n")
                
                if valorPgto > self.carteira:
                    raise ArithmeticError("Pagamento maior que dinheiro disponivel.\n")

                if not isinstance(objBicicletaria, Bicicletaria):
                    raise SystemError("Não recebeu uma bicicletaria.\n")

                valorTotal = objBicicletaria.calcularConta (quantidadeDevolv, modalidade, horaInicial, horaDevolucao, self)
                divida = objBicicletaria.receberPagamento(valorTotal, valorPgto)
                self.carteira -= valorPgto

                if divida == 0:
                    print(f"Cliente {self.nome} - Pagamento exato de R${valorPgto} da conta de R${valorTotal}. Carteira: R$ {self.carteira}.\n")
                    valorTotal = 0

                elif divida > 0:
                    print(f"Cliente {self.nome} - Pagamento parcial de R${valorPgto} da conta de R${valorTotal}. Restam R${divida} para pagar. Carteira: R$ {self.carteira}.\n")
                    valorTotal = divida

                else:
                    self.carteira -= divida
                    print(f"Cliente {self.nome} - Pagamento de R${valorPgto} da conta de R${valorTotal} com troco de R${-divida}. Carteira: R$ {self.carteira}.\n")
                    valorTotal = 0

                return self.carteira

            except ValueError:
                print(f"Cliente {self.nome} - Pagamento de R${valorPgto} não foi efetuado, pois o valor de pagamento não é válido. Carteira: R$ {self.carteira}.\n")    
                return -1
            except ArithmeticError:
                print(f"Cliente {self.nome} - Pagamento de R${valorPgto} não foi efetuado, pois o valor de pagamento é maior do que disponível na carteira. Carteira: R$ {self.carteira}.\n")    
                return -1
            except SystemError:
                print(f"Cliente {self.nome} - Pagamento de R${valorPgto} não foi efetuado, pois não recebeu bicicletaria. Carteira: R$ {self.carteira}.\n")    
                return -1
            except:
                print(f"Cliente {self.nome} - Pagamento de R${valorPgto}. Carteira: R$ {self.carteira}.\n")    
                return -1