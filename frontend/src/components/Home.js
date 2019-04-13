import React from 'react';
import TVShowList from './TVShowList/TVShowList';

class Home extends React.Component {
    // constructor() {
    //     super();
    // }

    render() {
        let { searchfield, openShowPage, changeRoute } = this.props;
        return (
            <div>
                {/* <h1>TV Show List</h1> */}
                <TVShowList searchfield = {searchfield} openShowPage = {openShowPage}/>
                <p onClick={() => changeRoute('newShowForm')} className='pointer dim'>Add show to database</p>
            </div>
        );
      }
}

export default Home;