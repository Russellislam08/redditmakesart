import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Images from "./components/images";

class App extends Component {
  render() {
    return (
      <div id="root">
        <div className="hero is-fullheight is-bold is-info">
          <div className="topnav nav-content">
            <h2 className="title">
              reddit<span class="makes">makes</span>art
            </h2>
          </div>
          <div className="hero-body">
            <div className="container">
              <Images />
              <div className="sidebar">
                <p>
                  This is a website that showcases original art content made by
                  reddit users on the r/art subreddit
                </p>
                <p>Some other cool subreddits:</p>
                <ul>
                  <li>r/art</li>
                  <li>r/dota2</li>
                  <li>r/cscareerquestions</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
