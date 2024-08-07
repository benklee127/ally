import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import "./Home.css";

function ProfileButton({ user }) {
  const sessionUser = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

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

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <div onClick={openMenu} className="profile-button">
        {sessionUser.profile_photo ? (
          <img src={sessionUser.profile_photo} />
        ) : (
          <i className="fas fa-user-circle" />
        )}
      </div>
      <div className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <div className="profile-menu-item">{user.username}</div>
            <div className="profile-menu-item">{user.email}</div>
            <div className="profile-menu-item">
              <div onClick={handleLogout} className="profile-menu-button">
                Log Out
              </div>
            </div>
          </>
        ) : null}
      </div>
    </>
  );
}

export default ProfileButton;
