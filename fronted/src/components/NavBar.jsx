import React from "react";
import { Link } from "react-router-dom";
import "../style/NavBar.css";

function NavBar(props) {
    console.log(props.user)
    return (
        <div className="topnav">
            <Link to="/">Transactions</Link>
            <Link to="/operations">Operations</Link>
            <Link to="/">Breakdown</Link>
            <div
                className={`balance-navbar ${
                    props.user.balance > 0 ? "positive" : "negative"
                }`}
            >
                BALANCE:{props.user.balance}
            </div>
            <img
                id="bank-logo"
                src="https://www.pngitem.com/pimgs/m/101-1016890_icon-bank-logo-png-transparent-png.png"
                alt="bank-logo"
            ></img>
        </div>
    );
}

export default NavBar;
