class Transaction {
    constructor(userId, amount, category, vendor, transactionId) {
        this.userId = userId;
        this.amount = amount;
        this.category = category;
        this.vendor = vendor;
        this.transactionId = transactionId;
    }
}

export default Transaction;
