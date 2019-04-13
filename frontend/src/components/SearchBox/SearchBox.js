import React from 'react';

const SearchBox = ({ search }) => {
    return (
        <div className='pa2'>
            <input 
                className='ba pa0 bg-lightest-blue'
                type='search' 
                placeholder='Search Shows' 
                onChange={search}
            />
        </div>
    );
}

export default SearchBox;