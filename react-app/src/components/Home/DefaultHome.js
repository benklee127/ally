import { useEffect, useState } from 'react'
import { useHistory } from 'react-router-dom'
import './Home.css'
import { Link } from 'react-router-dom';

export default function DefaultHome() {
    const history = useHistory();
    // let currentBGI = 0;


    return (
      <div>
        Splash page
        <div>
          <Link to="/signup" style={{ textDecoration: 'none' }}><button>Sign up</button></Link>
          <Link  to="/login" style={{ textDecoration: 'none' }}><button>Log in</button></Link>
        </div>
      </div>
    )
}
