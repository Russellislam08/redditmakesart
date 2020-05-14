import React, { Component } from "react";
import {
  Container,
  Navbar,
  Nav,
  NavDropdown,
  Form,
  FormControl,
  Button,
} from "react-bootstrap";
import logo from "./logo.svg";
import "./App.css";
import Images from "./components/images";

class App extends Component {
  render() {
    return (
      <div id="root">
        <Navbar expand="lg" fixed="top" className="topnav">
          <Container className="topnav-container">
            <Navbar.Brand className="brand" href="/">
              reddit<span class="makes">makes</span>art
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="ml-auto nav-content">
                <Nav.Link
                  href="https://github.com/Russellislam08/redditmakesart"
                  className="mr-sm-2"
                >
                  github
                </Nav.Link>
                <Nav.Link href="https://www.reddit.com/r/art">r/art</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>

        <Container>
          <Images />
        </Container>
      </div>
    );
  }
}

export default App;
