import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import { useState } from "react";
import TransactionsPage from "./components/TransactionsPage";

function App() {
    const [balance, setBalance] = useState(1000);
    return (
        <Router>
            <div className="App">
                <div id="home-background"></div>
                <NavBar balance={balance}></NavBar>
                <TransactionsPage />
                {/* <Route
                    exact
                    path="/"
                    render={() => <Home users={this.state.users} />}
                /> */}
            </div>
        </Router>
    );
}

export default App;
