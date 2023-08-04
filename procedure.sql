-- 1
-- To calculate each item’s price based on the quantity ordered. 

DELIMITER $$
CREATE PROCEDURE items_price()
BEGIN

 UPDATE order_items AS OI JOIN menu AS M ON OI.M_ID=M.M_ID
 SET OI.price = OI.quantity*M.price;
 
END$$
DELIMITER ;

CALL items_price();

SELECT * FROM order_items;


-- 2
-- To calculate the total amount of each order a customer has to pay for the order placed.

DELIMITER $$
CREATE PROCEDURE cal_tot()
BEGIN

UPDATE order_details AS OD JOIN (SELECT O_ID, SUM(Price) AS val  
                                 FROM order_items 
                                 GROUP BY O_ID) AS X ON OD.O_ID=X.O_ID
SET OD.Amount = X.val;
END$$
DELIMITER ;

CALL cal_tot();

SELECT * FROM `order_details`
