class Estoque:

    __estoque: list = []
    __codigo: int = 0

    @classmethod
    def relatorio_geral(cls) -> list:
        """Relatório geral dos produtos da despensa, inclusive os zerados"""
        relatorio: list = []
        for x in Estoque.__estoque:
            relatorio.append(x)
        return relatorio

    @classmethod
    def entrada_produto(cls, codigo: int, quantidade: int):
        Estoque.__estoque[codigo][3] += quantidade

    @classmethod
    def retirada_produto(cls, codigo: int, quantidade: int):
        if Estoque.__estoque[codigo][3] >= quantidade:
            Estoque.__estoque[codigo][3] -= quantidade
        else:
            print(f'Não disponibilizamos dessa quantidade do produto {Estoque.__estoque[codigo][0]}')

    @classmethod
    def verificar_zerados(cls):
        """Verifica quais produtos tem 0 unidades no estoque"""
        contagem_zerados = 0
        for x in Estoque.__estoque:
            if x[3] == 0:
                contagem_zerados += 1
                return print(f'O produto {x[0]}, código {x[2]}, está com o estoque zerado')
        if contagem_zerados == 0:
            return print('Não há produtos zerados no estoque')

    @classmethod
    def gravar_arquivo(cls):
        """Grava os produtos num arquivo .txt"""
        with open('despensa.csv', 'w', encoding='UTF-8') as desp:
            desp.write("Nome,Descrição,Código,Quantidade,")
            for x in Estoque.__estoque:
                desp.write("\n")
                for y in x:
                    desp.write(str(y) + ',')


    def __init__(self, nome: str, descricao: str, quantidade: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__codigo = Estoque.__codigo
        self.__quantidade = quantidade
        Estoque.__estoque.append([self.__nome, self.__descricao, self.__codigo, self.__quantidade])
        Estoque.__codigo += 1

    @property
    def nome_e_descricao(self):
        return f'{self.__nome} | {self.__descricao}'

    @property
    def quantidade(self):
        return f'{self.__nome} | Código: {self.__codigo} | Quantidade: {self.__quantidade}'

mesa = Estoque("Mesa", "de vidro 4 cadeiras", 3)
sofa = Estoque("Sofa", "Dois lugares", 2)
geladeira = Estoque("Geladeira", "Duas portas frost-free", 4)
tv = Estoque("TV", "42 polegadas smart", 5)
ventilador = Estoque("Ventilador", "30 cm", 6)

Estoque.gravar_arquivo()