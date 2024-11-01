import Businesscontent from "../components/Businesscontent"
import Emailtemplate from "../components/Emailtemplate"
import { useLocation } from 'react-router-dom';
import ButtonGradient from "../assets/svg/ButtonGradient"; 
import React, { useState, useRef } from 'react';
import axios from "axios";


const Business = () => {

  const location = useLocation()

  const { domain, campaign } = location.state

  const [emailContent, setEmailContent] = useState("")

  const [email, setEmail] = useState("")

  const responseEmailContent = axios.get("http://localhost:8000/wel/getemailcontent/",  {
    params:{
      content: domain.content,
      user_info: campaign.user_info,
      purpose: campaign.purpose
    }

  }).then((res) => {
    setEmailContent(res.data.email_content)
    console.log(emailContent)
  })

  const responseEmail = axios.get("http://localhost:8000/wel/getemail/", {
    params:{
      content: domain.content
    }

  }).then((res) => {
    setEmail(res.data.email)
    console.log("Email: ", email)
  })

  return (
    <div className="flex flex-row">
        <Businesscontent
            business = {domain} 
            />

        <Emailtemplate
        emailContent = {emailContent}
        />
      
    </div>
  )
}

export default Business
