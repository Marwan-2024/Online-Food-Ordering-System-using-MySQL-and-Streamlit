CREATE DATABASE IF NOT EXISTS ONLINE_FOOD_ORDERING_SYSTEM;

CREATE TABLE IF NOT EXISTS CUSTOMER
(
    C_ID varchar(20),
    Name varchar(50),
    Address varchar(50),
    Email varchar(20),
    Username varchar(30), 
    Password varchar(10),
    DOB date,
    Contact varchar(15),
    PRIMARY KEY (C_ID)
);

CREATE TABLE IF NOT EXISTS DELIVERY
(
    Del_ID varchar(20),
    C_ID varchar(20),
    Del_Status varchar(10),
    Del_Person_Name varchar(50),
    Del_Person_Contact varchar(15),
    Date date,
    PRIMARY KEY (Del_ID),
    FOREIGN KEY (C_ID) REFERENCES CUSTOMER(C_ID)
);

CREATE TABLE IF NOT EXISTS RESTAURANT
(
    R_ID varchar(20),
    Name varchar(50),
    Address varchar(50),
    Descp varchar(50),
    isActive varchar(3), 
    Opening_hrs time,
    Closing_hrs time,
    Email varchar(20),
    Contact varchar(15),
    PRIMARY KEY (R_ID)
);


CREATE TABLE IF NOT EXISTS MENU
(
    M_ID varchar(20),
    R_ID varchar(20),
    Item_Name varchar(20),
    Price float,
    Type varchar(20), 
    Descp varchar(50),
    PRIMARY KEY (M_ID),
    FOREIGN KEY (R_ID) REFERENCES RESTAURANT(R_ID)
);

CREATE TABLE IF NOT EXISTS ORDER_DETAILS
(
    O_ID varchar(20),
    C_ID varchar(50),
    R_ID varchar(20),
    Del_ID varchar(20),
    Amount float,
    Payment_Mode varchar(20),
    Payment_Status varchar(10), 
    Date date,
    PRIMARY KEY (O_ID),
    FOREIGN KEY (C_ID) REFERENCES CUSTOMER(C_ID),
    FOREIGN KEY (R_ID) REFERENCES RESTAURANT(R_ID),
    FOREIGN KEY (Del_ID) REFERENCES DELIVERY(Del_ID)
);

CREATE TABLE IF NOT EXISTS ORDER_ITEMS
(
    OItems_ID varchar(20),
    O_ID varchar(50),
    M_ID varchar(20),
    Quantity int,
    Price float,
    PRIMARY KEY (OItems_ID),
    FOREIGN KEY (O_ID) REFERENCES ORDER_DETAILS(O_ID),
    FOREIGN KEY (M_ID) REFERENCES MENU(M_ID)
);



ALTER TABLE CUSTOMER ADD UNIQUE (Email);
ALTER TABLE CUSTOMER ADD UNIQUE (Username);



