import React from "react";
import "./App.css";
// import Form from "./components/Form.js";
import Form2 from "./components/Form2.js";

class App extends React.Component {
  state = {
    fields: {}
  };

  onChange = updatedValue => {
    this.setState({
      fields: {
        ...this.state.fields,
        ...updatedValue
      }
    });
  };

  render() {
    return (
      <div className="App">
        <h1>Settings</h1>
        {/* <Form onChange={fields => this.onChange(fields)} /> */}
        <Form2 onChange={fields => this.onChange(fields)} />
        {/* <p>{JSON.stringify(this.state.fields, null, 2)}</p> */}
      </div>
    );
  }
}

export default App;
