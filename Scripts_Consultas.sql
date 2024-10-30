select C.nome from Cientista as C natural join Observacao as O where O.LOCALIZACAO = 'Atacama, Chile';

select O.NOME_centro, E.NOME, ES.NOME_ESTRELA, ES.IDADE from Exoplaneta as E join Estrela as ES on E.ESTRELA_ASSOCIADA=ES.NOME_ESTRELA 
natural join identificacao_planetas as IP natural join Observacao as O where O.NOME_CENTRO='Mauna Kea'; 

select O.NOME_CENTRO, count(*) from Exoplaneta as P join identificacao_planetas as IP on P.NOME=IP.NOME_PLANETA
inner join Observacao as O on O.NOME_CENTRO=IP.NOME_CENTRO group by O.NOME_CENTRO;

select count(*), P.SETOR_PESQUISA from Pesquisa as P natural join P_fisica as PS group by P.SETOR_PESQUISA;

select NOME,num_exoplanetas from Cientista;

select count(*) from Estrela;