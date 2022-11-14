SELECT_ALL_TRANSACTIONS = """SELECT * FROM Transactions_info"""

ADD_TRANSACTION = """INSERT INTO Transactions_info (amount,category,vendor,is_depoist) VALUES(%s,%s,%s,%s)"""

DELETE_TRANSACTION = """DELETE FROM Transactions_info WHERE transaction_id = %s"""
