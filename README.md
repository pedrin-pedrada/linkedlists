# LinkedLists

## Descrição do problema:
"Middleware Orientado a Mensagens (MOM), ou Message Brokers, ou Mensageria, são
ferramentas que oferecem suporte para comunicação assíncrona entre sistemas. Há
diferentes tipos de sistemas de mensageria (por assinatura, de broadcasting, de um
emissor para um receptor específico, etc), mas em geral essas ferramentas podem
armazenar temporariamente mensagens, não exigindo que o emissor e o receptor
estejam ativos durante a transmissão da mensagem. As mensagens são enfileiradas e
armazenadas até que o receptor as processe (desenfileire, de forma automática ou por
solicitação)."

O trabalho é a implementação de um sistema de mensageria simplificado, que vai
permitir a um emissor enviar mensagens para um ou mais receptores.


## Funcionalidades desenvolvidas
Algumas operações básicas a oferecidas pelo programa:
1) Inclui emissor na lista de emissores
2) Remove emissor da lista de emissores
3) Consulta emissores: escreve na tela os emissores cadastrados
4) Inclui receptor na lista de receptores
5) Remove receptor da lista de receptores: quando o receptor é removido, sua fila
de mensagens também é removida
6) Consulta receptores: escreve na tela os receptores cadastrados
7) Envia mensagem: um receptor cadastrado escreve a mensagem, e define quais
são os receptores (pelo menos um receptor). A mensagem é enfileirada na fila de
cada receptor.
8) Retira mensagem: um receptor cadastrado desenfileira uma mensagem
(apresenta mensagem de erro se a fila está vazia)
9) Consulta fila de mensagens: exibe a fila de mensagens de um receptor
10) Outras operações (a critério), como: exibe receptores com fila vazia, exibe
receptores com mais mensagens na fila, exibe total de mensagens enviadas por
um emissor, exibe total de mensagens recebidas por um receptor.

## Principais tecnologias utilizadas

Python (é premissa para o trabalho que as referências entre os nodos sejam manipuladas explicitamente pelo programa  - não utiliza classe,
método ou função pronta da linguagem para listas encadeadas).

## Sobre o Projeto

Projeto de Sistema de Mensageria simplificado usando listas encadeadas | Algoritmos e Estruturas de Dados | Análise e Desenvolvimento de Sistemas.