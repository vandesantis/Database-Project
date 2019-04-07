import React from 'react';
import './TVShowEntry.css';

const TVShowEntry = ({ openShowPage, title, genre, rating, synopsis, fcc }) => {
    return (
        <tr class='home-list'>
            <td><p onClick={() => openShowPage(title, genre, rating, synopsis, fcc)} className='title'>{title}</p></td>
            <td className='genre'>{genre}</td>
            <td className='rating'>{rating}</td>
        </tr>
    );
}

export default TVShowEntry;