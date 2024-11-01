import Heading from "../components/Heading";
import Section from "../components/Section";
import { BackgroundCircles, BottomLine, Gradient } from "../components/design/Hero";
import Input from "../components/Input"
import Button from "../components/Button";
import ButtonGradient from "../assets/svg/ButtonGradient";
import Header from "../components/Header";
import axios from "axios";
import GoogleButton from "react-google-button";
import React, { useState, useRef } from 'react';
import { useNavigate } from "react-router-dom";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


const Login = () => {

    const [currentUser, setCurrentUser] = useState(null);
    const [showMessage, setShowMessage] = useState(false);
    const [errorMessage, setErrorMessage] = useState("")

    const usernameRef = useRef();
    const passwordRef = useRef();

    let username = ""
    let password = ""

    let errMessage = ""

    let navigate = useNavigate();

    const userCheck = axios.get('http://localhost:8000/wel/login/').then((res) => {
        if (res.data.message){
            navigate('/main',{
                state: res.data.campaigns
            })
        }
    })

    const handleSubmit = () => {

        username = usernameRef.current.value
        password = passwordRef.current.value

        try {
            const response = axios.post('http://localhost:8000/wel/login/', {

                username: username,
                password: password

              })
              .then((res) => {

                setCurrentUser(true); // Assuming true indicates successful logi

                errMessage = res.data.message

                if (errMessage == true){

                    console.log(res.data.campaigns)

                    navigate('/main', {
                        state: res.data.campaigns
                    })
                }
                else{

                    setShowMessage(true)
                    setErrorMessage(errMessage)
                }
              })
              
        } catch (error) {
            console.error('Error logging in', error);
        }

    };

    return( 
    <Section id="features">
      <div className="container relative z-2">
        <div className="flex flex-wrap gap-10 mb-5 flex-col bg-no-repeat bg-cover bg-center" style={{
                backgroundImage: `url(./login-card.svg)`
            }}>
            <Heading
            className="md:max-w-md lg:max-w-2xl pt-[1em]"
            title="Sign In"
            />
            <Input
            id = "Email"
            placeholder= "Please enter your Email"
            type="text"
            inputRef = {usernameRef}
            />
            <Input
            id = "Password"
            placeholder= "Please enter your password"
            type="password"
            inputRef = {passwordRef}
            />

            { showMessage &&
                (<div>
                    <p className="text-red-500 text-center"> {errorMessage} </p>
                </div>)
            }   

            <div className="text-center p-5">
                <Button onClick = {handleSubmit} className="w-[30em] text-center">
                    Sign in
                </Button>
            </div>
            <Section
                className="pt-[5rem] -mt-[5.25rem]"
                crosses
                crossesOffset="lg:translate-y-[5.25rem]"
                customPaddings
                id="hero"
            />
            <Heading
            className="md:max-w-md lg:max-w-2xl pt-[3em]"
            title="Dont have an account? Sign-up."
            />

            <div className="text-center mb-[3em]">
                <Button className="w-[30em] text-center">
                    Sign-up
                </Button>
            </div>
            
        </div>
      </div>
      <ButtonGradient/>
    </Section>
    );
}

//<BackgroundCircles />

export default Login;