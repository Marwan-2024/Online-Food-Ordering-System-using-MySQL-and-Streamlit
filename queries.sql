-- JOIN QUERIES
-- 1
-- Display the address to which the delivery person has to deliver to.
SELECT Delivery.Del_ID, Delivery.Del_Person_Name, Customer.Address
FROM Delivery
INNER JOIN Customer ON Customer.C_ID=Delivery.C_ID;

-- 2
-- Display the restaurant name and corresponding menu items.
SELECT Restaurant.R_ID, Restaurant.Name, Menu.Item_Name 
FROM Restaurant
LEFT JOIN Menu ON Restaurant.R_ID=Menu.R_ID;

-- 3
-- Retrieve customer ID, name, and contact who have not completed the payment
SELECT Customer.C_ID, Customer.Name, Customer.Contact
FROM Customer
JOIN Order_Details 
WHERE Customer.C_ID=Order_Details.C_ID AND Order_Details.Payment_Status!= "Success";

-- 4
-- Retrieve all the menu items corresponding to an order.
SELECT Order_Details.O_ID, Menu.M_ID, Menu.Item_Name
FROM Order_Details
JOIN Order_Items ON Order_Details.O_ID=Order_Items.O_ID
JOIN Menu ON Order_Items.M_ID=Menu.M_ID
ORDER BY Order_Details.O_ID;


-- AGGREGATE FUNCTIONS
-- 1
-- Calculate the total amount for each order placed. 
SELECT O_ID, SUM(Price) 
FROM order_items 
      GROUP BY O_ID;

-- 2
-- Find the number of orders placed for each restaurant.
SELECT Restaurant.R_ID, count(DISTINCT(Order_Details.O_ID)) 
FROM Restaurant 
LEFT JOIN Order_Details on Order_Details.R_ID=Restaurant.R_ID
GROUP BY Restaurant.R_ID;

-- 3 
-- Find the maximum-priced item in restaurant R1.
SELECT R_ID, M_ID, Item_Name, Price
FROM menu
WHERE Price in (SELECT MAX(Price)
			    FROM menu 
			    WHERE R_ID='R1')
       AND R_ID='R1';

-- 4
-- Find the number of menu items in each restaurant.
SELECT Restaurant.R_ID, COUNT(Menu.R_ID) 
FROM Restaurant 
LEFT JOIN Menu ON Restaurant.R_ID = Menu.R_ID
GROUP BY Restaurant.R_ID;


-- SET OPERATORS
-- 1
-- Display Menu items, R_ID,M_ID of type burgers or price less than 200
SELECT R_ID, M_ID, Item_Name, Price
FROM Menu
WHERE Type="Burgers" 
UNION
SELECT R_ID, M_ID, Item_Name, Price
FROM Menu
     WHERE Price<=200;

-- 2
-- Display restaurants in J.P. that are active
SELECT R_ID, Name
FROM Restaurant
WHERE Address LIKE 'J%'
INTERSECT
SELECT R_ID, Name
FROM Restaurant
WHERE isActive="Yes";

--3 
-- Display customers whose total amount was at least 600 but corresponding ordered places is not from R1
SELECT C_ID, R_ID, Amount
FROM Order_Details
WHERE Amount>=600
EXCEPT
SELECT C_ID, R_ID, Amount
FROM Order_Details
WHERE R_ID="R1";

-- 4 
-- Display all transactions through UPI has not been completed/failed.
SELECT O_ID, Payment_Status, Amount
FROM Order_Details
WHERE Payment_Mode="UPI"
INTERSECT
SELECT O_ID, Payment_Status, Amount
FROM Order_Details
WHERE Payment_Status!="Success"

