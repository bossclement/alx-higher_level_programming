-- changes hbtn_0c_0 database to UTF8
-- change database to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- change table to utf8
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- change a field in a table to utf8
ALTER TABLE hbtn_0c_0.first_table MODIFY `name` VARCHAR(256) DEFAULT NULL;
