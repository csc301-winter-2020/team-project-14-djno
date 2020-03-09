# Disability Justice Network of Ontario by Team DJNO

## Description

- **In a high level description**, _Helpouts_ is a web and mobile application that allows people with disabilities to get help from other people in Ontario in real time. _Helpouts_ uses a request-offer model, where people can set their preferences and availability settings to offer help, and fill a request form to seek for help. Based on information submitted by the users, the application employs a matching algorithm that selects the most suitable candidate to assist with each request submitted. Users of this application are able to have better and simple access to the assistance they need.


- **The problem we are now trying to solve** with this application is to improve the overall social wellness of the disability community. This platform will gives people easy access to meet suitable peers by simply providing some information of their habits and preferences. In the society, there are many potential connections and friendships undiscovered, and this application could make it all possible.

- **The context required to understand why the application solves this problem** is the request-offer model, basic knowledge of disabilty, how the volunteer system works.

## Key Features

- The key feature of our application that the user can access is the matching algorithm that can match people who're free and able to help. Our algorithm uses the model of maximum same communications. It's based on the user settings, when the user set properties that're most suitable for the current requester's requirement after being assessed by the matching algorithm, he/she'll be pushed to that requester's recommendation list.

- Our application implements a google login, making it more convenient for users to register. This feature also guarantees safety and protection with regards to the users’ data. Besides this, users get to specify their _preferences_, meaning what sort of support are they willing/capable of offering to other disabled people. The users will also be able to make a request, which will contain a description of what sort of help they desire. Our application contains an algorithm which will match users based on their preferences and the demands in the requests.

- (To be done in deliverable3). Our app also has a chat system, using this system, people can chat freely after they find their matching helper. This functionality will make
  people feel more connected and increase the chance of a successful request and offer procedure.

## Basic instructions

A simple flow chart of usage: (https://drive.google.com/file/d/1hJMwSYwBMfhrg_YZIf8n2Rj9pvBhni62/view?fbclid=IwAR2_qGChIsXfY5gOgJaXTHqk29LqYY4yDIBpSYdxJZYvKpAe2e_x-GtED28)
1.	To access the application, go here (http://helpout3.eba-wjwn6cbb.us-east-2.elasticbeanstalk.com/index.html).
2.	To login click, on the google login icon and it will lead the user to a google authentication pop-up.
3.	If the authentication is successful, the user is lead to the home page, if unsuccessful he will remain at the login page. If this is a new user in the system, he will be registered in the database.
4.	From the home page, clicking the profile button leads to a page with a form, which the user can edit his personal information and save.
5.	From the home page, clicking on the Settings buttons leads to a page with another form, which users can fill out the fields with appropriate information about their location, schedule and preferences, and save.
6.	The user can post a request using the ‘+’ icon on the bottom right hand side, where a pop-up form is displayed. The user needs to fill out the form with appropriate information of his request and submit it, then wait for the internal algorithm to find him a match.
7. **todo**

## Development requirements

- The developer would need to install the files in requirements.txt

## Deployment and Github Workflow
We utilize branching thoroughly, especially when we are working on our individual parts. Do code reviews with another member associated with the updated when rebasing.
- The *dev-backend* branch is the root for all backend development, the *dev-frontend* is branch is the root for all frontend development. Developers would branch off to implement features, do code review with another member (usually with Truman or Junxuan, the lead of front-end and back-end development, resolve any issues, then rebase onto the *dev-backend/dev-frontend* branch once confirmed.
- The *exploration* branch contains samples and example usage for any third party api to be integrated.
- The *dev* branch is used for integrating front end and backend and modifications created during the process.
- The *master* branch hold latest working project, is updated by rebasing *dev* onto *master*. This is usually done by Junxuan and at least one other member.

Application deployment: 
- First we test the server's api calls using postman.
- 

For styling we followed PEP 8 (https://www.python.org/dev/peps/pep-0008/) and 

Development tools:
- PyCharm, MongoDB, Mongo Compass,Postman, Bootstrap Studio

## Licenses

- We will use MIT licensing

