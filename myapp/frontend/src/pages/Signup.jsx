import Heading from "../components/Heading";
import Section from "../components/Section";
import { BackgroundCircles, BottomLine, Gradient } from "../components/design/Hero";
import Input from "../components/Input"
import Button from "../components/Button";
import ButtonGradient from "../assets/svg/ButtonGradient";
import axios from "axios";
import React, { useState, useRef } from 'react';
import validator from 'validator';
import { useNavigate } from "react-router-dom";


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


const Signup = () => {

    const [showMessage, setShowMessage] = useState(false);
    const [errorMessage, setErrorMessage] = useState("")

    const usernameRef = useRef();
    const emailRef = useRef();
    const password1Ref = useRef();
    const password2Ref = useRef();

    let navigate = useNavigate();

    const RegisterUser = () => {

        let email = emailRef.current.value
        let username = usernameRef.current.value
        let password1 = password1Ref.current.value
        let password2 = password2Ref.current.value

        if (!validator.isEmail(email) || username == '' || password1 == '' || password2 == ''){

            setShowMessage(true)
            setErrorMessage("Please fill all fields!")
        }

        else{

            const response = axios.get('http://localhost:8000/wel/signup/', {
                params:{
                    email: email,
                    username: username,
                    password1: password1,
                    password2: password2
                }
            }).then((res) => {

                if (res.data.message != true){

                    setShowMessage(true)
                    setErrorMessage(res.data.message)

                }
                else{
                    navigate('/main')
                }
            })
        }
    }

    return( 
    <Section id="features">
      <div className="flex flex-row gap-2 container relative z-2">
        <div className="flex flex-wrap gap-5 mb-5 flex-col" style={{
                backgroundImage: `url(./src/assets/benefits/sign-up.svg)`
            }}>
            <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em]"
            title="Create Account"
            />
            <Input
            id = "Name"
            placeholder= "Please enter your Name"
            type="text"
            inputRef={usernameRef}
            />
            <Input
            id = "Email"
            placeholder= "Please enter your Email"
            type="text"
            inputRef={emailRef}
            />
            <Input
            id = "Password"
            placeholder= "Please enter your password"
            type="password"
            inputRef={password1Ref}
            />
            <Input
            id = "Password Again"
            placeholder= "Please enter your password again"
            type="password"
            inputRef={password2Ref}
            />
             { showMessage &&
                (<div>
                    <p className="text-red-500 text-center"> {errorMessage} </p>
                </div>)
            }   
            <div className="text-center p-5">
                <Button className="w-[30em] text-center"
                onClick={RegisterUser}>
                    Create Account
                </Button>
            </div>
        </div>

        <div>
            <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em]"
            title="Already have an account? Sign-in."
            />

            <div className="text-center mb-[3em]">
                <Button className="w-[30em] text-center">
                    Sign-in
                </Button>
            </div>
        </div>
        
      </div>
      <BackgroundCircles />
      <ButtonGradient />
    </Section>
    );
}

export default Signup;