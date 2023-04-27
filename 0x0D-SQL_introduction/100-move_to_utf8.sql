-- Convert a databasee to UTF8MB4, COLLATE UTF8MB4_UNICODE_CI
ALTER DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SELEECT CONVERT (`name` USING utf8mb4) AS `name` FROM `first_table`;
