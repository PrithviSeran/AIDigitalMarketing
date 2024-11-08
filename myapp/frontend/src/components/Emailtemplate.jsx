import Heading from "./Heading"
import Button from "./Button"
import Input from "./Input"
import ButtonGradient from "../assets/svg/ButtonGradient";
import axios from "axios";
import React, { useState, useRef } from 'react';



const Emailtemplate = (emailContent) => {

  const emailToRef = useRef();
  const subjectRef = useRef();
  const bodyRef = useRef();


  const SendEmail = (emailTo, subject, body) => {

    const response = axios.get("http://localhost:8000/wel/sendemail/",{
        params: {
          emailTo: emailTo,
          subject: subject,
          body: body
        }
      }
    ).then((res) => {
      alert("Your Email has been Sent")
    })


  }

  return (
    <div className="w-[55%] h-[85vh]">

        <Heading
        title="Auto Generated Email"
        />

        <div className="flex flex-col justify-center align-center">

            <h2 className="text-center" >Organization's Email</h2>
            <Input
            inputRef={emailToRef}/>

            <h2 className="text-center" >Subject</h2>
            <Input
            inputRef={subjectRef}/>

            <h2 className="text-center" >Body</h2>
            <Input
            textArea = "textarea"
            value = {emailContent}
            inputRef={bodyRef}
            />
            
            <div className="text-center">
                <Button
                className="w-[17em]"
                onClick={() => SendEmail(emailToRef.current.value, subjectRef.current.value, bodyRef.current.value)}>
                    Send Email
                </Button>
            </div>
        </div>

        <ButtonGradient/>

    </div>
  )
}

export default Emailtemplate
