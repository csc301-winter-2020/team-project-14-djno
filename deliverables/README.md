# Disability Justice Network of Ontario by Team DJNO

## Description

- **In a high level description**, _Helpouts_ is a web and mobile application that allows disabled people to get help from other people in Ontario in real time. **Helpouts uses a request-offer model**, where people make requests for help and people offer to help by setting their preferences accordingly. The web application has a matching algorithm that picks the most suitable candidate to help the disabled person. Each matching finds the information of a person who can offer help, along with identifying details such as email and ways of contact. Infomation is displayed on the page when a user on the mobile application or the web application sends a request for help. The mobile part is used to enable more portable usage of our app.

- A simpler description: We are building a web app to connect people with disabilities, both physical and mental, thereby creating a social network of disabled people. People with disabilities can find common interests and help each other out. Currently there is no other application out there that does exactly this thing for disabled people, so ours would be the first application.

- **The problem we are now trying to solve** with this is making sure disabled people in Ontario have the best people to offer help. Each person has a list of preferred way of communication in some situations and a location data. The more the way of communications is convenient for the people making a request, the more probable they're gonna be matched. Sometimes, the other person has already been possessed (this is a feature we'll work on in the later deliverables) by someone else, then we'll try to make sure that they won't match. We want to make sure that every disabled person has a handful of help, if needed, they can directly start a chat with people he/she is matched with. (this is a feature we're working in later deliverables)

- **The context required to understand why the application solves this problem** is knowing how disability facilities work, how the volunteer system works and how possible the current system may not have enough volunteers to help. Additional help from internet is needed for disabled people.

## Key Features

- The key feature of our application that the user can access is the matching algorithm that can match people who're free and able to help. Our algorithm uses the model of maximum same communications. It's based on the user settings, when the user set properties that're most suitable for the current requester's requirement after being assessed by the matching algorithm, he/she'll be pushed to that requester's recommendation list.

- Our application implements a google login, making it more convenient for users to register. This feature also guarantees safety and protection with regards to the users’ data. Besides this, users get to specify their ‘preferences’, meaning what sort of support are they willing/capable of offering to other disabled people. The users will also be able to make a request, which will contain a description of what sort of help they desire. Our application contains an algorithm which will match users based on their preferences and the demands in the requests.

- (To be done in deliverable3). Our app also has a chat system, using this system, people can chat freely after they find their matching helper. This functionality will make
  people feel more connected and increase the chance of a successful request and offer procedure.

## Basic instructions

### Web application

2. Click on a marker on the map to see the details of a homeless person in need.
3. A detailed box will appear on the top left hand corner containing the person's details.
   - You can close the box by clicking the close button in the bottom right corner of the details box.
   - You can mark the point as "Pending" to make it yellow. This action is persistent.
   - You can mark the point as "Complete" to remove it from the map. This action is persistent.
4. You can zoom in and out by clicking the `+` and `-` button at the top left corner of the map respectively. You can also zoom in and out by scrolling up and down on your mouse/trackpad respectively.

### Mobile application

1. In a new tab, or window go to our mobile app presently running on an android emulator at Appetize.io: https://appetize.io/app/5gatcnptebzga4fh6up350jaq4?device=nexus5&scale=75&orientation=portrait&osVersion=8.1
2. Press "Tap to Play".
3. Once the app loads, you can **either** press the red button "Use Current Location". (Note: this may use the location of the Appetize server where the emulator is running, **not your actual location**) **OR** press Drop a Pin button if you don't want to share your location.
   - Current Location: If prompted for location access, press "Allow".
   - Drop the Pin: navigate to where you see the homeless person and then tap to drop a pin. (tap the pin to remove the pin if accidental tap occurs). Once satisfied, press Proceed.
4. Fill in all the fields on the form with the appropriate information.
5. When all the information is recorded, click the "Submit" button. A popup should say that you are being redirected to the main page. When you dismiss the message, you should be redirected to the greeting page.
6. You should now be able to see your report in the tab or window where you have the web app running without even needing to refresh.

> You can verify that this is indeed the correct location by opening google maps in the emulator and see your current location. It will match what we have on our website map.

## Development requirements

- The developer would need to install the files in requirements.txt

## Deployment and Github Workflow

## Licenses

- We will use MIT licensing
