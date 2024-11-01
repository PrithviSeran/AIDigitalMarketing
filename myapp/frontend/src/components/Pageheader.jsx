import { useLocation } from "react-router-dom";
import { disablePageScroll, enablePageScroll } from "scroll-lock";
import axios from "axios";
import { brainwave } from "../assets";
import { navigation } from "../constants";
import Button from "./Button";
import MenuSvg from "../assets/svg/MenuSvg";
import { HamburgerMenu } from "./design/Header";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


const Pageheader = () => {

    let navigate = useNavigate();

    const logoutUser = () =>{

        const response = axios.post('http://localhost:8000/wel/logout/').then((res) => {
            navigate("/")
            console.log(res)
        })

    };

    return (
      <div
        className={`fixed top-0 left-0 w-full z-50 border-b border-n-6 lg:bg-n-8/90 lg:backdrop-blur-sm flex justify-between items-center p-4`}
      >
        {/* Add any left-aligned content here, such as a title or logo */}
  
        <Button onClick = {logoutUser} className="hidden lg:flex ml-auto">
          Log out
        </Button>
      </div>
    );
  };
  
  export default Pageheader;