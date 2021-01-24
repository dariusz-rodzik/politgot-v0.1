import React, { Component } from "react";
import AnswerQuestions from "./AnswerQuestions";
import { BrowserRouter as Router,  Switch, Route, Link, Redirect} from "react-router-dom"


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
        <Router>
            <Switch>
                <Route exact path="/"><p>This is a home page</p></Route>
                <Route path="/choose" component={AnswerQuestions} />
            </Switch>
        </Router>
        );
    }
}
