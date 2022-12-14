create table units (
	id int auto_increment primary key,
    name varchar(255)
    );

create table users (
	id int auto_increment primary key,
    unit int,
    f_name varchar(255),
    l_name varchar(255),
    email varchar(255),
    password varchar(255),
    foreign key (unit) references units (id)
    );

create table missions (
	id int auto_increment primary key,
    unit int,
    name varchar(255),
    start_date datetime,
    end_date datetime,
    foreign key (unit) references units (id)
	);

create table tmr_type (
	id int auto_increment primary key,
    type varchar(255)
    );
    
create table vehicles (
	id int auto_increment primary key,
    make varchar(255),
    model varchar(255)
    );
    
create table assets (
	id int auto_increment primary key,
    type varchar(255),
    length int,
    width int,
    heigh int,
    weight int,
    hazmat boolean
    );
    
create table tmrs (
	unit_id int,
    mission_id int,
    type int,
    name varchar(255),
    num varchar(255) unique key primary key,
    pickup varchar(255),
    start_date datetime,
    dropoff varchar(255),
    end_date datetime,
    assets varchar(255),
    sup_unit int,
    status varchar(255),
    comments varchar (255),
    edited_by int,
    foreign key (unit_id) references users (id),
    foreign key (mission_id) references missions (id),
    foreign key (edited_by) references users (id)
    );

create table tmr_wip (
	tmr_id varchar(255),
    vic_id int,
    asset_id int,
    foreign key (tmr_id) references tmrs (num),
    foreign key (vic_id) references vehicles (id),
    foreign key (asset_id) references assets (id)
    );