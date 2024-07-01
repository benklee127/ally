import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import './LoginForm.css';
import { Link } from "react-router-dom";
import { useModal } from "../../context/Modal";

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);


  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const demoUser = () => {
    return dispatch(login(
      'demo@aa.io',
      'password',
    ))
  }

  return (
    <>
      <div className="loggin">
        <div className="login-box">

        <div className="form-container">
        <form className='login-form' onSubmit={handleSubmit}>
          <div className="form-text">Login page</div>
          <ul>
            {errors.map((error, idx) => (
              <li key={idx}>{error}</li>
            ))}
          </ul>
          <label>
            <input
              type="email"
              placeholder="Email Address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <label>
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          <div className="login">
            <button type="submit">Submit</button>
          </div>
          <Link  to="/login" style={{ textDecoration: 'none' }}><button>Sign up</button></Link>

        </form>
           <div className="login-demo">
            <button type='submit' onClick={demoUser}>Demo User</button>
          </div>
        </div>
        </div>
      </div>
    </>
  );
}

export default LoginFormPage;
