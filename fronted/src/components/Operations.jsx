import React from "react";
import "../style/Operations.css"


function Operations(props) {
    return( 
        <div className="Operations">
                <h2 className="opertaions-title">Insert Transaction</h2>
                <input type="number" className="amount-input" placeholder="TRANSACTION AMOUNT" min="0"/>
                <input className="vendor-input" placeholder="TRANSACTION VEDOR"/>
                <input className="category-input" placeholder="TRANSACTION CATEGORY"/>
                <button className="deposit-button">Deposit</button>
                <button className="withdraw-button">Withdraw</button>
        </div>
        );
}

export default Operations;
