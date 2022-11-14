SELECT_TRANSACTIONS_BY_ID = """SELECT * FROM Transactions_info WHERE user_id=%s"""

ADD_TRANSACTION = """INSERT INTO Transactions_info (amount,category,vendor,is_depoist,user_id) VALUES(%s,%s,%s,%s,%s)"""

DELETE_TRANSACTION = """DELETE FROM Transactions_info WHERE transaction_id = %s"""

SELECT_ALL_CATEGORIES = """SELECT * FROM Categories_info"""
