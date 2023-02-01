create table employees (
  employee_id serial primary key,
  first_name text not null,
  last_name text not null,
  salary numeric not null,
  description text
);

insert into employees(first_name,last_name,salary,description) values ('Jan','Kowalski',10000,'Opisa Jana Kowalskiego, bardzo długi bo będziemy tego potrzebować w aplikacji webowej');
insert into employees(first_name,last_name,salary,description) values ('Stefan','Nowak',5000,'Opisa Stefana Nowaka, bardzo długi bo będziemy tego potrzebować w aplikacji webowej');
insert into employees(first_name,last_name,salary,description) values ('Krzysztof','Testowy',8000,'Opisa Krzysztofa Testowego, bardzo długi bo będziemy tego potrzebować w aplikacji webowej');

