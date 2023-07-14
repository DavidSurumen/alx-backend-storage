-- creates a stored procedure that computes and stores the average weighted score for all students
-- in the database 'holberton'
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	ALTER TABLE users ADD sum_weight INT DEFAULT 0;
	ALTER TABLE users ADD sum_weighted_score INT DEFAULT 0;

	UPDATE users
	SET sum_weight = (
		SELECT SUM(projects.weight)
		FROM corrections
		INNER JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = users.id
	);

	UPDATE users
	SET sum_weighted_score = (
		SELECT SUM(corrections.score * projects.weight)
		FROM corrections
		INNER JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = users.id
	);

	UPDATE users
	SET users.average_score = IF(users.sum_weight = 0, 0, users.sum_weighted_score / users.sum_weight);
	ALTER TABLE users DROP COLUMN sum_weighted_score;
	ALTER TABLE users DROP COLUMN sum_weight;
END $$
DELIMITER ;
