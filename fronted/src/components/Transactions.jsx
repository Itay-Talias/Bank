import React,{ useState,useEffect } from "react";
import axios from "axios"
import TransactionCard from "./TransactionCard";
import "../style/Transactions.css"


function Transactions(props) {
    const [transactions, setTransactions] = useState([]);
    useEffect(()=>{
        axios.get('http://localhost:8080/transactions/').then(res=>{setTransactions(res.data)})
    },[])

    return <div className="transactions">{transactions.map((t,i)=><TransactionCard key={i} transaction={t} />)}</div>;
}

export default Transactions;
