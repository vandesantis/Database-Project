import React from 'react';
import UserShowList from './UserShowList/UserShowList';

class UserProfile extends React.Component {
    // constructor() {
    //     super();
    // }

    render() {
        let { openShowPage } = this.props;
        return (
            <div>
                {/* <h1>TV Show List</h1> */}
                <UserShowList openShowPage = {openShowPage}/>
            </div>
        );
      }
}

export default UserProfile;