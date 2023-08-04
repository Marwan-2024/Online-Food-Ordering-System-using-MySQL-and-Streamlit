-- To ensure the quantity for which the order is placed is not less than 1.

DELIMITER $$
CREATE TRIGGER check_quant
BEFORE INSERT
ON order_items FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
DECLARE n int;
SET error_msg = ('Minimum quantity is 1');
SET n = (SELECT new.quantity);
IF n<1 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg; 
END IF; 
END $$
DELIMITER ;

INSERT INTO ORDER_ITEMS VALUES ("OI10", "O2", "M2", "","");
