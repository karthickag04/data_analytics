-- Switch to the studentdb database
use studentdb;

-- Show existing tables in the database
show tables;

-- Describe the structure of tbl_reg1 table
describe tbl_reg1;

-- Select all records from tbl_reg1
select * from tbl_reg1;

-- Changing datatype of 'age' column in tbl_reg1 from int to tinyint
ALTER TABLE tbl_reg1 MODIFY age TINYINT not null;

-- Adding a new column 'dob' (date of birth) to tbl_reg1
ALTER TABLE tbl_reg1 ADD column dob DATE;

-- Dropping 'dob' column from tbl_reg1
ALTER TABLE tbl_reg1 drop column dob;

-- Adding a new column 'email' to tbl_reg1 with unique constraint, placed at the beginning
ALTER TABLE tbl_reg1 ADD email VARCHAR(100) UNIQUE FIRST;

-- Adding a new column 'phone' to tbl_reg1 with not null constraint, placed after 'location'
ALTER TABLE tbl_reg1 ADD phone VARCHAR(20) NOT NULL AFTER location;

-- Renaming 'phone' column in tbl_reg1 to 'phone_no'
ALTER TABLE tbl_reg1 RENAME COLUMN phone TO phone_no;

-- Select all records from tbl_reg1 after modifications
select * from tbl_reg1;

-- Select all records from tbl_course
select * from tbl_course;

-- Describe the structure of tbl_course
describe tbl_course;

-- Show existing tables
show tables;

-- Renaming tbl_lib table to tbl_library
ALTER TABLE tbl_lib RENAME TO tbl_library;

-- Describe the structure of tbl_library
describe tbl_library;

-- Select all records from tbl_library
select * from tbl_library;

-- Truncate all data in tbl_library
truncate table tbl_library;

-- Delete all data from tbl_library
delete from tbl_library;

-- Adding a new column 'lib_id' to tbl_library as the first column
alter table tbl_library add column lib_id int first;

-- Modifying 'lib_id' column in tbl_library to be auto_increment primary key
ALTER TABLE tbl_library MODIFY COLUMN lib_id int auto_increment;

-- Adding a foreign key constraint 'fk_reg_id' on 'reg_id' column in tbl_library referencing 'sno' column in tbl_reg2
ALTER TABLE tbl_library ADD CONSTRAINT fk_reg_id FOREIGN KEY (reg_id) REFERENCES tbl_reg2(sno);

-- Select all records from tbl_reg1
select * from tbl_reg1;

-- Describe the structure of tbl_reg1
describe tbl_reg1;

-- Dropping 'phone_no', 'dob', and 'email' columns from tbl_reg1
alter table tbl_reg1 
drop column phone_no, 
drop column dob,
drop column email;

-- Inserting a new record into tbl_reg1
insert into tbl_reg1(sno,name, age, location) values (1118,"ak", 50, "Trichy");

-- Updating age of student with sno 1112 in tbl_reg1
UPDATE tbl_reg1 SET age = 21 WHERE sno = 1112;

-- Select all records from tbl_reg1 after update
select * from tbl_reg1;

-- Updating name and age for students with specific sno values in tbl_reg1
UPDATE tbl_reg1 SET name = 'pavithiran', age = 20 WHERE sno = 1113;

-- Updating location to 'Chennai' for students aged 50 in tbl_reg1
UPDATE tbl_reg1 SET location = 'Chennai' WHERE age = 50;

-- Updating name based on sno values using CASE statement in tbl_reg1
UPDATE tbl_reg1
SET name = CASE
    WHEN sno = 1114 THEN 'shri jeswanth'
    WHEN sno = 1115 THEN 'parthiban'
    WHEN sno = 1116 THEN 'karthick'
    END
WHERE sno IN (1114, 1115, 1116);

-- Select all records from tbl_reg1 after update
select * from tbl_reg1;

-- Updating name based on sno values using CASE statement in tbl_reg1
UPDATE tbl_reg1
SET name = CASE
    WHEN sno = 1112 THEN 'arun'
    WHEN sno = 1113 THEN 'arun kumar'
    WHEN sno = 1118 THEN 'ragu'
    END
WHERE sno IN (1112, 1113, 1118);
