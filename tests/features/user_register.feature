Feature: As an admin I want to create users

	Scenario: Check if the user can see Register link
		Given I am logged in as "udac.dev@gmail.com"
		Then I should see the url to "register" from url "/"
		
	Scenario: Check if user can navigate to registeration page
		Given I am logged in as "udac.dev@gmail.com"
		When I click on registration link
		Then I should see the registration page