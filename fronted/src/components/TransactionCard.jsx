import React from "react";
import "../style/TransactionCard.css"


function TransactionCard(props) {
    return( 
        <div className={`transaction-card ${props.transaction.amount >0 ? "positive" : "negative"}`}>
            <div className="text-card">
                <h4>Amount: {props.transaction.amount}</h4>
                <h5>Category: {props.transaction.category}</h5>
                <h6>Vendor: {props.transaction.vendor}</h6>
            </div>
        </div>
        );
}

export default TransactionCard;
