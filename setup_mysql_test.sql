-- Create development database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create development user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges for dev user in dev database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privileges for dev user in performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Reload privileges
FLUSH PRIVILEGES;
