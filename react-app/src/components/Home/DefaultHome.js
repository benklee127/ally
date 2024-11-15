import { useEffect, useState } from 'react'
import { useHistory } from 'react-router-dom'
import './Home.css'
import { Link } from 'react-router-dom';
import homebackground from "../../assets/homebackground.png";
import { useSelector } from "react-redux";
import { useDispatch } from "react-redux";
import { login } from "../../store/session";

export default function DefaultHome() {
    const history = useHistory();
    const dispatch = useDispatch();
    // let currentBGI = 0;

    const demoUser = () => {
      return dispatch(login("demo@aa.io", "password"));
    };

    return (

            <div className="dh-wrapper">
            <div className="dh-topbar">
            <i class="fa-solid fa-cat"></i>&nbsp; Sign in | Ally
            </div>

            <div className="dh-main-wrapper">
              <div className="dh-main">
                <div>
                <i class="fa-solid fa-cat"></i> Ally


                </div>
                <div>insert cool slogan</div>
                <div className='dh-main-buttons'>
                  <button onClick={()=>history.push('/signup')}>Sign up</button>
                  <button onClick={()=>history.push('/login')}>Log in</button>
                  <button onClick={demoUser}>Demo user</button>
                </div>
              </div>
              <div className="dh-main-image">
                <img src={homebackground} className="homebackground" />
              </div>
            </div>
          </div>
    )
}
