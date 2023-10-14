# LinkedLists

## Sobre o Projeto

Projeto de Sistema de Mensageria simplificado usando listas encadeadas, desenvolvido para a disciplina de Algoritmos e Estruturas de Dados - curso de Análise e Desenvolvimento de Sistemas.

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
permitir a um emissor enviar mensagens para um ou mais receptores. Para isso, ele vai
manter:

• uma lista de emissores de mensagens
• uma lista de receptores de mensagens
• filas de mensagens, uma fila para cada receptor
• Para poder enviar mensagem, um emissor tem que estar na lista de emissores. Para
enviar a mensagem, o emissor tem que informar quais são os receptores, que devem
estar na lista de receptores.
• Cada mensagem enviada é copiada (enfileirada) na fila de mensagens de cada um dos
receptores que o emissor definiu.
• Cada receptor deve retirar suas mensagens da fila (desenfileirar).

## Representação:
• Usa listas encadeadas (simples ou duplas).
• Cada nodo da lista de emissores deve conter: número de identificação (inteiro), nome
(string).
• Cada nodo da lista de receptores deve conter: número de identificação (inteiro), nome
(string).
• Cada fila de mensagens deve conter: identificação do receptor (inteiro), e a fila de
mensagens.
• Cada nodo da fila de mensagens deve conter: a identificação do emissor
(inteiro), e a mensagem (texto).
• É possível acrescentar outras informações nos nodos/listas se necessário.


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