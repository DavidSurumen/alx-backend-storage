-- creates a stored procedure that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE proj_id INT DEFAULT 0;
	DECLARE proj_count INT DEFAULT 0;

	SELECT COUNT(id) INTO proj_count FROM projects WHERE name = project_name;

	IF proj_count = 0 THEN
		INSERT INTO projects(name) VALUES (project_name);
	END IF;

	SELECT id INTO proj_id FROM projects WHERE name = project_name;

	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, proj_id, score);
END $$
DELIMITER ;
