# AI Digital Marketing Platform

## Overview

A Django-based platform that streamlines and enhances email marketing campaigns using modern automation and generative AI techniques. This project integrates web scraping, AI-generated content, and cloud infrastructure to deliver personalized outreach at scale.

## Features

- **Campaign Automation**  
  Automates the lifecycle of email campaigns from content generation to dispatch, reducing manual overhead for marketing teams.

- **Business Discovery**  
  Utilizes **Selenium** to identify relevant businesses and **Scrapy** to extract structured content from their websites.

- **AI-Powered Email Generation**  
  Integrates **Llama 3**, a state-of-the-art LLM, to craft personalized email templates based on the scraped content and business context.

- **Cloud-Based Infrastructure**  
  Employs **Google Cloud Platform (GCP)** for:
  - Secure user authentication
  - Gmail API integration for seamless email delivery

- **Robust Data Storage**  
  Implements a **PostgreSQL** database to manage user data and campaign history with an emphasis on security, scalability, and performance.

## Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **AI/LLM:** Llama 3
- **Web Automation & Scraping:** Selenium, Scrapy
- **Cloud Services:** Google Cloud Platform (Authentication, Email API)

## Goals

- Boost the effectiveness of cold outreach for small businesses and marketers.
- Demonstrate the application of LLMs in automating business processes.
- Build a scalable and secure SaaS-style architecture using modern web tools.

## Future Work

- Add campaign analytics and success tracking
- Enable A/B testing for generated email templates
- Implement user dashboards with campaign performance insights
