import React from "react";

export default class Form extends React.Component {
  state = {
    name: "",
    location: "",
    date: "",
    time: "",
    gender: "",
    age: "",
    request_type: "OPC",
    description: ""
  };

  defaultState = {
    name: "",
    location: "",
    date: "",
    time: "",
    gender: "",
    age: "",
    request_type: "OPC",
    description: ""
  };

  change = e => {
    this.props.onChange({ [e.target.name]: e.target.value });
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  onSubmit = e => {
    e.preventDefault();
    // TODO: jsonify <state> and send to server
    // TODO: Should take you to the matching page

    // this.setState(this.defaultState);
    // this.props.onChange(this.defaultState);

    console.log(state)
  };

  render() {
    return (
      <form>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          placeholder="Name of request"
          value={this.state.name}
          onChange={e => this.change(e)}
        />
        <br />

        <label htmlFor="location">Location:</label>
        <input
          type="text"
          id="location"
          name="location"
          placeholder="City"
          value={this.state.location}
          onChange={e => this.change(e)}
        />
        <br />

        <label htmlFor="date">Date:</label>
        <input
          id="date"
          type="date"
          name="date"
          value={this.state.date}
          onChange={e => this.change(e)}
        />
        <br />

        <label htmlFor="time">Time:</label>
        <input
          id="time"
          type="time"
          name="time"
          value={this.state.time}
          onChange={e => this.change(e)}
        />
        <br />

        <label htmlFor="age">Age:</label>
        <input
          id="age"
          type="number"
          name="age"
          value={this.state.age}
          onChange={e => this.change(e)}
          min="1"
          max="100"
        />
        <br />

        <label>Gender:</label>
        <input
          type="radio"
          id="male"
          name="gender"
          value="male"
          onChange={e => this.change(e)}
        />
        <label htmlFor="male">Male</label>
        <input
          type="radio"
          id="female"
          name="gender"
          value="female"
          onChange={e => this.change(e)}
        />
        <label htmlFor="female">Female</label>
        <input
          type="radio"
          id="other"
          name="gender"
          value="other"
          onChange={e => this.change(e)}
        />
        <label htmlFor="other">Other</label>
        <br />

        <label htmlFor="type">Request type:</label>
        <select id="type" name="request_type" onChange={e => this.change(e)}>
          <option value="OPC">Phone call</option>
          <option value="OQC">Quick chat</option>
          <option value="OQE">Quick errand</option>
        </select>
        <br />

        <label htmlFor="desc">Description:</label>
        <textarea
          id="desc"
          rows="4"
          cols="50"
          name="description"
          value={this.state.description}
          onChange={e => this.change(e)}
        ></textarea>
        <br />

        <button onClick={e => this.onSubmit(e)}>Submit Request</button>
      </form>
    );
  }
}
