import React, { Component } from "react";
import { Container } from "react-bootstrap";
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
            <div class="topnav-right title">
              <a href="#search">Search</a>
              <a href="#about">About</a>
            </div>
          </div>
          <Container>
            <Images />
          </Container>
        </div>
      </div>
    );
  }
}

export default App;
