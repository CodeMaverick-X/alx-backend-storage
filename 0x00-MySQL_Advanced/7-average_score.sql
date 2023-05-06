-- SQL script that creates a stored procedure `ComputeAverageScoreForUser`
-- that computes and store the average score for a student
DELIMITER $$
CREATE
DEFINER = CURRENT_USER
PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)
COMMENT 'TAKES USER ID'
LANGUAGE SQL
DETERMINISTIC
BEGIN
	DECLARE average INTEGER;
	SET average = (SELECT AVG(`score`) FROM `corrections`
		       WHERE corrections.user_id=user_id);
	UPDATE users
	SET average_score = average
	WHERE id=user_id;
END$$
