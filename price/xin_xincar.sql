create table xin_xincar
(
        id int unsigned not null auto_increment primary key,
        name varchar(1024) default NULL,
        city varchar(512) default NULL,
        price varchar(512) default NULL,
        licensed_time varchar(512) default NULL,
        mile varchar(512) default NULL
)  ENGINE=InnoDB DEFAULT CHARSET=utf8;