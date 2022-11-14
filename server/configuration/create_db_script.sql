CREATE DATABASE IF NOT EXISTS sql_bank;

USE sql_bank;

-- -----------------------------------------------------
-- Table `sql_bank`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS Transactions_info(
    transaction_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    amount INT NOT NULL,
    category VARCHAR(50) NOT NULL,
    vendor VARCHAR(50) NOT NULL,
    is_depoist BOOLEAN NOT NULL
);

