import React from "react";

import axios from "axios";

export default class UserList extends React.Component {
  state = {
    users: [],
  };

  componentDidMount() {
    axios.get(`/api/`).then((res) => {
      const users = res.data;
      this.setState({ users });
    });
  }

  render() {
    return (
      <ul>
        {this.state.users.map((user) => (
          <li>
            {user.username} - {user.email}
          </li>
        ))}
      </ul>
    );
  }
}
