import React, { Component } from "react";
import { Link } from "react-router-dom";
import "../style/NavBar.css";

class NavBar extends Component {
    render() {
        return (
            <div className="topnav">
                <Link to="/">Home</Link>
                <Link to="/">Catalog</Link>
                <img
                    id="bank-logo"
                    src="https://www.pngitem.com/pimgs/m/101-1016890_icon-bank-logo-png-transparent-png.png"
                    alt="bank-logo"
                ></img>
            </div>
        );
    }
}

export default NavBar;
