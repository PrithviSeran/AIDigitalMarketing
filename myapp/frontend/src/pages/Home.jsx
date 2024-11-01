import React from 'react'
import axios from 'axios';
import Hero from '../components/Hero';
import Header from '../components/Header';
import Benefits from '../components/Benefits'
import Button from '../components/Button';
import ButtonGradient from '../assets/svg/ButtonGradient.jsx'

const Home = () => {
  return (
    <div>
      <Header/>
      <Hero/>
      <Benefits/>

      <ButtonGradient/>
    </div>
  )
}


export default Home
