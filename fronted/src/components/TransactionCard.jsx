import React from "react";
import "../style/TransactionCard.css"
import axios from "axios"
import consts from "../model/Consts"


function TransactionCard(props) {
    const deleteTransaction=()=>{
        axios.delete(`${consts.TRANSACTION_URL}${props.transaction.transactionId}`)
        .then(()=>{props.fetchTransactions().then(()=>props.fetchUser())})
    }
    return( 
        <div className="transaction-card">
            <div className="text-card">
                <h4 className={`${props.transaction.amount >0 ? "positive-text" : "negative-text"}`}>{props.transaction.amount}$</h4>
                <h4>{props.transaction.category}</h4>
                <h4>{props.transaction.vendor}</h4>
                <button className="transactionC-delete-button" onClick={deleteTransaction}>Delete</button>
            </div>
        </div>
        );
}

export default TransactionCard;
