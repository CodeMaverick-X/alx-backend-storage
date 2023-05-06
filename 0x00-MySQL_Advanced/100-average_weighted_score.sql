-- a SQL script that creates a stored procedure 
-- ComputeAverageWeightedScoreForUser that computes
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    SELECT `corrections`.`score`, `projects`.`weight` / 100 as `weight`
    FROM `corrections` INNER JOIN `projects`
    ON `corrections`.`project_id` = `projects`.`id`
    
END $$
