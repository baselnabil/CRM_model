-- Active: 1726051192272@@127.0.0.1@3306@crm
CREATE TABLE IF NOT EXISTS customers (  
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    company_name VARCHAR(10) NOT NULL,
    email VARCHAR(15),
    address VARCHAR(20),
    phone INT  )


CREATE TABLE IF NOT EXISTS debts (
    id INT AUTO_INCREMENT PRIMARY KEY ,
    debt_amount DECIMAL(20,5) NOT NULL ,
    company_name VARCHAR(20),
    employee VARCHAR(10),
    debt_date DATE NOT NULL ,
    debt_due DATE NOT NULL)



