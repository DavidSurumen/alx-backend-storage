-- creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
DROP TRIGGER IF EXISTS update_items;
CREATE TRIGGER update_items AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	-- access the data from the orders table
	DECLARE itm_name VARCHAR(255);
	DECLARE number INT;
	SET itm_name = NEW.item_name;
	SET number = NEW.number;

	-- update the items table based on the trigger logic
	UPDATE items SET quantity = quantity - number WHERE name = itm_name;
END$$
