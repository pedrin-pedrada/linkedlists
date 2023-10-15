class Estrutura:  # classse base para montar a estrura dos dados
    def __init__(self):
        self.info = None  # referência das classes abaixo (como * em C)
        # self.ant = None  # Estrutura - referencia anterior (como * em C)
        self.prox = None  # Estrutura - proxima referencia (como * em C)


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


class ListaComunicacao:
    def __init__(self):
        self.id_receptor = None  # int - id do receptor da lista (não é referência *)
        self.inicio_mensagem = None  # Nodo - inicio da lista com as mensagens


class Header:
    def __init__(self):
        self.inicio_emissor = None  # Estrutura - inicio da lista com os emissores
        self.inicio_receptor = None  # Estrutura - inicio da lista com os receptores
        self.inicio_lista_comunicacao = None  # Estrutura - inicio da lista com as listas de mensagens


def mostrar_estrutura(inicio):
    aux = inicio
    while aux is not None:
        print(aux.info)
        aux = aux.prox


def mostrar_estrutura_inverso(inicio):
    aux = inicio
    while aux.prox is not None:
        aux = aux.prox


def incluir_emissor(nome_emissor):
    aux = header.inicio_emissor
    maior_id = 1
    while aux is not None:
        if aux.info.id_emissor >= maior_id:
            maior_id = aux.info.id_emissor + 1
        aux = aux.prox

    novo_emissor = Emissor()
    novo_emissor.id_emissor = maior_id
    novo_emissor.nome_emissor = nome_emissor

    nova_estrutura = Estrutura()
    nova_estrutura.info = novo_emissor

    nova_estrutura.prox = header.inicio_emissor
    header.inicio_emissor = nova_estrutura


def remover_emissor(id_emissor):
    if header.inicio_emissor is None:
        print('Nenhum emissor cadastrado')
        return

    aux = header.inicio_emissor
    success = False

    if header.inicio_emissor.info.id_emissor == id_emissor:
        header.inicio_emissor = header.inicio_emissor.prox
        success = True

    else:
        anterior = None
        while aux is not None:
            if aux.info.id_emissor == id_emissor:
                anterior.prox = aux.prox
                success = True
                break

            anterior = aux
            aux = aux.prox

    if success:
        print('Emissor deletado:')
        print(f'\t{aux.info.id_emissor} - {aux.info.nome_emissor}')
    else:
        print(f'Nenhum emissor foi encontrado com o id "{id_emissor}"')


def consultar_emissores():
    # escrever na tela os emissores cadastrados
    aux = header.inicio_emissor
    print('Emissores:')
    print(f'\tid_emissor - nome_emissor')
    while aux is not None:
        print(f'\t{aux.info.id_emissor} - {aux.info.nome_emissor}')
        aux = aux.prox


def valida_emissor(id_emissor):
    # retorna True ou False se existir um emissor com o id informado
    aux = header.inicio_emissor
    while aux is not None:
        if aux.info.id_emissor == id_emissor:
            return True
        aux = aux.prox
    return False


def incluir_receptor(nome_receptor):
    aux = header.inicio_receptor
    maior_id = 1
    while aux is not None:
        if aux.info.id_receptor >= maior_id:
            maior_id = aux.info.id_receptor + 1
        aux = aux.prox

    novo_receptor = Receptor()
    novo_receptor.id_receptor = maior_id
    novo_receptor.nome_receptor = nome_receptor

    nova_estrutura = Estrutura()
    nova_estrutura.info = novo_receptor

    nova_estrutura.prox = header.inicio_receptor
    header.inicio_receptor = nova_estrutura


def remover_receptor(id_receptor):
    # quando o receptor é removido, sua fila de mensagens também é removida
    if header.inicio_receptor is None:
        print('Nenhum receptor cadastrado')
        return

    aux = header.inicio_receptor
    success = False

    if header.inicio_receptor.info.id_receptor == id_receptor:
        header.inicio_receptor = header.inicio_receptor.prox
        success = True

    else:
        anterior = None
        while aux is not None:
            if aux.info.id_receptor == id_receptor:
                anterior.prox = aux.prox
                success = True
                break

            anterior = aux
            aux = aux.prox

    if success:
        print('Receptor deletado:')
        print(f'\t{aux.info.id_receptor} - {aux.info.nome_receptor}')
        remover_lista_comunicacao(id_receptor)

    else:
        print(f'Nenhum receptor foi encontrado com o id "{id_receptor}"')

    print("\tAinda não finalizado")


def consultar_receptores():
    # escrever na tela os receptores cadastrados
    aux = header.inicio_receptor
    print('Receptores:')
    print(f'\tid_receptor - nome_receptor')
    while aux is not None:
        print(f'\t{aux.info.id_receptor} - {aux.info.nome_receptor}')
        aux = aux.prox


def valida_receptor(id_receptor):
    # retorna True ou False se existir um receptor com o id informado
    aux = header.inicio_receptor
    while aux is not None:
        if aux.info.id_receptor == id_receptor:
            return True
        aux = aux.prox
    return False


def enviar_mensagem(id_emissor, id_receptor, mensagem):
    # um emissor cadastrado escreve a mensagem,
    # define quais são os receptores (pelo menos um receptor). a
    # mensagem é enfileirada na fila de cada receptor.
    existe_emissor = valida_emissor(id_emissor)
    existe_receptor = valida_receptor(id_receptor)

    if not existe_emissor or not existe_receptor:
        print("A mensagem não foi adicionada pois os emissores ou receptores informados não existem")
        return

    nova_mensagem = Mensagem()
    nova_mensagem.id_emissor = id_emissor
    nova_mensagem.mensagem = mensagem

    nova_estrutura = Estrutura()
    nova_estrutura.info = nova_mensagem

    aux = header.inicio_lista_comunicacao
    while aux is not None:
        if aux.info.id_receptor == id_receptor:  # existe lista do receptor -> enfileirar
            aux_mensagem = aux.info.inicio_mensagem
            while aux_mensagem.prox is not None:
                aux_mensagem = aux_mensagem.prox
            aux_mensagem.prox = nova_estrutura  # adiociona na ult posicao

            print("Mensagem adicionada na lista existente")
            return

        aux = aux.prox

    nova_lista_comunicacao = ListaComunicacao()
    nova_lista_comunicacao.id_receptor = id_receptor
    nova_lista_comunicacao.inicio_mensagem = nova_estrutura
    print("Uma nova lista de comunicacao foi criada")

    nova_estrutura_lista_comunicacao = Estrutura()
    nova_estrutura_lista_comunicacao.info = nova_lista_comunicacao

    nova_estrutura_lista_comunicacao.prox = header.inicio_lista_comunicacao
    header.inicio_lista_comunicacao = nova_estrutura_lista_comunicacao

    print("Mensagem adicionada")


def retira_mensagem(id_receptor):
    # um receptor cadastrado desenfileira uma mensagem
    # (apresentar mensagem de erro se a fila está vazia)
    print(f'Mensagem para o receptor "{id_receptor}":')

    existe_mensagem = False
    aux = header.inicio_lista_comunicacao
    while aux is not None:
        if aux.info.id_receptor == id_receptor:  # existe lista do receptor
            print(f'\tid_emissor - mensagem')

            if aux.info.inicio_mensagem is not None:
                print(f'\t{aux.info.inicio_mensagem.info.id_emissor} - {aux.info.inicio_mensagem.info.mensagem}')
                aux.info.inicio_mensagem = aux.info.inicio_mensagem.prox
                existe_mensagem = True

        aux = aux.prox

    if not existe_mensagem:
        print('Nenhuma mensagem cadastrada')


def consultar_fila_comunicacao(id_receptor):
    # exibe a fila de mensagens de um receptor
    print(f'Mensagens na fila do receptor "{id_receptor}":')

    existe_mensagem = False
    aux = header.inicio_lista_comunicacao
    while aux is not None:
        if aux.info.id_receptor == id_receptor:  # existe lista do receptor -> enfileirar
            aux_mensagem = aux.info.inicio_mensagem
            print(f'\tid_emissor - mensagem')

            while aux_mensagem is not None:
                print(f'\t{aux_mensagem.info.id_emissor} - {aux_mensagem.info.mensagem}')
                aux_mensagem = aux_mensagem.prox
                existe_mensagem = True

        aux = aux.prox

    if not existe_mensagem:
        print('Nenhuma mensagem na fila do receptor')


def remover_lista_comunicacao(id_receptor):
    # quando o receptor é removido, sua fila de mensagens também é removida
    if header.inicio_lista_comunicacao is None:
        return

    aux = header.inicio_lista_comunicacao
    success = False

    if header.inicio_lista_comunicacao.info.id_receptor == id_receptor:
        header.inicio_lista_comunicacao = header.inicio_lista_comunicacao.prox
        success = True

    else:
        anterior = None
        while aux is not None:
            if aux.info.id_receptor == id_receptor:
                anterior.prox = aux.prox
                success = True
                break

            anterior = aux
            aux = aux.prox

    if success:
        print(f'Lista de comunicacao do receptor "{id_receptor}" deletada')
    else:
        print(f'Nenhuma lista de comunicacao foi encontrado com o receptor "{id_receptor}"')


def outras_operacoes():
    # como exibir receptores com fila vazia,
    # exibir receptores com mais mensagens na fila,
    # exibir total de mensagens
    # enviadas por um emissor,
    # exibir total de mensagens recebidas por um recepto
    pass


header = Header()

if __name__ == "__main__":

    incluir_emissor('Ana')

    incluir_emissor('Pedro')
    incluir_emissor('Bárbara')
    incluir_emissor('Joao')
    incluir_emissor('Josias')
    incluir_emissor('Helena')
    consultar_emissores()
    # remover_emissor(1)
    consultar_emissores()

    print()
    print()

    incluir_receptor('Joao')
    incluir_receptor('Carlos')
    incluir_receptor('Roberto')
    incluir_receptor('Natasha')
    incluir_receptor('Smirnoff')
    incluir_receptor('Absolut')
    consultar_receptores()
    # remover_receptor(1)
    consultar_receptores()

    print()
    print()

    enviar_mensagem(1, 1, 'Bom dia')
    enviar_mensagem(4, 1, 'Boa tarde')
    enviar_mensagem(2, 0, 'Boa Noite')
    enviar_mensagem(2, 1, 'Boa Noite')
    enviar_mensagem(2, 2, 'Boa Noite')

    print()
    print()
    consultar_fila_comunicacao(0)
    print()
    consultar_fila_comunicacao(1)
    print()
    consultar_fila_comunicacao(2)
    print()
    print()
    retira_mensagem(1)
    print()
    consultar_fila_comunicacao(1)
    print()
    remover_lista_comunicacao(2)
    print()
    consultar_fila_comunicacao(2)

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

    # mostrar_estrutura(header.inicio_emissor)
    # print()
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
    #
    # mostrar_estrutura(novo)
    # print()
    # mostrar_estrutura_inverso(novo)

    # print('novo:', novo.info)
    # print('novo.prox.info:', novo.prox.info)
    # print('novo2:', novo2.info)
