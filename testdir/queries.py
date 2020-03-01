SQL1='''
SELECT r.name,count(s.name) 
    from students s, rooms r
    where s.room = r.id
    group by r.name
'''

SQL2='''
SELECT t.room, avg((current_date - birthday)/365) age
	FROM students t
group by t.room
order by age
limit 5
'''
SQL3='''
SELECT t.room, max(abs(s.birthday - t.birthday)/365) age
	FROM students t, students s
	where s.room = t.room and s.id < t.id
	group by t.room
	order by age desc
        limit 5


'''
SQL4='''

select t.name from rooms t
	where exists(
		select 1 from students s 
			where s.room = t.id and s.sex = 'M'
	) 
	and 
	exists(
		select 1 from students s 
			where s.room = t.id and s.sex = 'F'
	) 
'''
CREATE_ROOMS='''CREATE TABLE ROOMS(ID INT PRIMARY KEY,NAME CHAR(10));'''
CREATE_STUDENTS='''CREATE TABLE STUDENTS(BIRTHDAY DATE,ID INT PRIMARY KEY,NAME CHAR(29),ROOM INT,SEX CHAR(1));'''