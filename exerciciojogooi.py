class Jogo:
    def __init__(self, titulo, genero, classificacao_etaria, lancamento,preco):
        self._titulo = titulo
        self._genero = genero
        self._classificacao_etaria = classificacao_etaria
        self._lancamento = lancamento
        self._preco = preco

    def exibir_detalhes(self):
        print("Titulo:", self._titulo, "\nGênero:", self._genero, "\nClassificação etária:", self._classificacao_etaria, "\nData de lançamento:", self._lancamento, "\nPreço:",self._preco)

    def get_titulo(self):
        print(self._titulo)

    def get_genero(self):
        print(self._genero)
        
    def get_classificacao_etaria(self):
        print(self._classificacao_etaria)

    def get_lancamento(self):
        print(self._lancamento)

    def get_preco(self):
        print(self._preco)

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_genero(self, genero):
        self.genero = genero
        
    def set_classificacao_etaria(self,classificao_etaria):
        self._classificacao_etaria = classificao_etaria

    def set_lancamento(self, lancamento):
        self._lancamento = lancamento

    def set_preco(self, preco):
        self._preco = preco

class Jogador:
    def __init__(self, nickname, id_jogador, saldo_carteira):
        self._nickname = nickname
        self._id_jogador = id_jogador
        self._biblioteca_jogos = []
        self._saldo_carteira = saldo_carteira

    def exibir_perfil(self):
        print(f"Nome de usuário: {self._nickname} \nID jogador: {self._id_jogador} \nJogos na biblioteca: {self._biblioteca_jogos} \nSaldo na carteira: R${self._saldo_carteira}")

    def adicionar_jogo(self, jogo, preco):
        saldo = self._saldo_carteira
        if saldo < preco:
            print("Não foi póssivel efetuar a compra.\nSaldo disponível: ", self._saldo_carteira)
        else:
            saldo = saldo - preco
            self._saldo_carteira = saldo
            print("A compra foi concluida.\n Novo saldo: ", self._saldo_carteira)
            self._biblioteca_jogos.append(jogo)

    def adicionar_saldo(self, quantidade):
        saldo =  self._saldo_carteira
        self._saldo_carteira = saldo + quantidade
    
    #def debitar_saldo(self, preco):
    #    saldo = self._saldo_carteira
    #    if saldo < preco:
    #        print("Não foi póssivel efetuar a compra.\nSaldo disponível: ", self._saldo_carteira)
    #    else:
    #        saldo = saldo - preco
    #        self._saldo_carteira = saldo
    #        print("A compra foi concluida.\n Novo saldo: ", self._saldo_carteira)


    def get_nickname(self):
        print(self._nickname)

    def get_id_jogador(self):
        print(self._id_jogador)
        
    def get_biblioteca_jogos(self):
        print(self._biblioteca_jogos)

    def get_saldo_carteira(self):
        print(self._saldo_carteira)

    def set_nickname(self, nickname):
        self._nickname = nickname

    def set_id_jogador(self, id_jogador):
        self.id_jogador = id_jogador
    
class Plataforma:  
    def __init__(self, nome_plataforma):
        self._nome_plataforma = nome_plataforma
        self._catalogo = []
        self._jogadores_cadastrados = []
    
    def adicionar_jogo(self, jogo):
        self._catalogo.append(jogo)

    def cadastrar_jogador(self, jogador):
        self._jogadores_cadastrados.append(jogador)
    
    def exibir_tudo(self):
        print(f"Jogadores cadastrados: {self._jogadores_cadastrados} \nCatalogo de jogos: {self._catalogo}")

    def proucurar_jogo(self, procura):
        self.procura = procura
        jogo = self._catalogo
        if procura in jogo:
            print("Olha:", procura)
        else:
            print("Não encontrado burro '-'")


    def get_nome_plataforma(self):
        print(self._nome_plataforma)
    
    def get_catalogo(self):
        print(self._catalogo)

    def get_jogadores_cadastrados(self):
        print(self._jogadores_cadastrados)
    
    def set_nome_plataforma(self, nome):
        self._nome = nome




    


biblioteca = Plataforma("Gabriel SKeerrrrr")
biblioteca.exibir_tudo()
biblioteca.adicionar_jogo("Davi kart")
biblioteca.adicionar_jogo("Davi scat")
biblioteca.adicionar_jogo("Davi")
biblioteca.cadastrar_jogador("Fezes games")
biblioteca.exibir_tudo()

biblioteca.proucurar_jogo("oi")



