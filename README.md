QUAKE LOG PARSER

Este projeto consiste na implementação de um parser para o arquivo games.log, gerado por partidas do jogo Quake III Arena.
Todo o projeto está sendo desenvolvido utilizando a linguagem de programação Python, aplicando conceitos de Programação Orienta a Objetos (POO), seguindo boas práticas de organização e clareza de código.

Task 1 - Parser de Partidas

A primeira Task é processar o log e agrupar informações de cada partida, informando o total de kills por jogo, lista de jogadores que participaram de cada partida,
quantidade de kills realizadas por cada jogador mas nas kills contabilizadas pelo world para cada jogador, seria tirado uma kill. 
O parser inicia e cada vez que é encontrado um InitGame no log, uma nova partida é iniciada no dicionário.
Quando uma linha de kill é encontrada, o total de kills é incrementado, o killer e o victim são extraídos da linha e ambos são adicionados
na lista de players sem duplicação e a pontuação é atualizada: se o killer não for <world>, recebe 1 ponto; Se o killer for <world>, o victim perde 1 ponto.
A estrutura de resultado é um dicionário com chaves: total_kills, players e kills.


A resolução foi feita com a implementação de duas classes principais:
A Classe Game (que representa a partida individual) que armazena o game_id, total_kills, players e as kills do jogo e tem como atribuição Adicionar jogadores sem duplicação, registrar as kills e aplicar a regra especial do <world>.

A Classe Parser que é responsável por abrir o arquivo games.log, percorrendo linha por linha para identificar o início de uma nova partida (InitGame), identificar eventos de kill (Kill:), criar objetos (Game) e armazenar todas as partidas de um dicionário.




Task 2 - Ranking Geral de Kills

A segunda Task é criar um ranking geral de kills por jogador, informando o total de kills em ordem decrescente.
O parser inicia e percorre todos os objetos Game criados pelo parser na Task 1, soma as kills de cada jogador em todas as partidas e ordena os jogadores do maior para o menor número de kills.

A resolução foi feita com a implementação da Classe Ranking, responsável por receber o Parser já processado, percorrer todas as partidas, somar as kills de cada jogador, armazenar os totais em um novo dicionário acumulador, ordenar os jogadores usando o sorted() com lambda, reutilizando a lógica da Task 1.


Task 3 - API de Consulta (Placeholder)

A terceira Task consiste na criação de uma API REST utilizando FastAPI, permitindo a consulta dos dados processados na Task 1 e Task 2.
A API disponibiliza dois endpoints principais, o primeiro é a consulta de Partida por ID e o segundo endpoint é a consulta de Ranking Geral de Kills, em forma decrescente.

Tecnologias Utilizadas

FastAPI
Uvicorn

A resolução foi feita instanciando o Parser na inicialização da aplicação, carregando os dados do log uma única vez, sem sobrescrever, criando dois endpoints principais, GET /game/{game_id} e o GET /ranking.

A execução da API localmente: uvicorn Task_3_POO:app --reload

CONCEITOS APLICADOS AO PROJETO

Programação Orientada a Objetos;
Organização Modular do Código;
Manipulação de Arquivos;
Estrutura de Dados;
Ordenação com lambda;
Criação de API REST;
Tratamento de exceções com HTTPException;

