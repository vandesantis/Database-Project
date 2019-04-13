import React from 'react';
import TVShowEntry from '../UserShowEntry/UserShowEntry';
// import './UserShowList.css';

const exampleData = {
    data: [
        {
            title: "game of thrones",
            genre: "action",
            watchingStatus: "currently watching",
            rating: "9",
            synopsis: "dragons and stuff",
            fcc: "TV-MA"
        },
        {
            title: "Breaking bad",
            genre: "action",
            watchingStatus: "competed",
            rating: "10",
            synopsis: "meth",
            fcc: "TV-MA"
        },
        {
            title: "other show",
            genre: "comedy",
            watchingStatus: "competed",
            rating: "6",
            synopsis: "people",
            fcc: "TV-MA"
        }
    ]
}

class UserShowList extends React.Component {
    // constructor() {
    //     super();
    // }

    tvShowArray = exampleData.data.map((tvShow, i) => {
        return (
            <TVShowEntry openShowPage={this.props.openShowPage}
                title={tvShow.title}
                genre={tvShow.genre}
                watchingStatus={tvShow.watchingStatus}
                rating={tvShow.rating}
                synopsis={tvShow.synopsis}
                fcc={tvShow.fcc}/>
        )
    });

    render() {
        return (
            <table>
                <tr class='table-header'>
                    <td>Title</td>
                    <td>Genre</td>
                    <td>Watching Status</td>
                    <td>Rating</td>
                </tr>
                { this.tvShowArray }
            </table>
        );
    }
}

export default UserShowList;