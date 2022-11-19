import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import React,{ useState,useEffect } from "react";
import Transactions from "./components/Transactions";
import Operations from "./components/Operations"
import axios from "axios"
import User from "./model/User";
import Breakdown from "./components/Breakdown"

function App() {
    const [user, setUser] = useState({});
    const fetchUser=()=>{
        axios.get('http://localhost:8080/users/1').then(res=>{
            setUser(new User(res.data.user_id,res.data.username,
                res.data.password,res.data.balance))})
    }
    useEffect(()=>{
        fetchUser()
    },[]
    )

    return (
        <Router>
                <div className="App">
                    <div id="home-background"></div>
                    <NavBar user={user}></NavBar>
                    <Route path="/" exact render={() => <Transactions user={user} fetchUser={fetchUser}/>} />
                    <Route path="/operations" exact render={() => <Operations user={user} fetchUser={fetchUser}/>} />
                    <Route path="/breakdown" exact render={() => <Breakdown/>} />
                </div>
        </Router>
    );
}

export default App;
