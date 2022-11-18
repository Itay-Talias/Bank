SELECT_TRANSACTION_BY_ID = """SELECT * FROM Transactions_info WHERE transaction_id = %s"""

SELECT_TRANSACTIONS_BY_USER_ID = """SELECT * FROM Transactions_info WHERE user_id = %s"""

ADD_TRANSACTION = """INSERT INTO Transactions_info (amount,category,vendor,user_id) VALUES(%s,%s,%s,%s)"""

DELETE_TRANSACTION = """DELETE FROM Transactions_info WHERE transaction_id = %s"""

SELECT_ALL_CATEGORIES = """SELECT * FROM Categories_info"""

UPDATE_BALANCE_BY_ID = """UPDATE Users_info SET balance = %s WHERE user_id = %s"""

SELECT_USER_BY_ID = """SELECT * FROM Users_info WHERE user_id = %s"""

GROUP_BY_CATEGORY = """SELECT category , sum(amount) FROM Transactions_info GROUP BY category"""
