## Key Features
 * Described the key features in the application that the user can access
 * Provide a breakdown or detail for each feature that is most appropriate for your application
 * This section will be used to assess the value of the features built

## Instructions
 * Clear instructions for how to use the application from the end-user's perspective
 * How do you access it? Are accounts pre-created or does a user register? Where do you start? etc. 
 * Provide clear steps for using each feature described above
 * This section is critical to testing your application and must be done carefully and thoughtfully
 
 ## Development requirements
 * If a developer were to set this up on their machine or a remote server, what are the technical requirements (e.g. OS, libraries, etc.)?
 * Briefly describe instructions for setting up and running the application (think a true README).
 
 ## Deployment and Github Workflow

Describe your Git / GitHub workflow. Essentially, we want to understand how your team members shares a codebase, avoid conflicts and deploys the application.

 * Be concise, yet precise. For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Describe your overall deployment process from writing code to viewing a live applicatioon
 * What deployment tool(s) are you using and how
 * Don't forget to **briefly explain why** you chose this workflow or particular aspects of it!

 ## Licenses 

 Keep this section as brief as possible. You may read this [Github article](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository) for a start.

 * What type of license will you apply to your codebase?
 * What affect does it have on the development and use of your codebase?
 * Why did you or your partner make this choice?



# Disability Justice Network of Ontario by Team DJNO

## Description
* **In a high level description**, Helpouts is a web and mobile application with PWS technology that allows disabled people get the help of other people in Ontario in real time. Our application is available both on web and mobile browser. **Helpouts uses a request-offer model**, where people make request for help and people offer to help by setting their preferences. The web application has a matching algorithm that picks the most suitable people to help the disabled person. Each matching finds the information of a person who can offer help, along with identifying details such as email and ways of contact. infomation is displayed on the page when a user on the mobile application or the web application sends a request for help. The mobile part is used to enable more portable usage of our app. 

* **The problem we are now trying to solve** with this is making sure disabled people in Ontario have the best people to offer help. Each person has a list of preferred way of communications in some situations and a location data. The more the way of communications is convenient for the people making a request, the more probable they're gonna match. Sometimes, the other person has already been possessed (this is a feature we'll work on in the later deliverables) by someone else, then we'll try to make sure that they won't match. We want to make sure that every disabled peron has a handful of helps, if needed, they can directly start a chat with people he/she is matched with. (this is a feature we're working in later deliverables)
* **The context required to understand why the application solves this problem** is knowing how disability facilities works, how the volunteer system works and how possible the current system may not have enough volunteers to help. Additional help from internet is needed for disabled people.

## Key Features
* The key feature of our application that the user can access is the matching algorithm that can match people who're free and able to help. Our algorithm uses the model of maximum same communications. It's based on the user settings, when the user set properties that're most suitable for the current requester's requirement after being assessed by the matching algorithm, he/she'll be pushed to that requester's recommendation list.

* (To be done in deliverable3). Our app also has a chat system, using this system, people can chat freely after they find their matching helper. This functionality will make 
people feel more connected and increase the chance of a successful request and offer procedure.
## Basic instructions
### Web application
2. Click on a marker on the map to see the details of a homeless person in need.
3. A detailed box will appear on the top left hand corner containing the person's details. 
   * You can close the box by clicking the close button in the bottom right corner of the details box.
   * You can mark the point as "Pending" to make it yellow. This action is persistent.
   * You can mark the point as "Complete" to remove it from the map. This action is persistent.
4. You can zoom in and out by clicking the `+` and `-` button at the top left corner of the map respectively. You can also zoom in and out by scrolling up and down on your mouse/trackpad respectively.

### Mobile application
1. In a new tab, or window go to our mobile app presently running on an android emulator at Appetize.io: https://appetize.io/app/5gatcnptebzga4fh6up350jaq4?device=nexus5&scale=75&orientation=portrait&osVersion=8.1
2. Press "Tap to Play".
3. Once the app loads, you can **either** press the red button "Use Current Location". (Note: this may use the location of the Appetize server where the emulator is running, **not your actual location**) **OR** press Drop a Pin button if you don't want to share your location.
   * Current Location: If prompted for location access, press "Allow".
   * Drop the Pin: navigate to where you see the homeless person and then tap to drop a pin. (tap the pin to remove the pin if accidental tap occurs). Once satisfied, press Proceed.
5. Fill in all the fields on the form with the appropriate information.
5. When all the information is recorded, click the "Submit" button. A popup should say that you are being redirected to the main page. When you dismiss the message, you should be redirected to the greeting page.
6. You should now be able to see your report in the tab or window where you have the web app running without even needing to refresh.

> You can verify that this is indeed the correct location by opening google maps in the emulator and see your current location. It will match what we have on our website map.