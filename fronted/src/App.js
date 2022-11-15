import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import NavBar from "./components/NavBar";

function App() {
    return (
        <Router>
            <div className="App">
                <div id="home-background"></div>
                <NavBar></NavBar>
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
