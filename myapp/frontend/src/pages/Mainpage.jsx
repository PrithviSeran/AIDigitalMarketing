import Heading from "../components/Heading";
import Section from "../components/Section";
import { BackgroundCircles, BottomLine, Gradient } from "../components/design/Hero";
import Input from "../components/Input"
import Button from "../components/Button";
import ButtonGradient from "../assets/svg/ButtonGradient";
import Createcampaign from "../components/Createcampaign";
import Yourcampaigns from "../components/Yourcampaigns";
import Pageheader from "../components/Pageheader";
import axios from "axios";
import React, { useState, useRef, useEffect } from 'react';
import { useLocation } from 'react-router-dom';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const Mainpage = () => {

  const location = useLocation()

  const [campaigns, setCampaigns] = useState(location.state || []);

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/ws/campaigns/');

    socket.onopen = () => {
      console.log('WebSocket connection established');
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log('Message from server:', data.message);
      setCampaigns((prevCampaigns) => [...prevCampaigns, data.message]);
    };

    return () => {
      socket.close(); // Clean up the WebSocket when component unmounts
    };
  }, []);

  return (
    <div className="flex flex-row">

        <Pageheader/>

        <Yourcampaigns campaigns={campaigns} />

        <Createcampaign setCampaigns={setCampaigns}/>

        <ButtonGradient/>
        
    </div>
  )
}

export default Mainpage
