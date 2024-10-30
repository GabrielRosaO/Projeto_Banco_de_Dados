use BD_Exoplanetas;

select * from cientista;
select * from exoplaneta;
select * from observacao;
select * from pesquisa;
select * from estrela;
select * from identificacao_estrelas;
select * from identificacao_planetas;
select * from p_biologia;
select * from p_fisica;
select * from p_geologia;


insert into Exoplaneta values ('2M0437 b', 'Confirmado', 2021, 'Imagem D', '2M0437', 128.1, null, 4.0, null, null);
insert into Exoplaneta values ('COCONUTS-2 b', 'Confirmado', 2021, 'Imagem D', 'COCONUTS-2A',  10.89, null, 6.4, 1.12, null);
insert into Exoplaneta values ('11 Com b', 'Confirmado', 2007, 'Velocidade Radial', '11 Com', 110.6, null, null, null, 326.03);
insert into Exoplaneta values ('Gaia-3 b', 'Confirmado', 2021, 'Velocidade Radial', 'Gaia-3', 35.37, null, null, null, 310.9);  
insert into Exoplaneta values ('TOI-3362 b', 'Confirmado', 2021, 'Transito', 'TOI-3362', 370.85, null, 4.0, 1.2, 18.02);
insert into Exoplaneta values ('AB Pic b', 'Confirmado', 2005, 'Imagem D', 'AB Pic', 47.3, null, 13.5, 1.75, null);

insert into identificacao_planetas values ('Mauna Kea', 'COCONUTS-2 b');
insert into identificacao_planetas values ('Real de Greenwich', '2M0437 b');
insert into identificacao_planetas values ('Mauna Kea', '11 Com b');
insert into identificacao_planetas values ('Paranal', 'Gaia-3 b');
insert into identificacao_planetas values ('Paranal', 'TOI-3362 b');
insert into identificacao_planetas values ('Real de Greenwich', 'AB Pic b');


insert into Estrela values ('11 Com', null, 19.0, 2.7, -0.35);
insert into Estrela values ('2M0437', 0.0025, 0.84, 0.0165, 0.01);
insert into Estrela values ('COCONUTS-2A', 0.475, 0.388, 0.37, 0.08);
insert into Estrela values ('Gaia-3', 7.9, 0.69, 0.705, 0.12);
insert into Estrela values ('TOI-3362', 2.14, 1.83, 1.445, 0.017);
insert into Estrela values ('AB Pic', 0.03, null, null, 0.04);

insert into Observacao values ('Mauna Kea', 'Havaí, EUA');
insert into Observacao values ('Paranal', 'Atacama, Chile');
insert into Observacao values ('Real de Greenwich', 'Londres, Inglaterra');

insert into Pesquisa values (23423, 10, 'Amazonas, BR', 'Biologia');
insert into Pesquisa values (18347, 10, 'Atacama, CL', 'Geologia');
insert into Pesquisa values (05918, 10, 'Moscow, RU', 'Fisica');
insert into Pesquisa values (57150, 10, 'Frankfurt, DE', 'Fisica');  

insert into p_biologia values (23423);

insert into p_fisica values (05918);
insert into p_fisica values (57150);

insert into p_geologia values (18347);

insert into identificacao_estrelas values ('Mauna Kea', '11 Com');
insert into identificacao_estrelas values ('Mauna Kea', 'COCONUTS-2A');
insert into identificacao_estrelas values ('Paranal', '2M0437');
insert into identificacao_estrelas values ('Paranal', 'Gaia-3');
insert into identificacao_estrelas values ('Real de Greenwich', 'TOI-3362');


insert into Cientista values ('410475111', 'Rogerio M.', 5, 'Mauna Kea'); 
insert into Cientista values ('478159513', 'Mario S.', 4, 'Mauna Kea');
insert into Cientista values ('198273959', 'Luigi S.', 4, 'Mauna Kea');
insert into Cientista values ('981759234', 'Miles M.', 2, 'Paranal');
insert into Cientista values ('198723565', 'Peter P.', 3, 'Paranal');
insert into Cientista values ('571732885', 'Toad K.', 10, 'Paranal');
insert into Cientista values ('091723751', 'Adre M.', 8, 'Real de Greenwich');
insert into Cientista values ('000012355', 'Bowser H.', 6, 'Real de Greenwich');
insert into Cientista values ('183759915', 'Sylas T.', 2, 'Real de Greenwich');




