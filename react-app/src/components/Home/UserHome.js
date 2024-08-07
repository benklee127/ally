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
import ProfileButton from "./ProfileButton";

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
    <div>
      <div className="navbar-wrapper">
        <div className="home-topbar">
          <i class="fa-solid fa-cat"></i>&nbsp;Ally
        </div>
        <div className="prof-button-wrapper">
          {<ProfileButton user={sessionUser} />}
        </div>
    </div>
      <Collection></Collection>
    </div>
  );
}
