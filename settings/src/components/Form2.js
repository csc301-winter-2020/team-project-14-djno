import React from "react";

export default class Form2 extends React.Component {
  defaultState = {
    gps: 0,
    Monday: 0,
    Tuesday: 0,
    Wednesday: 0,
    Thursday: 0,
    Friday: 0,
    Saturday: 0,
    Sunday: 0,
    morning: 0,
    afternoon: 0,
    evening: 0,
    REN: 0,
    RES: 0,
    RENA: 0,
    RESA: 0,
    RHN: 0,
    RHS: 0,
    RLN: 0,
    RLS: 0,
    RWL: 0,
    RPUD: 0,
    RPUO: 0,
    RHMS: 0
  };

  state = {
    gps: 0,
    Monday: 0,
    Tuesday: 0,
    Wednesday: 0,
    Thursday: 0,
    Friday: 0,
    Saturday: 0,
    Sunday: 0,
    morning: 0,
    afternoon: 0,
    evening: 0,
    REN: 0,
    RES: 0,
    RENA: 0,
    RESA: 0,
    RHN: 0,
    RHS: 0,
    RLN: 0,
    RLS: 0,
    RWL: 0,
    RPUD: 0,
    RPUO: 0,
    RHMS: 0
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
    // TODO: jsonify <state> and send to server
    // TODO: Should take you to the home page

    // this.setState(this.defaultState);
    // this.props.onChange(this.defaultState);
    console.log(this.state)
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
          name="Monday"
          checked={this.state.Monday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="tues">Tuesday</label>
        <input
          type="checkbox"
          id="tues"
          name="Tuesday"
          checked={this.state.Tuesday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="wed">Wednesday</label>
        <input
          type="checkbox"
          id="wed"
          name="Wednesday"
          checked={this.state.Wednesday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="thurs">Thursday</label>
        <input
          type="checkbox"
          id="thurs"
          name="Thursday"
          checked={this.state.Thursday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="fri">Friday</label>
        <input
          type="checkbox"
          id="fri"
          name="Friday"
          checked={this.state.Friday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="sat">Saturday</label>
        <input
          type="checkbox"
          id="sat"
          name="Saturday"
          checked={this.state.Saturday}
          onChange={e => this.onChange(e)}
        />
        <label htmlFor="sun">Sunday</label>
        <input
          type="checkbox"
          id="sun"
          name="Sunday"
          checked={this.state.Sunday}
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
        <h3>Services willing to provide:</h3>
        <label htmlFor="REN">Education Navigation</label>
        <input
          type="checkbox"
          id="REN"
          name="REN"
          checked={this.state.REN}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RES">Education Support</label>
        <input
          type="checkbox"
          id="RES"
          name="RES"
          checked={this.state.RES}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RENA">Employment Navigation</label>
        <input
          type="checkbox"
          id="RENA"
          name="RENA"
          checked={this.state.RENA}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RESA">Employment Support</label>
        <input
          type="checkbox"
          id="RESA"
          name="RESA"
          checked={this.state.RESA}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RHN">Health care Navigation</label>
        <input
          type="checkbox"
          id="RHN"
          name="RHN"
          checked={this.state.RHN}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RHS">Health care Support</label>
        <input
          type="checkbox"
          id="RHS"
          name="RHS"
          checked={this.state.RHS}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RLN">Local Navigation</label>
        <input
          type="checkbox"
          id="RLN"
          name="RLN"
          checked={this.state.RLN}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RLS">Local Support</label>
        <input
          type="checkbox"
          id="RLS"
          name="RLS"
          checked={this.state.RLS}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RWL">Wellbeing/leisure</label>
        <input
          type="checkbox"
          id="RWL"
          name="RWL"
          checked={this.state.RWL}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RPUD">Pick up and delivery</label>
        <input
          type="checkbox"
          id="RPUD"
          name="RPUD"
          checked={this.state.RPUD}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RPUO">Pick up and drop off</label>
        <input
          type="checkbox"
          id="RPUO"
          name="RPUO"
          checked={this.state.RPUO}
          onChange={e => this.onChange(e)}
        />
        <br />
        <label htmlFor="RHMS">Homemaking supports</label>
        <input
          type="checkbox"
          id="RHMS"
          name="RHMS"
          checked={this.state.RHMS}
          onChange={e => this.onChange(e)}
        />
        <br />

        <button onClick={e => this.onSubmit(e)}>Update Settings</button>
      </form>
    );
  }
}
