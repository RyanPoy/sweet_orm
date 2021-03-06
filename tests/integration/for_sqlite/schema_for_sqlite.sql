
create table foos (
    c_bigint bigint default 10,
    c_blob blob(1024),
    c_bool bool default 0,
    c_char char default 'c',
    c_date date not null,
    c_datetime datetime not null,
    c_double double precision not null,
    c_integer integer default 100 null,
    c_numeric numeric null,
    c_real real,
    c_smallint smallint, 
    c_text text(1024),
    c_time time,
    c_varbinary varbinary(255),
    c_varchar varchar(64) not null default ''
);


create table users (
    id integer primary key,
    name varchar(32) not null default '',
    age int not null default 20
);

create table mobiles (
    id integer primary key,
    name varchar(32) not null default '',
    user_id int not null,
    foreign key (user_id) references users(id)
);

create table cars (
    id integer primary key,
    name varchar(32) not null default '',
    user_id int not null,
    foreign key (user_id) references users(id)
);

create table articles (
    id integer primary key,
    title varchar(64) not null,
    content text
);

create table tags (
    id integer primary key,
    name varchar(32) not null
);

create table articles_tags (
    id integer primary key,
    article_id int not null,
    tag_id int not null,
    foreign key (article_id) references articles(id),
    foreign key (tag_id) references tags(id)
);

create table categories (
    id integer primary key,
    name varchar(32) not null default '',
    parent_id int default null
);

create index idx_categories_parent_id on categories(parent_id);

create table students (
    id integer primary key,
    name varchar(32) not null default ''
);

create table courses (
    id integer primary key,
    name varchar(32) not null default ''
);

create table scores (
    id integer primary key,
    student_id int not null,
    course_id int not null,
    value int not null default 0,
    foreign key (student_id) references students(id),
    foreign key (course_id) references courses(id)    
);
