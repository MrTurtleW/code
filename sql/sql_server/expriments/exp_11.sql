create login cxp with password='123',default_database=EDUC;

create user p for login cxp with default_schema=dbo;

create role ��ƽ
grant update(sno),select on student to ��ƽ��

drop role ��ƽ;

exec sp_adduser 'cxp','p','��ƽ'