from huggingface_hub import InferenceClient

CLEAN_UP_RESPONSE = "Can you remove any CSS, JS, or HTML from this text below. Give me no other extra words in your response: \n "

FIND_EMAIL = "Can you find any contact emails in this text below? If you can, only return the email found. If not, return 'No email found'\n"
    
TEST_TEXT =  """
Skip directly to site content
	Skip directly to search




	
	
		
			
			An official website of the United States government
		
		
			
				Here's how you know
				
			
		
	
	
		
			
				
				
					Official websites use .gov
					A .gov website belongs to an official government organization in the United States.
				
			
			
				
				
					Secure .gov websites use HTTPS
					A lock ( ) or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.
				
			
		
	




	

	
		
			
	

		
		
			
				
					COVID-19				
			
			
				
								
					
						Explore Topics					
				
								
	Search
	
		
		Clear Input
		Search
	

			
		
	



	
			
							
										
											
							For Everyone
															
													
									
						
				
											
							
								About COVID-19							
						
											
							
								Symptoms							
						
											
							
								People with Certain Medical Conditions and COVID-19							
						
											
							
								COVID-19 Vaccines							
						
											
							
								Testing							
						
											
							
								Treatment							
						
											
							
								How to Protect Yourself and Others							
						
											
							
								Tools and Resources							
						
																
							
								View all							
						
										
			
		
				
							
										
											
							Health Care Providers
															
													
									
						
				
											
							
								Long COVID							
						
											
							
								Clinical Care							
						
											
							
								Infection Control Guidance							
						
											
							
								Clinical Care Quick Reference							
						
											
							
								Overview of Testing for SARS-CoV-2							
						
																
							
								View all							
						
										
			
		
				
							
										
											
							Public Health
															
													
									
						
				
											
							
								Surveillance and Data Analytics							
						
											
							
								Safety Precautions: Cleaning and Disinfecting for COVID-19							
						
											
							
								Interim Guidelines for Biosafety and COVID-19							
						
											
							
								CDC Science behind Long COVID							
						
											
							
								Health Equity in COVID-19							
						
											
							
								Variants and Genomic Surveillance for SARS-CoV-2							
						
																
							
								View all							
						
										
			
		
			
	
		
			
						
							
									
						View All					
								
						
	




	
		
	

		
			
    search
    close search
   
			
    
	
		
		Clear Input
		search
	

   
		
	

	
					
				COVID-19			
			
		
   Menu 
   Close 
  

		
			
				
	
		
		Clear Input
		search
	

			
			
								
												
								
									
										
											For Everyone										
									
								
								
									
										
																							
													
														About COVID-19													
												
																							
													
														Symptoms													
												
																							
													
														People with Certain Medical Conditions and COVID-19													
												
																							
													
														COVID-19 Vaccines													
												
																							
													
														Testing													
												
																							
													
														Treatment													
												
																							
													
														How to Protect Yourself and Others													
												
																							
													
														Tools and Resources													
												
																						
																								
													
														View All													
												
																																				
													
														Home													
												
																							
										
									
								
							
													
								
									
										
											Health Care Providers										
									
								
								
									
										
																							
													
														Long COVID													
												
																							
													
														Clinical Care													
												
																							
													
														Infection Control Guidance													
												
																							
													
														Clinical Care Quick Reference													
												
																							
													
														Overview of Testing for SARS-CoV-2													
												
																						
																								
													
														View All													
												
																																				
													
														Home													
												
																							
										
									
								
							
													
								
									
										
											Public Health										
									
								
								
									
										
																							
													
														Surveillance and Data Analytics													
												
																							
													
														Safety Precautions: Cleaning and Disinfecting for COVID-19													
												
																							
													
														Interim Guidelines for Biosafety and COVID-19													
												
																							
													
														CDC Science behind Long COVID													
												
																							
													
														Health Equity in COVID-19													
												
																							
													
														Variants and Genomic Surveillance for SARS-CoV-2													
												
																						
																								
													
														View All													
												
																																				
													
														Home													
												
																							
										
									
								
							
																									
							
			
									
						
							View All						
						COVID-19
					
							
		
	

	 


	
	
	
					
				About COVID-19			
						
				Symptoms			
						
				People with Certain Medical Conditions and COVID-19			
						
				COVID-19 Vaccines			
						
				Testing			
						
				Treatment			
						
				How to Protect Yourself and Others			
						
				Tools and Resources			
									
					View All				
			



	

			
			June 25, 2024		
		

			
					
		
	Symptoms of COVID-19	
	
		
	
		
			
		Key points
		
		
		
People with COVID-19 have a wide range of symptoms ranging from mild symptoms to severe illness.


Symptoms may appear 2-14 days after exposure to the virus.


Symptoms may start as mild, and some people will progress to more severe symptoms.



		
			
							
			
							
		
	
			
			
		
		

	

	
		
		
	Signs and Symptoms
The following list does not include all possible symptoms. Symptoms may change with new COVID-19 variants and can vary depending on vaccination status. Possible symptoms include:

Fever or chills


Cough


Shortness of breath or difficulty breathing


Sore throat


Congestion or runny nose


New loss of taste or smell


Fatigue


Muscle or body aches


Headache


Nausea or vomiting


Diarrhea



CDC will continue to update this list as we learn more about COVID-19. 
Feeling Sick?
Stay home and away from others (including people you live with who are not sick) if you have symptoms that aren't better explained by another cause.
Seek health care promptly for testing and/or treatment if you have risk factors for severe illness; treatment may help lower your risk of severe illness.



	When to seek emergency help
Look for emergency warning signs* for COVID 19:

Trouble breathing


Persistent pain or pressure in the chest


New confusion


Inability to wake or stay awake


Depending on skin tone, lips, nail beds and skin may appear pale, gray, or blue.



If someone is showing any of these signs, call 911 or call ahead to your local emergency facility. Notify the operator that you are seeking care for someone who has or may have COVID-19.
*This list does not include all possible symptoms. Please call your medical provider for any other symptoms that are severe or concerning to you.



	Difference between flu and COVID-19
Influenza (Flu) and COVID-19 are both contagious respiratory illnesses, but they are caused by different viruses. COVID-19 is caused by infection with a coronavirus named SARS-CoV-2, and flu is caused by infection with one of the influenza viruses. You cannot tell the difference between flu and COVID-19 by symptoms alone because some of the symptoms are the same. 
Some nucleic acid amplification tests (NAATs), including PCR tests, can differentiate between flu and COVID-19 at the same time. If one of these tests is not available, many testing locations provide flu and COVID-19 tests separately. 
Keep Reading:
Similarities and Differences between Flu and COVID-19


	Resources
Videos
Symptoms of Coronavirus Disease 2019 (youtube.com)


	
		
			
		
	
		On This Page	
	
		
							Signs and Symptoms
								When to seek emergency help
								Difference between flu and COVID-19
								Resources
						
	

	
		
		
	
		
	
		
		

			
			June 25, 2024		
	



	
		Sources
		Print
		Share
		
			



		
	

	
		
			
				Facebook
				
			
			
				LinkedIn
				
			
			
				Twitter
				
			
			
				Syndicate
				
			
		
	
	

		
			Content Source:
			National Center for Immunization and Respiratory Diseases (NCIRD)
		

		SourcesNational Center for Immunization and Respiratory Diseases (NCIRD)	



	

	
	


	
		
			
				
											
										
						COVID-19						
					
				
			
											COVID-19 (coronavirus disease 2019) is a disease caused by a virus named SARS-CoV-2. It can be very contagious and spreads quickly.
					
						
				View All			
					
		
			
				
											
													
																
									For Everyone
									
								
															
																
													
								
									About COVID-19								
							
													
								
									Symptoms								
							
													
								
									People with Certain Medical Conditions and COVID-19								
							
													
								
									COVID-19 Vaccines								
							
													
								
									Testing								
							
													
								
									Treatment								
							
													
								
									How to Protect Yourself and Others								
							
													
								
									Tools and Resources								
							
																			
								
									View all									
								
							
											
				
													
													
								
																		
										Health Care Providers
										
									
																	
								
																													
											
												Long COVID											
										
																													
											
												Clinical Care											
										
																													
											
												Infection Control Guidance											
										
																																						
											
												View All												
											
										
																	
							
													
								
																		
										Public Health
										
									
																	
								
																													
											
												Surveillance and Data Analytics											
										
																													
											
												Safety Precautions: Cleaning and Disinfecting for COVID-19											
										
																													
											
												Interim Guidelines for Biosafety and COVID-19											
										
																																						
											
												View All												
											
										
																	
							
											
							
			
				
					
					Sign up for Email Updates
					
				
			
		
	




	

	
		
			
				
					Contact Us 
				
				
					
						Contact Us 
						
							Call 800-232-4636
							Contact CDC
						
					
				

				
					About CDC 
				
				
					
						About CDC 
						
							Mission & Organization
							Budget & Funding
							Careers & Jobs
						
					
				

				
					Policies 
				
				
					
						
							
								
									Accessibility
									External Links
									Privacy
									Web Policies
								
							
							
								
									FOIA
									OIG
									No Fear Act
									Nondiscrimination
									Vulnerability Disclosure Policy
								
							
						
					
				

				
					Languages 
				
				
					
						
							
								Languages
								
									Español
									Multilingual Content
								
							
							
								Language Assistance
								
									
										
											Español
											繁體中文
											Tiếng Việt
											한국어
										
									
									
										
											Tagalog
											Русский
											العربية
											Kreyòl Ayisyen
										
									
									
										
											Français
											Polski
											Português
											Italiano
										
									
									
										
											Deutsch
											日本語
											فارسی
											English
										
									
								
							
						
					
				

				
					Archive 
				
				
					
						
							CDC Archive
						
					
				
			
		
	




	
		
			
				
					Contact Us 
				
				
					Contact Us 
					
						Call 800-232-4636
						Contact CDC
					
				

				
					About CDC 
				
				
					
						Mission & Organization
						Budget & Funding
						Careers & Jobs
						About CDC
					
				

				
					Policies 
				
				
					
						Accessibility
						External Links
						Privacy
						Web Policies
					
					
						FOIA
						OIG
						No Fear Act
						Nondiscrimination
						Vulnerability Disclosure Policy
					
				

				
					Languages 
				
				
					Languages 
					
						Español
						Multilingual Content
					
					Language Assistance 
					
						Español
						繁體中文
						Tiếng Việt
						한국어
						Tagalog
						Русский
						العربية
						Kreyòl Ayisyen
						Français
						Polski
						Português
						Italiano
						Deutsch
						日本語
						فارسی
						English
					
				

				
					Archive 
				
				
					
						CDC Archive
					
				
			
		
	


	
		
			
				
			
		
		
			
				
					
				
				
					
				
				
					
				
				
					
				
			
			
				
					
				
				
					
				
				
					
				
				
					
				
			
		
	


	
		
			HHS.gov
			USA.gov
		
	





	




	



var CDC_POST={"id":"1788_50","type":"cdc_dfe","context":"1788-2","lang":"en","audience":"gen","tax":{"cdc_topics":["d130dbda-56f6-48d1-9736-11adecf7b6f5"],"cdc_categories":["f99c55f7-123e-4fd7-a629-95c9340c264d"],"cdc_audiences":["8de1299b-beee-47ff-a33e-3ab1d2f97e0c"]}};


"""

ABOUT_MYSELF = """ My name is Prithvi Seran, and I am a first-year computer science student at the University of Toronto. 
				   Engineering is a discipline I always wanted to learn alongside my fascination with computer science, so I am looking to explore the overlap of machine learning and mechatronics."""

PURPOSE = "I am seeking research positions for Summer 2025 in the field of computer science, machine learning and computer engineering."

RESEARCH_INFO_TEST = """Alán Aspuru-Guzik is a professor of Chemistry and Computer Science at the University of Toronto and is also the Canada 150 Research Chair in Theoretical Chemistry and a Canada CIFAR AI Chair at the Vector Institute. He is a CIFAR Lebovic Fellow co-directing the Accelerated Decarbonization program. Alán also holds a Google Industrial Research Chair in Quantum Computing. Alán is the director of the Acceleration Consortium, a University of Toronto-based strategic initiative that aims to gather researchers from industry, government, and academia around pre-competitive research topics related to the lab of the future.

Alán began his independent career at Harvard University in 2006 and was a Full Professor at Harvard University from 2013-2018. He received his B.Sc. from the National Autonomous University of Mexico (UNAM) in 1999 and his PhD from the University of California, Berkeley in 2004, where he was also a postdoctoral fellow from 2005-2006.

Alán conducts research in the interfaces of quantum information, machine learning and chemistry. He was a pioneer in the development of algorithms and experimental implementations of quantum computers and quantum simulators dedicated to chemical systems. He has studied the role of quantum coherence in the transfer of excitonic energy in photosynthetic complexes and has accelerated the discovery by calculating organic semiconductors, organic photovoltaic energy, organic batteries and organic light-emitting diodes. He has worked on molecular representations and generative models for the automatic learning of molecular properties. Currently, Alán is interested in automation and "autonomous" chemical laboratories for accelerating scientific discovery.Among other recognitions, he received the Google Focused Award for Quantum Computing, the Sloan Research Fellowship, The Camille and Henry Dreyfus Teacher-Scholar award, and was selected as one of the best innovators under the age of 35 by the MIT Technology Review. He is an elected fellow of the American Physical Society, an elected fellow of the American Association for the Advancement of Science (AAAS), and received the Early Career Award in Theoretical Chemistry from the American Chemical Society. Alán appeared as one of the top 100 most powerful Canadians in 2024 by the Maclean’s Magazine under the AI Category.

Alán is editor-in-chief of the journal Digital Discovery, as well as co-founder of Zapata AI, Kebotix, Intrepid Labs, and Axiomatic AI.

‍

To request a Resume or Curriculum Vitae of Alán please contact aspuru.assistant@utoronto.ca.


Alán's Twitter, Substack and Mastodon profile."""

def llama_wrapper(prompt, scraped_text):
    response = ""

    client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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",
    )

    for message in client.chat_completion(
        messages=[{"role": "user", "content": prompt + scraped_text}],
        max_tokens=500,
        stream=True,
    ):
        response = response + message.choices[0].delta.content


    return response


def generate_email_using_llama(about_myself, purpose, website_content):
	response = ""
      
	client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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",
	)
        

	for message in client.chat_completion( 
		messages=[{"role": "user", "content": """Heres information about me: \n""" + about_myself + 
												"""\n  Based on this information, generate me an email for this purpose: \n""" + purpose +
												"""\n  The email should be catered towards this information: \n""" + website_content }], 
		max_tokens=500, stream=True,
		):
	
		response = response + message.choices[0].delta.content

	return response
		


if __name__ == "__main__":
    
	client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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",
	)
        

	for message in client.chat_completion( 
            messages=[{"role": "user", "content": """Heres information about me: \n""" + ABOUT_MYSELF + 
                       							  """\n  Based on this information, generate me an email for this purpose: \n""" + PURPOSE +
                                                  """\n  The email should be catered towards this information: \n""" + RESEARCH_INFO_TEST }], 
            max_tokens=500, stream=True,):
    	
		print(message.choices[0].delta.content)