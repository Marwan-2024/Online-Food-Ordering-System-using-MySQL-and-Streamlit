-- To display the number of customers who have ordered from a particular restaurant. 

DELIMITER $$
CREATE FUNCTION customer_no(rest varchar(20))
RETURNS integer
DETERMINISTIC
BEGIN
 declare c_count int; 
 select count(DISTINCT(C_ID)) into c_count
 from order_details O
 where rest  = O.R_ID;
 return c_count;
END;
$$
DELIMITER ;


SELECT DISTINCT R_ID, customer_no(R_ID) FROM restaurant;
