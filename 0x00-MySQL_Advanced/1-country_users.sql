-- creates a table `users` with teh following fields
-- id, email, name, country
CREATE TABLE IF NOT EXISTS users(
	id INTEGER AUTO_INCREMENT NOT NULL UNIQUE,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US'
	);
