
import Campaigncontent from "../components/Campaigncontent"
import Section from "../components/Section"
import Heading from "../components/Heading"
import Button from "../components/Button"
import Input from "../components/Input"
import Stackelement from "../components/Stackelement"
import { useLocation } from 'react-router-dom';
import React, { useState, useRef, useEffect } from 'react';
import ButtonGradient from "../assets/svg/ButtonGradient";
import Pageheader from "../components/Pageheader";
import { useNavigate } from "react-router-dom";
import { BackgroundCircles } from "../components/design/Hero"
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const Campaign = () => {

  const location = useLocation()

  const [shouldConnect, setShouldConnect] = useState(false);

  let navigate = useNavigate();


  const [campaign, setCampaign] = useState(location.state.campaign || []);
  const [domains, setDomains] = useState(location.state.domains || []);


  const getDomains = () => {

    console.log("Clicked! ")

    const socket = new WebSocket('ws://localhost:8000/ws/ok/');

    socket.onopen = () => {
      socket.send(JSON.stringify({ message: campaign.id}));

    }

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log('Message from server:', data.message);
      setDomains(data.message);
    };

  }

  const handleDomain = (domain) => {

    navigate('/business',{
      state: {
        domain: domain,
        campaign: campaign
      }
  })

  }

  return (
    <div className="flex flex-row gap-4">

        <Pageheader/>
        
          <Campaigncontent
              campaign = {campaign}
              />

          <div className="w-[55%] h-[80vh] mt-15">
              <div className="flex flex-col">

                <Heading 
                className="md:max-w-md lg:max-w-2xl pt-[3em] text-center"
                title="Search for Businesses"
                />
                  <div className="mb-4 flex flex-row gap-4 justify-center align-center">

                      <Button onClick={getDomains}>
                        Find Businesses
                      </Button>

                  </div>

                  <div className="flex flex-col overflow-auto max-h-[75vh] gap-3 justify-center mx-5">

                    {domains.map((domain) => (
                        <Stackelement
                        title = {domain.domain}
                        onClick = {() => handleDomain(domain)}
                        />
                    ))}

                  </div>

              </div>
          </div>
        
        <ButtonGradient/>
      
    </div>
    
  )
}

export default Campaign
