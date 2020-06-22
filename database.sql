create database test;
use test;
create table user(
id int not null auto_increment,
username varchar(30),
password varchar(70),
data_registered timestamp,
primary key (id)
);