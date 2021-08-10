-- Create development database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- select dev database
USE hbnb_dev_db;

-- Create development user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges for dev user in dev database
GRANT ALL PRIVILEGES ON hbnb_dev.* TO 'hbnb_dev'@'localhost';

-- Grant select privileges for dev user in performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
