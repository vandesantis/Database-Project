import React from 'react';
import './Navigation.css';

const Navigation = ({ changeRoute }) => {
    return (
        <nav className=''>
            <ul className='nav'>
                <li className='start'><p onClick={() => changeRoute('home')} className='pointer dim'>TV Show List</p></li>
                <li><p onClick={() => changeRoute('user')} className='mr4 pointer dim'>Profile</p></li>
                <li><p onClick={() => changeRoute('login')} className='mr4 pointer dim'>Login</p></li>
                <li><p onClick={() => changeRoute('signup')} className='mr3 pointer dim'>Sign Up</p></li>
            </ul>

{/* 
            <div className='start'>
                <p onClick={() => changeRoute('home')} className='logo pointer'>TV Show List</p>
            </div>
            <div className='end'>
                <p onClick={() => changeRoute('login')} className='login dim'>Login</p>
                <p onClick={() => changeRoute('signup')} className='pointer dim'>Sign Up</p>
            </div> */}
        </nav>
    );
}

export default Navigation;