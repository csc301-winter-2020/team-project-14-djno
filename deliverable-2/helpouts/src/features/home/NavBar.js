import React, { Component } from 'react';

export default class NavBar extends Component {
  static propTypes = {};

  render() {
    return (
      <nav className="home-nav-bar">
        <a class="active" href="#">
          Home
        </a>
        <a href="#">Chat</a>
        <a href="#">Profile</a>
      </nav>
    );
  }
}
