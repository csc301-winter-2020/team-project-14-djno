import React from "react";

export default class Form extends React.Component {
  state = {
    gps: 0,
    monday: 0,
    tuesday: 0,
    wednesday: 0,
    thursday: 0,
    friday: 0,
    saturday: 0,
    sunday: 0,
    morning: 0,
    afternoon: 0,
    evening: 0,
    phone_call: 0,
    quick_connect: 0,
    quick_task: 0
  };

  onChange = e => {
    const isChecked = e.target.checked;
    const name = e.target.name;
    const value = isChecked ? 1 : 0;
    this.props.onChange({ [name]: value });
    this.setState({
      [name]: value
    });
  };

  onSubmit = e => {
    e.preventDefault();
    if (
      !this.state.phone_call &&
      !this.state.quick_connect &&
      !this.state.quick_task
    ) {
      alert("You must choose at least one preference!");
      return;
    }
    // TODO: jsonify <state> and send to server
    // TODO: Should take you to the home page
    this.setState({
      gps: 0,
      monday: 0,
      tuesday: 0,
      wednesday: 0,
      thursday: 0,
      friday: 0,
      saturday: 0,
      sunday: 0,
      morning: 0,
      afternoon: 0,
      evening: 0,
      phone_call: 0,
      quick_connect: 0,
      quick_task: 0
    });
    this.props.onChange({
      gps: 0,
      monday: 0,
      tuesday: 0,
      wednesday: 0,
      thursday: 0,
      friday: 0,
      saturday: 0,
      sunday: 0,
      morning: 0,
      afternoon: 0,
      evening: 0,
      phone_call: 0,
      quick_connect: 0,
      quick_task: 0
    });
  };

  render() {
    return (
      <form>
        <label htmlFor="gps">GPS/location sharing</label>
        <input
          type="checkbox"
          id="gps"
          name="gps"
          checked={this.state.gps}
          onChange={e => this.onChange(e)}
        />
        <h3>Availability</h3>
        <label>Days: </label>
        <label htmlFor="mon">Monday</label>
        <input
          type="checkbox"
          id="mon"
          name="monday"
          checked={this.state.monday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="tues">Tuesday</label>
        <input
          type="checkbox"
          id="tues"
          name="tuesday"
          checked={this.state.tuesday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="wed">Wednesday</label>
        <input
          type="checkbox"
          id="wed"
          name="wednesday"
          checked={this.state.wednesday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="thurs">Thursday</label>
        <input
          type="checkbox"
          id="thurs"
          name="thursday"
          checked={this.state.thursday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="fri">Friday</label>
        <input
          type="checkbox"
          id="fri"
          name="friday"
          checked={this.state.friday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="sat">Saturday</label>
        <input
          type="checkbox"
          id="sat"
          name="saturday"
          checked={this.state.saturday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="sun">Sunday</label>
        <input
          type="checkbox"
          id="sun"
          name="sunday"
          checked={this.state.sunday}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label>Time of day: </label>
        <label htmlFor="morn">Morning</label>
        <input
          type="checkbox"
          id="morn"
          name="morning"
          checked={this.state.morning}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="aft">Afternoon</label>
        <input
          type="checkbox"
          id="aft"
          name="afternoon"
          checked={this.state.afternoon}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="eve">Evening</label>
        <input
          type="checkbox"
          id="eve"
          name="evening"
          checked={this.state.evening}
          onChange={e => this.onChange(e)}
        />
        <h3>Available Category:</h3>
        <label htmlFor="call">Phone call/chat</label>
        <input
          type="checkbox"
          id="call"
          name="phone_call"
          checked={this.state.phone_call}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="qc">Quick* connect</label>
        <input
          type="checkbox"
          id="qc"
          name="quick_connect"
          checked={this.state.quick_connect}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="qt">Quick* task</label>
        <input
          type="checkbox"
          id="qt"
          name="quick_task"
          checked={this.state.quick_task}
          onChange={e => this.onChange(e)}
        />
        <br />
        <button onClick={e => this.onSubmit(e)}>Update Settings</button>
      </form>
    );
  }
}
