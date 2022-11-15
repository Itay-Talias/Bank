import React from "react";
import "../style/TransactionCard.css"
const transction={
    transaction_id:2,
    amount:200,
    category:"food",
    vendor:"chips",
    is_depoist: true
}

function TransactionCard(props) {
    return( 
        <div className={`transaction-card ${transction.is_depoist ? "positive" : "negative"}`}>
            <div className="text-card">
                <h4>Amount: {transction.amount}</h4>
                <h5>Category: {transction.category}</h5>
                <h6>Vendor: {transction.vendor}</h6>
            </div>
        </div>);
}

export default TransactionCard;
