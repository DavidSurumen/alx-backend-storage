-- creates a stored procedure that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE projs_count INT DEFAULT 0;
	DECLARE sum_score INT DEFAULT 0;

	SELECT COUNT(*) INTO projs_count
	FROM corrections WHERE corrections.user_id = user_id;

	SELECT SUM(score) INTO sum_score
	FROM corrections WHERE corrections.user_id = user_id;

	UPDATE users SET users.average_score = IF(projs_count = 0, 0, sum_score / projs_count) WHERE id = user_id;
END $$
DELIMITER ;
