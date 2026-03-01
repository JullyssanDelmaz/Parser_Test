QUAKE LOG PARSER

Este projeto consiste na implementação de um parser para o arquivo games.log, gerado por partidas do jogo Quake III Arena.
Todo o projeto está sendo desenvolvido utilizando a linguagem de programação Python, aplicando conceitos de Programação Orienta a Objetos (POO), seguindo boas práticas de organização e clareza de código.

A primeira Task é processar o log e agrupar informações de cada partida, informando o total de kills por jogo, lista de jogadores que participaram de cada partida,
quantidade de kills realizadas por cada jogador mas nas kills contabilizadas pelo world para cada jogador, seria tirado uma kill. 
O parser inicia e cada vez que é encontrado um InitGame no log, uma nova partida é iniciada no dicionário.
Quando uma linha de kill é encontrada, o total de kills é incrementado, o killer e o victim são extraídos da linha e ambos são adicionados
na lista de players sem duplicação e a pontuação é atualizada: se o killer não for <world>, recebe 1 ponto; Se o killer for <world>, o victim perde 1 ponto.
A estrutura de resultado é um dicionário com chaves: total_kills, players e kills.
