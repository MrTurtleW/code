INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('CS01','�����һ��','����','�����Ӧ��');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('CS02','���������','����','�����Ӧ��');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('MT04','��ѧ�İ�','�³�','��ѧ');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('PH08','����˰�','���','����');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('GL02','�������','����','Ӧ�õ���');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('CS03','���������','�����','�����Ӧ��');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('GL04','�����İ�','�ܲ�','Ӧ�õ���');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('MT05','��ѧ���','����','��ѧ');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('CS07','������߰�','����','�����Ӧ��');
INSERT INTO class(clsNo,clsName,Director,Speciality)
		  VALUES('PH09','����Ű�','��','����');
select * from class;
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090101','����','��','CS01','�¹�40#',20,1.76);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090102','���','��','CS01','����·96#',22,1.72);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090306','��ͮ','Ů','MT04','����·94#',19,1.65);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090107','����','Ů','PH08','����С��74#',18,1.60);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090108','�����','��','CS03','�˻�·10#',21,1.83);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090305','��','��','PH09','ľҶ36#',22,1.80);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090110','�ܲ�','��','GL04','κ��7#',22,1.73);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090113','����','��','MT05','���4#',18,1.75);
INSERT INTO student(sno,sname,ssex,clsNo,saddr,sage,height)
		  VALUES('20090117','����','��','CS07','ľҶ18#',17,1.78);
select * from student;

INSERT INTO course(cno,cname,cpno,Ccredit)
		  VALUES('0001','�ߵ���ѧ',null,6);
INSERT INTO course(cno,cname,cpno,Ccredit)
		  VALUES('0003','���������','0001',3);
INSERT INTO course(cno,cname,cpno,Ccredit)
		  VALUES('0007','����','0001',4);
INSERT INTO course(cno,cname,cpno,Ccredit)
		  VALUES('0005','Ӣ��',NULL,3);
INSERT INTO course(cno,cname,cpno,Ccredit)
		  VALUES('0006','���ݽṹ',null,4);
INSERT INTO course(cno,cname,cpno,Ccredit)
		  VALUES('0002','��ɢ��ѧ',NULL,2);
select * from course;

INSERT INTO sc(sno,cno,grade)
		  VALUES('20090101','0001',90);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090101','0007',86);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090102','0001',87);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090101','0003',93);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090306','0001',87);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090306','0003',93);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090106','0007',85);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090306','0007',90);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090102','0003',96);
INSERT INTO sc(sno,cno,grade)
		  VALUES('20090306','0001',90);
select * from sc;

INSERT INTO student(sno,sname,ssex,clsNo,sage)
		  VALUES('20091101','����','��','CS01',19);
select * from student;

update student set clsNo='CS02' where clsNo='CS01' and sage<20;
select * from student;

delete student where clsNo='CS02' and sage<20;
select * from student;