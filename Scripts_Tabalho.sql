
drop database exoplanetas;


create database BD_Exoplanetas;

use BD_Exoplanetas;


create table cientista (
	ID varchar(9) not null default (000000000),
    NOME varchar(15) not null,
    NUM_EXOPLANETAS int,
    NOME_CENTRO varchar(30) not null,
    primary key (ID),
    foreign key (NOME_CENTRO) references Observacao(NOME_CENTRO)
		on update cascade
        on delete cascade);
    
create table Observacao (
	NOME_CENTRO varchar(30) not null,
    LOCALIZACAO varchar(30) not null,
    primary key (NOME_CENTRO));
    
create table Pesquisa (
	ID varchar(5) not null default (00000),
    NUM_PESQUISADORES int not null default (0),
    LOCALIZACAO varchar(30) not null,
    SETOR_PESQUISA char(10) not null,
    primary key(ID));

create table Estrela (
	NOME_ESTRELA varchar(20) not null,
    IDADE double,
    RAIO double,
    MASSA double,
    METALICIDADE double,
    primary key(NOME_ESTRELA));

create table Exoplaneta (
	NOME varchar(20) not null,
    STATUS char(12) not null default('Candidato'),
    ANO_DESCOBERTA int not null,
    METODO_IDENTIFICACAO varchar(20) not null,
    ESTRELA_ASSOCIADA varchar(20),
    DISTANCIA_ESTRELA double,
    MOLECULAS char(12),
    MASSA double,
    RAIO double,
    PERIODO double,
    primary key(NOME),
    foreign key(ESTRELA_ASSOCIADA) references Estrela(NOME_ESTRELA)
		on delete cascade
        on update cascade
    );


create table Identificacao_Estrelas (
	NOME_CENTRO varchar(30) not null,
    NOME_ESTRELA varchar(20) not null,
    primary key(NOME_CENTRO, NOME_ESTRELA),
    foreign key (NOME_CENTRO) references Observacao(NOME_CENTRO)
		on delete cascade
        on update cascade,
	foreign key (NOME_ESTRELA) references Estrela(NOME_ESTRELA)
		on delete cascade
        on update cascade);

create table Identificacao_Planetas (
	NOME_CENTRO varchar(30) not null,
    NOME_PLANETA varchar(20) not null,
    primary key(NOME_CENTRO, NOME_PLANETA),
    foreign key(NOME_CENTRO) references Observacao(NOME_CENTRO)
		on delete cascade
        on update cascade,
	foreign key(NOME_PLANETA) references Exoplaneta(NOME)
		on delete cascade
        on update cascade);
    
create table P_Biologia (
	ID varchar(6) not null,
    primary key (ID),
    foreign key(ID) references Pesquisa(ID)
		on delete cascade
        on update cascade);


create table P_Geologia (
	ID varchar(6) not null,
    primary key (ID),
    foreign key(ID) references Pesquisa(ID)
		on delete cascade
        on update cascade);
        

create table P_Fisica (
	ID varchar(6) not null,
    primary key (ID),
    foreign key(ID) references Pesquisa(ID)
		on delete cascade
        on update cascade);
        

alter table p_fisica add SETOR varchar(10) default 'Fisica';
alter table p_biologia add SETOR varchar(10) default 'Biologia';
alter table p_geologia add SETOR varchar(10) default 'Geologia';





