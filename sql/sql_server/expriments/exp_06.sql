update student set sname='����' where sname='���';
select * from student;
select student.sno,student.sname from student,class where student.clsNo=class.clsNo and class.Speciality='�����Ӧ��';
select distinct sno from sc;
select sno,0.75*grade from sc where grade>80 and grade <90 and cno='0001';
select student.* from student,class where student.clsNo=class.clsNo and (class.Speciality='�����Ӧ��' or class.Speciality like '��ѧ') and sname like '��%';
select sno,grade from sc where grade>(select sc.grade from sc,student where student.sno=sc.sno and student.sname='����' and sc.cno='0001');
select sname from student where not exists(select * from sc where cno='0002' and sno=student.sno);