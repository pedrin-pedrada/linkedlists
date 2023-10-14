class Estrutura:  # classse base para montar a estrura dos dados
    def __init__(self):
        self.info = None  # referência das classes abaixo (como * em C)
        self.ant = None  # Nodo - referencia anterior (como * em C)
        self.prox = None  # Nodo - proxima referencia (como * em C)


class Emissor:
    def __init__(self):
        self.id_emissor = None  # int
        self.nome_emissor = None  # str


class Receptor:
    def __init__(self):
        self.id_receptor = None  # int
        self.nome_receptor = None  # str


class Mensagem:
    def __init__(self):
        self.id_emissor = None  # int - id do emissor da mensagem (não é referência *)
        self.mensagem = None  # str


class ListaMensagem:
    def __init__(self):
        self.id_receptor = None  # int - id do receptor da lista (não é referência *)
        self.inicio_mensagem = None  # Nodo - inicio da lista com as mensagens


class Header:
    def __init__(self):
        self.inicio_emissor = None  # Nodo - inicio da lista com os emissores
        self.inicio_receptor = None  # Nodo - inicio da lista com os receptores
        self.inicio_lista_mensagem = None  # Nodo - inicio da lista com as listas de mensagens


def mostrar_estrutura(inicio):
    aux = inicio
    while aux is not None:
        print(aux.info)
        aux = aux.prox


def mostrar_estrutura_inverso(inicio):
    aux = inicio
    while aux.prox is not None:
        aux = aux.prox

    while aux is not None:
        print(aux.info)
        aux = aux.ant


def incluir_emissor(nome_emissor):
    aux = header.inicio_emissor
    maior_id = 0
    while aux is not None:
        if aux.info.id_emissor >= maior_id:
            maior_id = aux.info.id_emissor + 1
        aux = aux.prox

    novo_emissor = Emissor()
    novo_emissor.id_emissor = maior_id
    novo_emissor.nome_emissor = nome_emissor
    nova_estrutura = Estrutura()
    nova_estrutura.info = novo_emissor

    if header.inicio_emissor is None:
        header.inicio_emissor = nova_estrutura
    else:
        aux = header.inicio_emissor
        while aux.prox is not None:
            aux = aux.prox

        aux.prox = nova_estrutura
        nova_estrutura.ant = aux


def remover_emissor(id_deletar):
    aux = header.inicio_emissor

    if header.inicio_emissor is None:
        print('Nenhum emissor cadastrado')
        return

    success = False
    if header.inicio_emissor.info.id_emissor == id_deletar:
        header.inicio_emissor = header.inicio_emissor.prox
        success = True

    else:
        while aux is not None:
            if aux.info.id_emissor == id_deletar:
                aux.ant.prox = aux.prox

                if aux.prox is not None:
                    aux.prox.ant = aux.ant

                success = True
                break
            aux = aux.prox

    if success:
        print('Emissor deletado:')
        print(f'\t{aux.info.id_emissor} - {aux.info.nome_emissor}')
        del aux
    else:
        print(f'Nenhum emissor foi encontrado com o id "{id_deletar}"')


def consultar_emissores():
    # escrever na tela os emissores cadastrados
    aux = header.inicio_emissor
    print('Emissores:')
    print(f'\tid_emissor - nome_emissor')
    while aux is not None:
        print(f'\t{aux.info.id_emissor} - {aux.info.nome_emissor}')
        aux = aux.prox


def incluir_receptor():
    pass


def remover_receptor():
    # quando o receptor é removido, sua fila de mensagens também é removida
    pass


def consultar_receptores():
    # escrever na tela os receptores cadastrados
    pass


def enviar_mensagem():
    # um receptor cadastrado escreve a mensagem, e define quais são os receptores (pelo menos um receptor). a
    # mensagem é enfileirada na fila de cada receptor.
    pass


def retira_mensagem():
    # um receptor cadastrado desenfileira uma mensagem (apresentar mensagem de erro se a fila está vazia)
    pass


def consultar_fila_mensagens():
    # exibe a fila de mensagens de um receptor
    pass


def outras_operacoes():
    # como exibir receptores com fila vazia, exibir receptores com mais mensagens na fila, exibir total de mensagens
    # enviadas por um emissor, exibir total de mensagens recebidas por um recepto
    pass


header = Header()

if __name__ == "__main__":
    # emissor = Emissor()
    # inicio_emissor = Estrutura()
    # inicio_emissor.info = emissor
    #
    # receptor = Receptor()
    # inicio_receptor = Estrutura()
    # inicio_receptor.info = receptor
    #
    # mensagem = Mensagem()
    # inicio_mensagem = Estrutura()
    # inicio_mensagem.info = mensagem
    #
    # lista_mensagem = ListaMensagem()
    # inicio_lista_mensagem = Estrutura()
    # inicio_lista_mensagem.info = lista_mensagem
    #
    # lista_mensagem.inicio_mensagem = inicio_mensagem
    #
    # header.inicio_emissor = inicio_emissor
    # header.inicio_receptor = inicio_receptor
    # header.inicio_lista_mensagem = inicio_lista_mensagem

    incluir_emissor('Pedro')
    incluir_emissor('Joao')
    incluir_emissor('Gabriel')
    incluir_emissor('Josias')
    consultar_emissores()
    remover_emissor(0)
    consultar_emissores()

    # mostrar_estrutura(header.inicio_emissor)
    print()
    # mostrar_estrutura_inverso(header.inicio_emissor)

    # novo = Estrutura()
    # novo2 = Estrutura()
    # novo3 = Estrutura()
    # novo4 = Estrutura()
    #
    # novo.info = 1
    # novo2.info = 2
    # novo3.info = 3
    # novo4.info = 4
    #
    # novo.prox = novo2
    # novo2.prox = novo3
    # novo3.prox = novo4
    #
    # novo2.ant = novo
    # novo3.ant = novo2
    # novo4.ant = novo3
    #
    # mostrar_estrutura(novo)
    # print()
    # mostrar_estrutura_inverso(novo)

    # print('novo:', novo.info)
    # print('novo.prox.info:', novo.prox.info)
    # print('novo2:', novo2.info)
    # print('novo2.ant.info:', novo2.ant.info)