//rafce
import Heading from "./Heading";
import Section from "./Section";
import { BackgroundCircles, BottomLine, Gradient } from "./design/Hero";
import Input from "./Input"
import Button from "./Button";
import React, { useState, useRef } from 'react';
import axios from "axios";
import Cookies from 'js-cookie';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const Createcampaign = ({ setCampaigns }) => {

    const nameOfCampaign = useRef();
    const infoAbtYourself = useRef();
    const purposeOfTheCampaign = useRef();
    const campaignTarget = useRef();

    const handleCreateCampaign = () => {

        let name = nameOfCampaign.current.value
        let info = infoAbtYourself.current.value
        let purpose = purposeOfTheCampaign.current.value
        let target = campaignTarget.current.value

        try {
            const response = axios.get('http://localhost:8000/wel/createcampaign/', {
                params: {
                    name,
                    use: 'personal',
                    user_info: info,
                    purpose,
                    target_audience: target,
                  },
                }).then((res)=>{
                    console.log("New Campaign: ", res.data.campaigns);
                    // Optionally, update campaigns immediately in the UI
                    setCampaigns(res.data.campaigns);

                })
          
                // WebSocket will handle real-time updates too
              } catch (error) {
                console.error('Error creating campaign: ', error);
              } 
    }

  return (
    <div className=" w-[60%]">
        <Section id="features">
        <Heading
        className="md:max-w-md lg:max-w-2xl pt-[3em]"
        title="Create a Campaign"
        />
        <div className=" container relative z-2">
            <div className=" flex flex-wrap gap-10 mb-5 flex-col" style={{
                    backgroundImage: `url(./src/assets/benefits/create-campiagn.svg)`
                }}>

                <div className="text-center pt-7 px-0">
                    <h1 className="text-[1.2em] pb-2">Whats the name of this campaign?</h1>

                    <Input
                    id = "Name"
                    placeholder= "Name of Campaign"
                    type="text"
                    inputRef = {nameOfCampaign}
                    />

                    <h1 className="text-[1.2em] pb-2">Add information about yourself that would be important to your clients</h1>

                    <Input
                    id = "Info"
                    placeholder= "Information About Yourself"
                    type="text"
                    textArea="textarea"
                    inputRef = {infoAbtYourself}
                    />

                    <h1 className="text-[1.2em] pb-2">What is the purpose of this campaign?</h1>

                    <Input
                    id = "prupose"
                    placeholder= "Purpose of the Campaign"
                    type="text"
                    textArea="textarea"
                    inputRef = {purposeOfTheCampaign}
                    />

                    <h1 className="text-[1.2em] pb-2">Who are the people that your are trying to target?</h1>

                    <Input
                    id = "target"
                    placeholder= "Who Are You Trying to Target?"
                    type="text"
                    textArea="textarea"
                    inputRef = {campaignTarget}
                    />
                    <div className="text-center mb-5">
                        <Button onClick = {handleCreateCampaign} className="w-[30em] text-center">
                            Create Campaign
                        </Button>
                    </div>
                </div>
            </div>
            
        </div>
        <BackgroundCircles />
        </Section>
    </div>
  )
}

export default Createcampaign


// Menu redesigns for restaurants 

// I have worked as a graphic designer for 5 years. 

// I want to redesign the menu cards of seafood restaurants in Whitby.

// Seafood restaurants in Whitby.

/*
- **Website revamps for local bookstores**
- **I have worked as a web developer for 4 years.**
- **I want to improve the online presence of independent bookstores in Toronto.**
- **Independent bookstores in Toronto.**
*/

/*Here’s another example with a similar structure but a different topic:

- **Fitness program development for athletes**
- **I have worked as a personal trainer for 5 years.**
- **I want to create specialized workout plans for marathon runners in Toronto.**
- **Marathon runners in Toronto.**

*/