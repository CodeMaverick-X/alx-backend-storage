-- sql script that contains a stored procedure `AddBonus`
-- that adds a new corr for a student
DELIMITER $$
CREATE
DEFINER = CURRENT_USER
PROCEDURE AddBonus ( IN user_id INTEGER, IN project_name varchar(255), IN score INTEGER)
COMMENT 'aded corr for student'
LANGUAGE SQL
DETERMINISTIC
BEGIN
	DECLARE project_id INTEGER;
	SET project_id = (SELECT id FROM projects WHERE `name`=project_name);
	IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END$$
