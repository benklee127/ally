import { useSelector, useDispatch } from "react-redux";
import { useEffect, useRef, useState } from "react";
import { logout } from "../../store/session";
import { getAllImageThunk } from "../../store/image";
import { Link, useHistory } from "react-router-dom";
import "./UserHome.css";
import OpenModalButton from "../OpenModalButton";
import {
  getUserFavImgThunk,
  deleteUserFavImgThunk,
  addUserFavThunk,
} from "../../store/image";
import Favorites from "../Favorites";
import Collection from "../Collections";

export default function UserHome() {
  const sessionUser = useSelector((state) => state.session.user);
  const ulRef = useRef();
  const [showMenu, setShowMenu] = useState(false);
  const currDate = new Date();
  const [info, setInfo] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();


  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  useEffect(() => {

  }, [dispatch]);

  //onMouseOver={showInfo(image.id)} onMouseLeave={notShowInfo(image.id)}
  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    // closeMenu()
    history.push('/')
    };

  return (
    <div>Logged in home
      <div></div>
      <button className='log-out' onClick={handleLogout}>Log out</button>
      <Collection></Collection>
    </div>
  );
}
