import Heading from "./Heading";
import Section from "./Section";
import Stackelement from "./Stackelement";
import { BackgroundCircles, BottomLine, Gradient } from "./design/Hero";
import Input from "./Input"
import Button from "./Button";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import React, { useState, useRef, useEffect } from 'react';


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


const Yourcampaigns = (campaigns) => {

  let navigate = useNavigate();

  const [domains, setDomains] = useState([])
  const [currentCampaign, setCurrentCampaign] = useState(null);

  const handleCampaign = (campaign) => {

    const response = axios.get("http://localhost:8000/wel/domains/",{
        params: {
          id: campaign.id
        }
      }
    ).then((res) => {
        setDomains(res.data.domains)
        setCurrentCampaign(campaign);
    })
  }

  useEffect(() => {
    if (domains.length && currentCampaign) {
      navigate("/campaign", {
        state: {
          campaign: currentCampaign,
          domains: domains,
        },
      });
    }
  }, [domains, currentCampaign, navigate]);

  return (
    <div className="w-[40%]">
        <Section id="features">
        <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em]"
            title="Your Campaigns"
            />
        <div className="flex flex-col gap-7 overflow-auto max-h-[75vh]">

            {campaigns.campaigns.map((campaign) => (
                 <Stackelement
                 title = {campaign.name}
                 onClick = {() => handleCampaign(campaign)}
                 />
            ))}

        </div>
        </Section>
    </div>
  )
}

export default Yourcampaigns
