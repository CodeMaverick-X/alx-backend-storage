-- sql script that creates a trigger that resets the
-- attr valid_email only when the email has been changed,
DELIMITER $$
CREATE
DEFINER = CURRENT_USER
TRIGGER email_check BEFORE UPDATE
ON `users` FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END$$
