mysql -h localhost -u root
mysql -u root -p

create database CSE370;

use CSE370;

create table lab_grades(Std_ID char(4),Name varchar(15),Major char(3),section char(1),Days_present int, Project_marks double, CGPA decimal(3,2),Submission_date date);

insert into lab_grades values('s001', 'Abir', 'CS', '1', 10, 18.5, 3.91, '2018-09-15'),('s019', 'Naima', 'CSE', '2', 12, 20, 3.7, '2018-08-14'),('s002', 'Nafis', 'CSE', '1', 12, 20, 3.86, '2018-08-15'),
('s003', 'Tasneem', 'CS', '1', 8, 18, 3.57, '2018-09-18'),('s004', 'Nahid', 'ECE', '2', 7, 16.5, 3.25, '2018-08-20'),('s005', 'Arafat', 'CS', '2', 11, 20, 4.0, '2018-09-13'),('s006', 'Tasneem', 'CSE', '1', 12, 17.5, 3.7, '2018-08-15'),('s007', 'Muhtadi', 'ECE', '1', 10, 19, 3.67, '2018-09-16'),('s008', 'Farhana', 'CSE', '2', 6, 15, 2.67, '2018-08-16');

select * from lab_grades;

------
DESCRIBE lab_grades;

ALTER TABLE lab_grades ADD project_title varchar(10);

ALTER TABLE lab_grades MODIFY COLUMN project_title varchar(50);

ALTER TABLE lab_grades DROP COLUMN project_title;

Update lab_grades SET Project_marks = 18.5 where Std_ID = 's003';

UPdate Lab_grades SET CGPA ='3.5', Days_present=10 WHERE Name = 'Nahid';

Update Lab_grades SET Project_marks = 15 WHERE Name = 'Tasneem';

Delete from lab_grades where Name='Naima';

Delete from lab_grades where Days_present<10;

Drop table lab_grades;

Drop database CSE370;

SELECT Std_ID, Name, CGPA From lab_grades;

Select Name, (Project_marks+Days_present*5/12) From lab_grades;

Select Name, (Project_marks+Days_present*5/12) AS total_Marks From lab_grades;

Exit


----HOMEWORK-----

create table users(member_id varchar(5), Name varchar(50), email varchar(50), influence_count int, member_since date, multiplier int);

insert into users values
('1','Taylor Otwell','otwell@laravel.com',739360,'2020-06-10',10),
('2','Ryan Dahl','ryan@nodejs.org',633632,'2020-04-22',10),
('3','Brendan Eich','eich@javascript.com',939570,'2020-05-07',8),
('5','Evan You','you@vuejs.org',982630,'2020-06-11',7),
('6','Rasmus Lerdorf','leordorf@php.org',937927,'2020-06-03',8),
('7','Guido van Rossum','guido@python.org',968827,'2020-07-18',19),
('8','Adrian Holovaty','adrian@djangoproject.com',570724,'2020-05-07',5),
('9','Simon Willison','simon@djangoproject.com',864615,'2020-04-30',4),
('10','James Gosling','james@java.com',719491,'2020-05-18',5),
('11','Rod Johnson','rod@spring.io',601744,'2020-05-18',7),
('12','Satoshi Nakamoto','nakamoto@blockchain.com',630488,'2020-05-10',10);

Query1: ALTER TABLE users CHANGE member_id id char(5);
Query2: SELECT id, name, email, member_since FROM users;
Query3: SELECT name, email FROM users;
Query4: SELECT name,email, member_since,(1-(multiplier*influence_count/20000000)) FROM users;
Query5: SELECT name,email, member_since,(1-(multiplier*influence_count/20000000)) AS Ranking FROM users;


WEEK 3
SELECT UPPER(Name) FROM lab_grades;

SELECT * FROM lab_grades;
SELECT Major FROM lab_grades;

SELECT DISTINCT Major FROM lab_grades;

SELECT * FROM lab_grades ORDER BY CGPA;
SELECT * FROM lab_grades ORDER BY CGPA DESC;
SELECT * FROM lab_grades ORDER BY Days_present,CGPA;

SELECT Name, Major, CGPA FROM lab_grades WHERE Major='CSE';
SELECT Name, Project_marks FROM lab_grades WHERE Project_marks BETWEEN 16.5 AND 20;
SELECT Name, Major, CGPA FROM lab_grades WHERE Major IN ('CS', 'CSE');
SELECT Name, Major, CGPA, Days_present FROM lab_grades WHERE Major='CSE' AND Days_present>10;
SELECT Name, Major FROM lab_grades WHERE Name Like 'a%';
SELECT Name, Major FROM lab_grades WHERE Name Like 'a%a%';
SELECT Name, Major FROM lab_grades WHERE Name Like 'a___';

SELECT MAX(cgpa) FROM lab_grades;
SELECT MAX(cgpa) AS highest_cgpa FROM lab_grades;
SELECT MIN(cgpa) AS lowest_cgpa FROM lab_grades;
SELECT AVG(days_present) FROM lab_grades;
SELECT SUM(days_present) FROM lab_grades;
SELECT MAX(name) FROM lab_grades;
SELECT MIN(name) FROM lab_grades;

SELECT major, MAX(cgpa) FROM lab_grades GROUP BY major;
SELECT COUNT(*) FROM lab_grades;
SELECT major, COUNT(*) FROM lab_grades GROUP BY major;
SELECT major, COUNT(*) FROM lab_grades WHERE days_present <10 GROUP BY major;
SELECT major, COUNT(*) FROM lab_grades GROUP BY major HAVING COUNT(*)>2;

Homework 3
Query1: SELECT DISTINCT multiplier FROM users ORDER BY multiplier DESC;
Query2: SELECT id,influence_count FROM users ORDER BY influence_count;
Query3: SELECT DISTINCT member_since FROM users ORDER BY member_since;
Query4: SELECT name, email, member_since FROM users WHERE member_since LIKE '2020-07-1';
Query5: SELECT name, email, member_since FROM users WHERE member_since<'2020-07-1';
Query6: SELECT name, email, member_since FROM users WHERE member_since BETWEEN '2020-07-31' AND '2020-08-15';
Query7: SELECT name, email, member_since FROM users WHERE influence_count>=750000;
Query8: SELECT name, email, member_since FROM users WHERE member_since BETWEEN '2020-07-31' AND '2020-08-15' AND influence_count>=750000;
Query9: SELECT id FROM users WHERE email Like '%.com';
Query10:SELECT id FROM users WHERE email Like '%djangoproject%';
Query11:SELECT name,email FROM users ORDER BY member_since DESC LIMIT 5;
Query12:SELECT COUNT(*) FROM users;
Query13:SELECT COUNT(DISTINCT multiplier) FROM users;
Query14:SELECT COUNT(*),multiplier FROM users WHERE member_since>'2020-04-30' GROUP BY multiplier;
Query15:SELECT name,multiplier FROM users WHERE influence_count>=700000 AND multiplier%2=0 ORDER BY name DESC;

LAB 4:
select max(cgpa) from lab_grades;

Nested Queries, Finding the name of the max CGPA
select Name from lab_grades where cgpa = (select max(cgpa) from lab_grades);

Find the name who has the max CGPA of each dept
SELECT name, major, cgpa from lab_grades Where (major,cgpa) IN (Select major,max(cgpa) From Lab_grades Group by major);

Select cgpa from lab_grades Where major = 'CS';
Select cgpa from lab_grades Where major = 'CSE';
Select cgpa from lab_grades Where major = 'ECE';

Select a student from CS whose CGPA is greater than the ones in CSE
Select name,cgpa from lab_grades Where major ='CS' AND cgpa>ANY (SELECT cgpa FROM lab_grades Where major='CSE');
Select name,cgpa from lab_grades Where major ='CS' AND cgpa>ALL (SELECT cgpa FROM lab_grades Where major='CSE');

SELECT DISTINCT MAJOR FROM Lab_grades L1 Where EXISTS (Select * From Lab_grades L2 Where L2.Major=L1.Major AND L2.cgpa<3.7);
SELECT Name,cgpa,Std_ID FROM Lab_grades L1 Where not EXISTS (Select * From Lab_grades L2 Where L2.Std_ID!=L1.Std_ID AND L2.Project_marks>L1.Project_marks);


Homework 4
Query1: SELECT employee_id, last_name, email, salary, department_id FROM employees WHERE (department_id, salary) IN (Select department_id, MAX(salary) FROM employees GROUP BY department_id);
Query2: SELECT employee_id, last_name, email, commission_pct, department_id FROM employees WHERE (commission_pct,department_id) IN (SELECT department_id, MAX(commission_pct) FROM employees GROUP BY department_id);
Query3: SELECT employee_id, last_name, email, commission_pct, department_id FROM employees WHERE (commission_pct,department_id) IN (SELECT department_id, MIN(commission_pct) FROM employees GROUP BY department_id);
Query4: SELECT employee_id, last_name, email, commission_pct, department_id FROM employees WHERE department_id =5 AND commission_pct>ANY (SELECT commission_pct FROM employees WHERE department_id=7);
Query5: SELECT employee_id, last_name, email, salary, department_id FROM employees WHERE department_id =5 AND salary>ANY (SELECT salary FROM employees WHERE department_id=7);
Query6: SELECT department_id, job_id, salary FROM employees WHERE salary<ANY (SELECT job_id, salary FROM employees GROUP BY department_id);
Query7: SELECT manager_id FROM employees L1 WHERE EXISTS (SELECT * FROM employees L2 Where L2.manager_id=L1.manager_id AND L2.salary<2500);
Query8: SELECT manager_id FROM employees L1 WHERE EXISTS (SELECT * FROM employees L2 Where L2.manager_id=L1.manager_id AND L2.commission_pct<18.25);
Query9: SELECT manager_id FROM employees L1 WHERE NOT EXISTS (SELECT * FROM employees L2 Where L2.manager_id=L1.manager_id AND L2.salary<3500);
Query10:SELECT manager_id FROM employees L1 WHERE NOT EXISTS (SELECT * FROM employees L2 Where L2.manager_id=L1.manager_id AND L2.commission_pct<45.05);
