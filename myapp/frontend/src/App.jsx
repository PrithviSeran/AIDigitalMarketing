import React from 'react';
import axios from 'axios';
import Hero from './components/Hero';
import Header from './components/Header';
import Benefits from './components/Benefits';
import Home from './pages/Home'
import Login from './pages/Login'
import Signup from './pages/Signup'
import Mainpage from './pages/Mainpage'
import Campaign from './pages/Campaign'
import Business from './pages/Business';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


const App = () => {
  return (

      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/signup" element={<Signup/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/main" element={<Mainpage/>} />
        <Route path="/campaign" element={<Campaign/>} />
        <Route path="/business" element={<Business/>} />
      </Routes>
  );
};

export default App;
