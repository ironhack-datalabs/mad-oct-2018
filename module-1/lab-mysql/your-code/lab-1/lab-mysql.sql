
CREATE DATABASE IF NOT EXISTS lab_mysql;

USE lab_mysql;

CREATE TABLE Cars (ID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (ID), VIN VARCHAR(45),  Manufacturer VARCHAR(45), Model VARCHAR(45), Year INT, Color VARCHAR(45));

CREATE TABLE Customers (ID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (ID), Customers_id INT,  Name VARCHAR(45), Phone BIGINT, email VARCHAR(45), Address VARCHAR(45), City VARCHAR(45), State VARCHAR(45), Country VARCHAR(45), ZIP INT);

CREATE TABLE Invoices (ID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (ID), Invoices_id INT, date DATE, Car VARCHAR(45), Customer VARCHAR(45), Salesperson VARCHAR(45));

CREATE TABLE Salespersons (ID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (ID), Salespersons_id INT, Name VARCHAR(45), Store VARCHAR(45));

CREATE TABLE Cars_have_customers (Cars_have_customers_id INT, VIN INT, Customers_id INT, PRIMARY KEY (Cars_have_customers_id), FOREIGN KEY (VIN) REFERENCES Cars (ID), FOREIGN KEY (Customers_id) REFERENCES Customers (ID));

CREATE TABLE Cars_have_invoices (Cars_have_invoices_id INT, VIN INT, Invoices_id INT, PRIMARY KEY (Cars_have_invoices_id), FOREIGN KEY (VIN) REFERENCES Cars(ID), FOREIGN KEY (Invoices_id) REFERENCES Invoices (ID));

CREATE TABLE Customers_have_salespersons (Customers_have_salespersons_id INT, Customers_id INT, Salespersons_id INT, PRIMARY KEY (Customers_have_salespersons_id), FOREIGN KEY (Customers_id) REFERENCES Customers (ID), FOREIGN KEY (Salespersons_id) REFERENCES Salespersons(ID));

INSERT INTO Cars (ID, VIN, Manufacturer, Model, Year, Color) 
  VALUES (0, '3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', 2019, 'Blue'),
    			(0, 'ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', 2019, 'Red'),
				(0, 'RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', 2018, 'White'),
				(0, 'HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', 2018, 'Silver'),
				(0, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60', 2019, 'Gray'),
				(0, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', 2019, 'Gray');


INSERT INTO Customers  (ID, Customers_id, Name, Phone, email, Address, City, State, Country, ZIP)
	VALUES (0, 100001, 'Pablo Picasso', 0034636176382, '-', 'Paseo de la Chopera 14', 'Madrid', 'Madrid', 'Spain', 28045),
					(0, 200001, 'Abraham Lincoln', 0013059077086, '-', '120 SW 8th St', 'Miami', 'Florida', 'USA', 33130),
                    (0, 300001, 'Napoleón Bonaparte', 00337874389, '-', '40 Rue de Colisee', 'Isle de France', 'Paris', 'France', 75008);
                    

INSERT INTO Invoices (ID, Invoices_id, date, Car, Customer, Salesperson)
	VALUES (0, 852399038, '2018-08-22', '3K096I98581DHSNUP', 'Abraham Lincoln','Gail Forcewind'),
			(0, 731166526, '2018-12-31', 	'HKNDGS7CU31E9Z7JW', 'Pablo Picasso', 'Bob Frapples'),
			(0,	271135104, '2019-01-22', 'RKXVNNIHLVVZOUB4M', 'Napoleón Bonaparte', 'Shonda Leer');
        

INSERT INTO Salespersons (ID, Salespersons_id, Name, Store)
	VALUES (0, 00001, 'Petey Cruiser', 'Madrid'),
			(0, 00002, 	'Anna Sthesia', 'Barcelona'),
			(0, 00003,	'Paul Molive', 'Berlin'),
			(0, 00004,	'Gail Forcewind', 'Paris'),
			(0, 00005,	'Paige Turner', 'Mimia'),
			(0, 00006,	'Bob Frapples', 'Mexico City'),
			(0,	00007,	'Walter Melon', 'Amsterdam'),
			(0, 00008,	'Shonda Leer', 'São Paulo');