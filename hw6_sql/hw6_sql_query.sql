---1. Insert dump (my_items) to your local database.
---	Create additional table phones with fields:
---		id, phone_name, company_id, user_id
CREATE TABLE phones (
	id int NOT NULL AUTO_INCREMENT,
	phone_name varchar(255) NULL,
	company_id int NOT NULL,
	user_id int NOT NULL,
	PRIMARY KEY (id)
);

---	Create additional table phone_companies with fields:
---		id, name
CREATE TABLE phone_companies (
	id int NOT NULL AUTO_INCREMENT,
	name varchar(255) NULL,
	PRIMARY KEY (id)
);

---Write select and save it to file to get users is developers.
SELECT * FROM users WHERE is_developer=1 INTO OUTFILE '/var/lib/mysql-files/devs.txt';

---	Insert xiaomi, apple, samsung to companies.
INSERT INTO phone_company (name) VALUES ("Xiaomi"), ("Apple"), ("Samsung");

---	Insert 3 phone (with any data) to phones.
INSERT INTO phones (phone_name, company_id, user_id) 
VALUES ("Xiaomi Redmi Note 8T", 1, 1), 
	("Apple iPhone 11", 2, 3), 
	("Samsung Galaxy S20", 3, 5);


---	Write select and save it to file to get phones where company_id=XIAOMI COMPANY ID.
SELECT * FROM phones WHERE company_id=1 INTO OUTFILE '/var/lib/mysql-files/xiaomi_phones.txt';

---2.* Select all users which have phones.
SELECT * FROM users
WHERE id IN (SELECT user_id FROM phones);
