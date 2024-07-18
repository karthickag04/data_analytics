-- Create a new database named studentDb1
create database studentDb1;

-- Switch to the newly created database
use studentdb1;

-- Create a table named tbl_reg with columns sno, name, age, location
create table tbl_reg(
    sno int, 
    name varchar(50),
    age int,
    location varchar(60)
);

-- Show the list of tables in the current database
show tables;

-- Drop (delete) the table tbl_reg
drop table tbl_reg;

-- Create a new table tbl_reg1 with columns sno (primary key), name, age, location
create table tbl_reg1(
    sno int primary key, 
    name varchar(50),
    age int,
    location varchar(60)
);

-- Create a new table tbl_reg2 with columns sno (primary key with auto increment), name (unique), age (must be > 18), location (default value "Trichy")
create table tbl_reg2(
    sno int primary key auto_increment, 
    name varchar(50) unique not null,
    age int check (age > 18),
    location varchar(60) default "Trichy"
);

-- Drop (delete) the table tbl_reg2
drop table tbl_reg2;

-- Show the list of tables in the current database
show tables;

-- Describe the structure (columns) of table tbl_reg2
describe tbl_reg2;

-- Select all rows from table tbl_reg (assuming it exists)
select * from tbl_reg;

-- Select sno and name columns from table tbl_reg2
select sno, name from tbl_reg2;

-- Select sno as "Register No" and name as "Student Name" from table tbl_reg2
select sno as "Register No", name as "Student Name" from tbl_reg2;

-- Method 01: Insert rows into table tbl_reg using specified column names
insert into tbl_reg(sno, name, age, location) values (1001, "Arun Kumar", 20, "Trichy");

-- Attempting to insert into tbl_reg without specifying all columns (not valid)
insert into tbl_reg(sno) values (1001);
insert into tbl_reg(name) values ("Arun");

-- Method 02: Insert rows into table tbl_reg assuming all columns are provided
-- Working example
insert into tbl_reg values (1001, "Arun Kumar", 20, "Trichy");

-- Not working examples due to incorrect values or column order
insert into tbl_reg values (11, 22, 20, "Trichy");  -- Incorrect values
insert into tbl_reg values ("arun", 22, 20, "Trichy");  -- Incorrect values

-- Select all rows from table tbl_reg1
select * from tbl_reg1;

-- Insert a row into tbl_reg1 specifying all columns
insert into tbl_reg1(sno, name, age, location) values (1112, "Arun Kumar", 20, "Trichy");

-- Insert a row into tbl_reg1 without specifying all columns (assuming sno is auto_increment or default)
insert into tbl_reg1(sno) values (1113);

-- Select all rows from table tbl_reg2
select * from tbl_reg2;

-- Insert rows into tbl_reg2 with specified columns
insert into tbl_reg2(name, age, location) values ("Arun Kumar", 50, "Trichy");
insert into tbl_reg2(sno, name, age, location) values (20, "Arun", 50, "Trichy");

-- Insert a row into tbl_reg2 without specifying all columns (assuming location defaults to "Trichy")
insert into tbl_reg2(name, age) values ("shri son", 19);

-- Insert a row into tbl_reg2 specifying sno and location
insert into tbl_reg2(sno, age, location) values (20, 50, "Trichy");

-- Create a table tbl_course with columns course_id (primary key auto_increment) and course_name
create table tbl_course(
    course_id int primary key auto_increment,
    course_name varchar(255)
);

-- Create a table tbl_lib with columns lib_id (primary key auto_increment), reg_id (foreign key referencing tbl_reg2), course_id (foreign key referencing tbl_course), name, book_tk, book_rt
create table tbl_lib(
    lib_id int primary key auto_increment,
    reg_id int,
    course_id int,
    name varchar(50),
    book_tk date,
    book_rt date,
    foreign key (reg_id) references tbl_reg2(sno),
    foreign key (course_id) references tbl_course(course_id)
);

-- Describe the structure (columns and constraints) of table tbl_lib
describe tbl_lib;

-- Select all rows from table tbl_lib
select * from tbl_lib;

-- Select all rows from table tbl_reg2
select * from tbl_reg2;

-- Select all rows from table tbl_course
select * from tbl_course;

-- Insert a row into tbl_course with course_name "BSC"
INSERT INTO tbl_course(course_name) values("BSC");

-- Insert multiple rows into tbl_lib with specified columns
INSERT INTO tbl_lib (lib_id, reg_id, course_id, name, book_tk, book_rt) VALUES
(2, 1, 1, 'Jane Smith', '2024-02-01', '2024-02-10'),
(3, 1, 1, 'Alice Johnson', '2024-03-01', '2024-03-20'),
(4, 1, 1, 'Bob Brown', '2024-04-01', '2024-04-15');
