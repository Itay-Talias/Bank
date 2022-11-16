import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import React,{ useState,useEffect } from "react";
import Transactions from "./components/Transactions";
import Operations from "./components/Operations"
import axios from "axios"
import User from "./Model/User";

function App() {
    const [user, setUser] = useState(new User());
    useEffect(()=>{
        axios.get('http://localhost:8080/users/1').then(res=>{setUser(new User(res.data.user_id,res.data.username,res.data.password,res.data.balance))})
    },[])
    return (
        <Router>
                <div className="App">
                    <div id="home-background"></div>
                    <NavBar balance={user.balance}></NavBar>
                    <Route path="/" exact render={() => <Transactions/>} />
                    <Route path="/operations" exact render={() => <Operations/>} />

                </div>
        </Router>
    );
}

export default App;
