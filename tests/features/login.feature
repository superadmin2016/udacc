Feature: As a web admin
			I want to secure my website.

	Scenario: Successful login
	 	Given flask is setup
		When I login with "udac.dev@gmail.com" and "admin"
	 	then I should see the alert "admin"
	 	
 	Scenario: Unsuccessful login
 		Given flask is setup
 		When I login with "udac.dev@gmail.com" and "admin2"
 		then I should see the alert "Invalid username or password"

 