import React,{ useState,useEffect } from "react";
import axios from "axios"
import TransactionCard from "./TransactionCard";
import "../style/Transactions.css"


function Transactions(props) {
    const [transactions, setTransactions] = useState([]);

    const fetchTransaction=async()=>{
        const res = await axios.get('http://localhost:8080/transactions/')
        setTransactions(res.data)
    }

    useEffect(()=>{
        fetchTransaction()
    },[])

    return <div className="transactions">{transactions.map((t,i)=><TransactionCard key={i} transaction={t} fetchTransaction={fetchTransaction} fetchUser={props.fetchUser} />)}</div>;
}

export default Transactions;
