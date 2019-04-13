import React from 'react';
// import './TVShowPage.css';

const TVShowPage = ({ title, genre, rating, synopsis, fcc }) => {
    return (
        <div>
            <h1>{title}</h1>
            <p>genre: {genre}</p>
            <p>rating: {rating}</p>
            <p>synopsis: {synopsis}</p>
            <p>fcc: {fcc}</p>
        </div>
    );
}

export default TVShowPage;