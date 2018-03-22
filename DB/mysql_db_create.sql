#remote_user_create
create database devdb;
insert into mysql.user(Host,User,Password) values("192.168.%.%","dev",password("123456"));
grant all privileges on devdb.* to dev@'192.168.%.%' identified by '123456';
flush privileges;

#table_create
use `devdb`;

create table `tb_ip`(
    `id` int unsigned not null auto_increment comment 'PKey id',
    `protocol` char(8) not null default 'no',
    `address` char(16) not null default 'no',
    `port` int(8) unsigned not null default 0,
    `add_time` timestamp not null default current_timestamp on update current_timestamp,
    primary key (`id`),
    unique key `address` 
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
