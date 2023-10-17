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
    print('\033[92m', end="")

    aux = header.inicio_emissor
    qtd = 0
    print('Emissores:')
    if header.inicio_emissor is None:
        print("\tNenhum emissor cadastrado")

    else:
        print(f'\tid_emissor - nome_emissor')
        while aux is not None:
            print(f'\t{aux.info.id_emissor} - {aux.info.nome_emissor}')
            aux = aux.prox
            qtd += 1

    print('\033[0m', end="")
    return qtd


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


def consultar_receptores():
    # escrever na tela os receptores cadastrados
    print('\033[93m', end="")
    aux = header.inicio_receptor
    print('Receptores:')
    qtd = 0

    if header.inicio_receptor is None:
        print('\tNenhum receptor cadastrado')
    else:
        print(f'\tid_receptor - nome_receptor')
        while aux is not None:
            print(f'\t{aux.info.id_receptor} - {aux.info.nome_receptor}')
            aux = aux.prox
            qtd += 1

    print('\033[0m', end="")
    return qtd


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

    qtd = consulta_qtd_mensagens(id_receptor)
    if qtd:
        aux = header.inicio_lista_comunicacao
        while aux is not None:
            if aux.info.id_receptor == id_receptor:  # existe lista do receptor
                print(f'\tid_emissor - mensagem')

                if aux.info.inicio_mensagem is not None:
                    print(f'\t{aux.info.inicio_mensagem.info.id_emissor} - {aux.info.inicio_mensagem.info.mensagem}')
                    aux.info.inicio_mensagem = aux.info.inicio_mensagem.prox

            aux = aux.prox

        if qtd-1 > 0:
            print(f'Ainda existem "{qtd-1}" mensagens na fila')
        else:
            print("Todas mensagens foram retiradas")

    else:
        print('Nenhuma mensagem cadastrada')


def consultar_lista_comunicacao(id_receptor):
    # exibe a fila de mensagens de um receptor
    print('\033[94m', end="")
    print(f'Mensagens na fila do receptor "{id_receptor}":')

    print(f'"{consulta_qtd_mensagens(id_receptor)}" mensagens na fila')

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

    print('\033[0m', end="")


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


def consulta_qtd_mensagens(id_receptor):
    # exibe a fila de mensagens de um receptor
    qtd = 0
    aux = header.inicio_lista_comunicacao
    while aux is not None:
        if aux.info.id_receptor == id_receptor:  # existe lista do receptor -> enfileirar
            aux_mensagem = aux.info.inicio_mensagem

            while aux_mensagem is not None:
                aux_mensagem = aux_mensagem.prox
                qtd += 1

        aux = aux.prox

    return qtd


def inicia_interface():
    print('Bem Vindo!')
    print("Trabalho 1 - Algorítimos e Estrutura de Dados")
    print("Grupo: Bárbara Schneider e Pedro Schneider")
    while True:
        print('\033[1m', end='')
        print('\033[96m'+'================= Menu =================')
        print('\033[92m'+'\t1'+'\033[0m'+' - Emissores')
        print('\033[93m'+'\t2'+'\033[0m'+' - Receptores')
        print('\033[94m'+'\t3'+'\033[0m'+' - Mensagens')
        print('\033[91m'+'\t0'+'\033[0m'+' - Sair')
        print()
        print('\033[96m'+'========================================')
        print('\033[0m', end='')
        print('Selecione uma opção:')
        resposta = input()
        print()

        match resposta:  # EMISSORES
            case '1':
                print('\033[92m' + '1' + '\033[0m' + ' - Emissores')
                while True:
                    print('\033[1m', end='')
                    print('\033[96m' + '================= Menu =================')
                    print('\033[92m'+'\tEmissores'+'\033[0m')
                    print('\t1 - Cadastrar emissor')
                    print('\t2 - Remover emissor')
                    print('\t3 - Consultar emissores')
                    print('\033[91m'+'\t0'+'\033[0m'+' - Voltar')
                    print()
                    print('\033[96m' + '========================================')
                    print('\033[0m', end='')
                    print('Selecione uma opção:')
                    resposta = input()
                    print()

                    match resposta:
                        case '1':
                            print('\033[1m', end='')
                            print('1 - Cadastrar emissor')
                            print('Insira o nome do emissor:')
                            print('\033[0m', end='')
                            resposta = input()
                            print()
                            incluir_emissor(resposta)

                        case '2':
                            print('\033[1m', end='')
                            print('2 - Remover emissor')
                            qtd = consultar_emissores()
                            print()
                            if qtd:
                                print('Insira o id do emissor que deseja remover:')
                            else:
                                continue

                            print('\033[0m', end='')
                            resposta = input()
                            print()

                            try:
                                resposta = int(resposta)
                            except ValueError:
                                print("Id inválido, não foi possível remover")
                                continue

                            remover_emissor(resposta)

                        case '3':
                            print('\033[1m', end='')
                            print('3 - Consultar emissores')
                            consultar_emissores()
                            print()
                            print('\033[0m', end='')

                        case '0':
                            print('\033[91m' + '0' + '\033[0m' + ' - Voltar')
                            print('Voltando para o menu...')
                            break

                        case _:
                            print(f'"{resposta}" não é uma opção válida')

            case '2':  # RECEPTORES
                print('\033[93m' + '2' + '\033[0m' + ' - Receptores')
                while True:
                    print('\033[1m', end='')
                    print('\033[96m' + '================= Menu =================')
                    print('\033[93m'+'\tReceptor'+'\033[0m')
                    print('\t1 - Cadastrar receptor')
                    print('\t2 - Remover receptor')
                    print('\t3 - Consultar receptores')
                    print('\033[91m'+'\t0'+'\033[0m'+' - Voltar')
                    print()
                    print('\033[96m' + '========================================')
                    print('\033[0m', end='')
                    print('Selecione uma opção:')
                    resposta = input()
                    print()

                    match resposta:
                        case '1':
                            print('\033[1m', end='')
                            print('1 - Cadastrar receptor')
                            print('Insira o nome do receptor:')
                            print('\033[0m', end='')
                            resposta = input()
                            print()
                            incluir_receptor(resposta)

                        case '2':
                            print('\033[1m', end='')
                            print('2 - Remover receptor')
                            qtd = consultar_receptores()
                            print()
                            if qtd:
                                print('Insira o id do receptor que deseja remover:')
                            else:
                                continue

                            print('\033[0m', end='')
                            resposta = input()
                            print()

                            try:
                                resposta = int(resposta)
                            except ValueError:
                                print("Id inválido, não foi possível remover")
                                continue

                            remover_receptor(resposta)

                        case '3':
                            print('\033[1m', end='')
                            print('3 - Consultar receptores')
                            consultar_receptores()
                            print()
                            print('\033[0m', end='')

                        case '0':
                            print('\033[91m' + '0' + '\033[0m' + ' - Voltar')
                            print('Voltando para o menu...')
                            break

                        case _:
                            print(f'"{resposta}" não é uma opção válida')

            case '3':  # MENSAGENS
                print('\033[94m' + '3' + '\033[0m' + ' - Mensagens')
                while True:
                    print('\033[1m', end='')
                    print('\033[96m' + '================= Menu =================')
                    print('\033[94m'+'\tMensagens'+'\033[0m')
                    print('\t1 - Enviar mensagem')
                    print('\t2 - Ler mensagem de um receptor (desenfileirar)')
                    print('\t3 - Consultar fila de comunicacao de um receptor')
                    print('\t4 - Remover todas mensagens de um receptor')
                    print('\033[91m'+'\t0'+'\033[0m'+' - Voltar')
                    print()
                    print('\033[96m' + '========================================')
                    print('\033[0m', end='')
                    print('Selecione uma opção:')
                    resposta = input()
                    print()

                    match resposta:
                        case '1':
                            # Emissor
                            print('1 - Enviar mensagem')
                            qtd_emissores = consultar_emissores()
                            print()
                            if qtd_emissores == 0:
                                print("Não é possível adicionar mensagem pois não há emissores cadastrados")
                                continue

                            print('Selecione o emissor da mensagem:')
                            id_emissor = input()
                            print()
                            try:
                                id_emissor = int(id_emissor)
                            except ValueError:
                                print('O id informado é inválido')
                                continue

                            if not valida_emissor(id_emissor):
                                print('Nenhum emissor cadastrado com o id informado')
                                continue

                            # Mensagem
                            print('Insira a mensagem que deve ser enviada ')
                            mensagem = input()
                            print()

                            # Receptor(es)
                            adicionar_receptor = '1'
                            qtd_receptores = consultar_receptores()
                            print()
                            if qtd_receptores == 0:
                                print("Não é possível adicionar mensagem pois não há receptores cadastrados")
                                continue

                            while adicionar_receptor == '1':

                                print('Selecione o receptor da mensagem (apenas 1 de cada vez): ')
                                id_receptor = input()
                                print()
                                try:
                                    id_receptor = int(id_receptor)
                                except ValueError:
                                    print('O id informado é inválido')
                                    print('Deseja tentar novamente?')
                                    print('\t0 - Não')
                                    print('\t1 - Sim')
                                    adicionar_receptor = input()
                                    continue

                                if not valida_receptor(id_receptor):
                                    print('Nenhum receptor cadastrado com o id informado')
                                    print('Deseja tentar novamente?')
                                    print('\t0 - Não')
                                    print('\t1 - Sim')
                                    adicionar_receptor = input()
                                    continue

                                enviar_mensagem(id_emissor, id_receptor, mensagem)
                                print()

                                print('Deseja enviar a mensagem para outro receptor?')
                                print('\t0 - Não')
                                print('\t1 - Sim')
                                adicionar_receptor = input()

                        case '2':
                            print('2 - Ler mensagem de um receptor (desenfileirar)')

                            qtd_receptores = consultar_receptores()
                            print()
                            if qtd_receptores == 0:
                                print("Não há receptores cadastrados")
                                continue

                            print('Selecione o receptor que deseja visualizar:')
                            id_receptor = input()
                            print()
                            try:
                                id_receptor = int(id_receptor)
                            except ValueError:
                                print('O id informado é inválido')
                                continue

                            if not valida_receptor(id_receptor):
                                print("Não existe receptor com o id informado")
                                continue

                            retira_mensagem(id_receptor)

                        case '3':
                            print('3 - Consultar fila de comunicacao de um receptor')

                            qtd_receptores = consultar_receptores()
                            print()
                            if qtd_receptores == 0:
                                print("Não há receptores cadastrados")
                                continue

                            print('Selecione o receptor que deseja visualizar:')
                            id_receptor = input()
                            print()
                            try:
                                id_receptor = int(id_receptor)
                            except ValueError:
                                print('O id informado é inválido')
                                continue

                            if not valida_receptor(id_receptor):
                                print("Não existe receptor com o id informado")
                                continue

                            consultar_lista_comunicacao(id_receptor)
                            print()

                        case '4':
                            print('4 - Remover todas mensagens de um receptor')

                            qtd_receptores = consultar_receptores()
                            print()
                            if qtd_receptores == 0:
                                print("Não há receptores cadastrados")
                                continue

                            print('Selecione o receptor que deseja visualizar:')
                            id_receptor = input()
                            print()
                            try:
                                id_receptor = int(id_receptor)
                            except ValueError:
                                print('O id informado é inválido')
                                continue

                            if not valida_receptor(id_receptor):
                                print("Não existe receptor com o id informado")
                                continue

                            remover_lista_comunicacao(id_receptor)

                        case '0':
                            print('\033[91m' + '0' + '\033[0m' + ' - Voltar')
                            print('Voltando para o menu...')
                            break

                        case _:
                            print(f'"{resposta}" não é uma opção válida')

            case '0':
                print('\033[91m' + '0' + '\033[0m' + ' - Sair')
                print('Saindo...')
                print('Obrigado!')
                exit()

            case _:
                print(f'"{resposta}" não é uma opção válida')


header = Header()

if __name__ == "__main__":
    inicia_interface()
