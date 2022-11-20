import React,{ useState,useEffect } from "react";
import axios from "axios"
import TransactionCard from "./TransactionCard";
import "../style/Transactions.css"
import Transaction from "../model/Transaction";


function Transactions(props) {
    const [transactions, setTransactions] = useState([]);

    const fetchTransaction=async()=>{
        const res = await axios.get('http://localhost:8080/transactions/')
        setTransactions(res.data.map(t=>new Transaction(t.user_id,t.amount,t.category,t.vendor,t.transaction_id)))
    }

    useEffect(()=>{
        fetchTransaction()
    },[])

    return <div className="transactions">{transactions.map((t,i)=><TransactionCard key={i} transaction={t} fetchTransaction={fetchTransaction} fetchUser={props.fetchUser} />)}</div>;
}

export default Transactions;
