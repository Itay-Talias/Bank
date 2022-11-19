import React from "react";
import "../style/TransactionCard.css"
import axios from "axios"


function TransactionCard(props) {
    const deleteTransaction=()=>{
        axios.delete(`http://localhost:8080/transactions/${props.transaction.transaction_id}`)
        .then(()=>{props.fetchTransaction().then(()=>props.fetchUser())})
    }
    return( 
        <div className={`transaction-card ${props.transaction.amount >0 ? "positive" : "negative"}`}>
            <div className="text-card">
                <h4>Amount: {props.transaction.amount}</h4>
                <h5>Category: {props.transaction.category}</h5>
                <h6>Vendor: {props.transaction.vendor}</h6>
                <button className="transactionC-delete-button" onClick={deleteTransaction}>Delete</button>
            </div>
        </div>
        );
}

export default TransactionCard;
