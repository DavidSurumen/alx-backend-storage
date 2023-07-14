-- creates a stored procedure that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE sum_weight INT;
	DECLARE sum_weighted_score INT;

	SELECT SUM(projects.weight) INTO sum_weight
	FROM corrections
		INNER JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	SELECT SUM(corrections.score * projects.weight) INTO sum_weighted_score
	FROM corrections
		INNER JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	IF sum_weight = 0 THEN
		UPDATE users
		SET users.average_score = 0
		WHERE users.id = user_id;
	ELSE
		UPDATE users
		SET users.average_score = sum_weighted_score / sum_weight
		WHERE users.id = user_id;
	END IF;
END $$
DELIMITER ;
