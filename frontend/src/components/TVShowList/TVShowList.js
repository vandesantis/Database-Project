import React from 'react';
import TVShowEntry from '../TVShowEntry/TVShowEntry';
import './TVShowList.css';

const exampleData = {
    data: [
        {
            title: "game of thrones",
            genre: "action",
            rating: "N/A",
            synopsis: "dragons and stuff",
            fcc: "TV-MA"
        },
        {
            title: "Breaking bad",
            genre: "action",
            rating: "N/A",
            synopsis: "meth",
            fcc: "TV-MA"
        }
    ]
}

class TVShowList extends React.Component {
    render() {
        const filteredData = exampleData.data.filter((tvShow, i) => {
            return tvShow.title.toLowerCase().includes(this.props.searchfield.toLowerCase());
        });
    
        const tvShowArray = filteredData.map((tvShow, i) => {
            return (
                <TVShowEntry 
                    key={tvShow.title}
                    openShowPage={this.props.openShowPage}
                    title={tvShow.title}
                    genre={tvShow.genre}
                    rating={tvShow.rating}
                    synopsis={tvShow.synopsis}
                    fcc={tvShow.fcc}/>
            )
        });

        return (
            <table>
                <tbody>
                    <tr className='table-header'>
                        <td>Title</td>
                        <td>Genre</td>
                        <td>Rating</td>
                    </tr>
                    { tvShowArray }
                </tbody>
            </table>
        );
    }
}

export default TVShowList;