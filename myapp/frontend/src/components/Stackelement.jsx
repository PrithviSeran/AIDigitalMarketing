import { useNavigate } from "react-router-dom";
import React, { useState, useRef, useEffect } from 'react';


const Stackelement = ({ title, onClick }) => {

  return (
    
    <button onClick = {onClick} className="py-[0.3em] px-[0.3em] mx-[1em] bg-color-5 bg-opacity-[30%] rounded-[1.2em] bg-gradient-to-r from-blue-500 to-purple-500 text-white ">
        <span className="flex w-full h-full bg-gray-900 text-white rounded-[0.75em] py-[1.5em] px-[1em] transition ease-in-out delay-150 hover:bg-opacity-0 duration-300 h5">
            {title}
        </span>
    </button>
    
  )
}

export default Stackelement
