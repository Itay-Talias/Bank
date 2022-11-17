import React from "react";
import { useState,useEffect } from "react";
import axios from "axios"
import "../style/Operations.css"


function Operations(props) {
        const [categories,setCategories]=useState([])
        useEffect(()=>{
                axios.get('http://localhost:8080/categories/').then(res=>{setCategories(res.data)})
            },[])

        const [inputValues,setInputValues]=useState({amount:0,vendor:"",category:"init"})
        const inputHandler=(e)=>{
                const newInputValues={...inputValues}
                let newValue=e.target.value
                if(e.target.name==="amount"){
                        newValue=Math.abs(newValue)
                }
                newInputValues[e.target.name]=newValue
                console.log(newInputValues)
                setInputValues(newInputValues)
        }
        const clickHandler=(e)=>{
                if(inputValues.amount !== "" && inputValues.vendor !== "" && inputValues.category!=="init"){
                        axios.post('http://localhost:8080/transactions/',
                        {
                                user_id:props.user.user_id,
                                amount: e.target.name==="withdraw"? -(inputValues.amount) : inputValues.amount,
                                category: inputValues.category,
                                vendor: inputValues.vendor
                        })
                        setInputValues({amount:0,vendor:"",category:""})
                        props.fetchUser()
                }
                
        }
    return( 
        <div className="Operations">
                <h2 className="opertaions-title">Insert Transaction</h2>
                <label>Transaction amount</label>
                <input name="amount" type="number" className="amount-input" min="0" value={inputValues.amount} onChange={inputHandler} />
                <label>Transaction vendor</label>
                <input name="vendor" className="vendor-input" placeholder="TRANSACTION VEDOR" value={inputValues.vendor} onChange={inputHandler}/>
                <label>Transaction category</label>
                <select name="category" className="category-input" value={inputValues.category} onChange={inputHandler}>
                        <option value="init">Select category</option>
                        {categories.map(c=><option value={c} selected>{c}</option>)}
                </select>
                <button className="deposit-button" name="deposit" onClick={clickHandler} >Deposit</button>
                <button className="withdraw-button" name="withdraw" onClick={clickHandler}>Withdraw</button>
        </div>
        );
}

export default Operations;
