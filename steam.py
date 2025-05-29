class Jogo:
    def __init__(self, titulo, genero, classificacao_etaria, lancamento,preco):
        self._titulo = titulo
        self._genero = genero
        self._classificacao_etaria = classificacao_etaria
        self._lancamento = lancamento
        self._preco = preco

    def exibir_detalhes(self):
        print("\nTitulo:", self._titulo, "\nGênero:", self._genero, "\nClassificação etária:", self._classificacao_etaria, "\nData de lançamento:", self._lancamento, "\nPreço:","R$",self._preco)

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
        print(f"Nome de usuário: {self._nickname} \nID jogador: {self._id_jogador}")
        print("Jogos na biblioteca:")
        for jogo in self._biblioteca_jogos:
            jogo.exibir_detalhes()
            print()
        print(f"Saldo na carteira: R${self._saldo_carteira}")

    def adicionar_jogo(self, jogo, preco):
        saldo = self._saldo_carteira
        if saldo < preco:
            print("Não foi póssivel efetuar a compra.\nSaldo disponível: ", self._saldo_carteira)
        else:
            saldo = saldo - preco
            self._saldo_carteira = saldo
            print("A compra foi concluida.\nNovo saldo: ", self._saldo_carteira)
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
    
    def adicionar_jogo(self, *jogos):
        for jogo in jogos:
            self._catalogo.append(jogo)

    def comprar_jogo(self, comprador, jogo_desejado):
        if comprador not in self._jogadores_cadastrados:
            print(f"Erro: Jogador '{comprador._nickname}' não está cadastrado.")
            return
        if jogo_desejado not in self._catalogo:
            print(f"Erro: Jogo '{jogo_desejado._titulo}' não está disponível.")
            return
        if comprador._saldo_carteira >= jogo_desejado._preco:
            comprador._saldo_carteira -= jogo_desejado._preco
            comprador._biblioteca_jogos.append(jogo_desejado)
            print(f"Compra realizada! '{jogo_desejado._titulo}' foi adicionado à biblioteca de {comprador._nickname}.")
        else:
            print(f"Saldo insuficiente. Preço do jogo: R${jogo_desejado._preco}")


    def cadastrar_jogador(self, jogador):
        self._jogadores_cadastrados.append(jogador)
    
    def exibir_tudo(self):
        print("\n--- Jogadores Cadastrados ---")
        for jogador in self._jogadores_cadastrados:
            print(f"Nickname: {jogador._nickname}, ID: {jogador._id_jogador}, Saldo: R${jogador._saldo_carteira}")
        
        print("\n--- Catálogo de Jogos ---")
        for jogo in self._catalogo:
            jogo.exibir_detalhes()
            print("----------------------")

    def proucurar_jogo(self, procura):
        self.procura = procura
        jogo = self._catalogo
        if procura in jogo:
            print("jogo está no catalogo")
        else:
            print("Não encontrado burro '-'")
    
    def proucurar_jogador(self, procura):
        self.procura = procura
        player = self._jogadores_cadastrados
        if procura in player:
            print("Usuário encontrado: ", player)
        else:
            print("Burro não encontrado")

    def listar_jogos_catalogo(self):
        catalogo = self._catalogo
        print("-----------")
        for jogo in catalogo:
            jogo.exibir_detalhes()
            print("-----------")

    def get_nome_plataforma(self):
        print(self._nome_plataforma)
    
    def get_catalogo(self):
        print(self._catalogo)

    def get_jogadores_cadastrados(self):
        print(self._jogadores_cadastrados)
    
    def set_nome_plataforma(self, nome):
        self._nome = nome

caua = Plataforma("oi")
dudu = Jogador("dukko","#dudu",2000.0)
caua2 = Jogador("tobirama", "#tobi", 2000.0)
jogo = Jogo("bobo", "ação", "18+", 2018, 200)
jogo2 = Jogo("bobo esponja", "puzzle", "18+", 2020,230)

caua.cadastrar_jogador(dudu)
caua.cadastrar_jogador(caua2)
caua.adicionar_jogo(jogo,jogo2)

dudu.exibir_perfil()
caua.comprar_jogo(dudu, jogo)
caua.comprar_jogo(caua2,jogo2)
dudu.exibir_perfil()
caua2.exibir_perfil()