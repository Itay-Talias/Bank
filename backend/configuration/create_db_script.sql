CREATE DATABASE IF NOT EXISTS sql_bank;

USE sql_bank;

-- -----------------------------------------------------
-- Table `sql_bank`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Users_info(
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    balance VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Transactions_info(
    transaction_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    amount INT NOT NULL,
    category VARCHAR(50) NOT NULL,
    vendor VARCHAR(50) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Users_info(user_id)
);

CREATE TABLE IF NOT EXISTS Categories_info(
    category VARCHAR(50) NOT NULL PRIMARY KEY
);


INSERT INTO Categories_info VALUES("Transportation");
INSERT INTO Categories_info VALUES("Food");
INSERT INTO Categories_info VALUES("Entertainment");
INSERT INTO Users_info VALUES(1,"itay","123456",1000);
INSERT INTO Transactions_info VALUES(1,-10,"Transportation","bus",1);
INSERT INTO Transactions_info  VALUES(2,-100,"Food","cat food",1);
INSERT INTO Transactions_info VALUES(3,-200,"Entertainment","cat toys",1);
INSERT INTO Transactions_info VALUES(4,1700,"Entertainment","cat video on tiktok",1);



