-- script thqt creates a table 'users' of unique users.
DROP TABLE IF EXISTS users;
CREATE TABLE users(
        `id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `email` VARCHAR(255) NOT NULL UNIQUE,
        `name` VARCHAR(255)
);
