-- Conver the hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- convert all of the following to UTF8:
-- *	Database	`hbtn_0c_0`
-- *	Table		`first_table`
-- *	Field		`first_table`

-- Alter the database
ALTER DATABASE `hbtn_0c_0` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- Alter the table
USE `hbtn_0c_0`;
ALTER TABLE `first_table` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- Alter a field
ALTER TABLE `first_table`
CHANGE `name` `name` VARCHAR(256) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';
