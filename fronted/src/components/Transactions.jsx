import React,{ useState,useEffect } from "react";
import axios from "axios"
import TransactionCard from "./TransactionCard";
import "../style/Transactions.css"
import Transaction from "../model/Transaction";
import consts from "../model/Consts";


function Transactions(props) {
    const [transactions, setTransactions] = useState([]);

    const fetchTransactions=async()=>{
        const res = await axios.get(consts.TRANSACTION_URL)
        setTransactions(res.data.map(t=>new Transaction(t.user_id,t.amount,t.category,t.vendor,t.transaction_id)))
    }

    useEffect(()=>{
        fetchTransactions()
    },[])

    return <div className="transactions">
        {transactions.map((t,i)=><TransactionCard key={i} transaction={t} fetchTransactions={fetchTransactions} fetchUser={props.fetchUser} />)}
            </div>;
}

export default Transactions;
