import * as React from "react";
import { useState,useEffect } from "react";
import axios from "axios"
import "../style/Operations.css"
import Snackbart from "./Snackbar";
import consts from "../model/Consts"



function Operations(props) {
        const [openSnackbar, setOpenSnackbar] = useState(false);
        const [alertType,setAlertType]=useState(consts.SUCCESS)
        const [categories,setCategories]=useState([])
        const [inputValues,setInputValues]=useState({amount:consts.INIT_NUMBER,vendor:consts.INIT_STRING,category:consts.INIT_CATEGORY})

        useEffect(()=>{
                axios.get(consts.CATEGORIES_URL).then(res=>{setCategories(res.data)})
            },[])

        const inputHandler=(e)=>{
                const newInputValues={...inputValues}
                let newValue=e.target.value
                if(e.target.name==="amount"){
                        newValue=Math.abs(newValue)
                }
                newInputValues[e.target.name]=newValue
                setInputValues(newInputValues)
        }
        const clickHandler=(e)=>{
                if(inputValues.amount !== consts.INIT_NUMBER && inputValues.vendor !== consts.INIT_STRING && inputValues.category!==consts.INIT_CATEGORY){
                        axios.post(consts.TRANSACTION_URL,
                        {
                                user_id:props.user.user_id,
                                amount: e.target.name==="withdraw"? -(inputValues.amount) : inputValues.amount,
                                category: inputValues.category,
                                vendor: inputValues.vendor
                        }).then(()=>{setInputValues({amount:consts.INIT_NUMBER,vendor:consts.INIT_STRING,category:consts.INIT_CATEGORY})
                        props.fetchUser()})
                        setAlertType(consts.SUCCESS)
                }
                else{
                        setAlertType(consts.ERROR)
                }                
                setOpenSnackbar(true)
        }
        console.log(alertType)
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
                <Snackbart open={openSnackbar} setOpen={setOpenSnackbar} alert={alertType}></Snackbart>
        </div>
        );
}

export default Operations;
