select * from dojos;
insert into dojos (name)values("Ninja_dojo");
insert into dojos (name)values("Cat_dojo");
insert into dojos (name)values("Dog_dojo");
delete from dojos;
insert into dojos (name)values("Master_dojo");
insert into dojos (name)values("Snake_dojo");
insert into dojos (name)values("Wolf_dojo");
select * from ninjas;
insert into ninjas (first_name, last_name, age, dojo_id)values("Kevin","cantrell",18,13);
insert into ninjas (first_name, last_name, age, dojo_id)values("Harry","bran",22,13);
insert into ninjas (first_name, last_name, age, dojo_id)values("Jacob","frombar",21,13);

insert into ninjas (first_name, last_name, age, dojo_id)values("json_arrayagg","json_objectagg",20,14);
insert into ninjas (first_name, last_name, age, dojo_id)values("john","jewl",20,14);
insert into ninjas (first_name, last_name, age, dojo_id)values("lang","haller",19,14);

insert into ninjas (first_name, last_name, age, dojo_id)values("con","lanbert",18,15);
insert into ninjas (first_name, last_name, age, dojo_id)values("don","derg",22,15);
insert into ninjas (first_name, last_name, age, dojo_id)values("bryn","forgen",21,15);

select * from ninjas where dojo_id = 13;

select * from ninjas where dojo_id = 15;

select * from dojos where id = 15