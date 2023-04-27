-- Convert a databasee to UTF8MB4, COLLATE UTF8MB4_UNICODE_CI
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `hbtn_0c_0`;

ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- SELECT CONVERT (`name` USING utf8mb4) AS `name` FROM `first_table`;
