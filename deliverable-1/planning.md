# Disability Justice Network of Ontario
> _Note:_ This document is meant to evolve throughout the planning phase of your project.   That is, it makes sense for you commit regularly to this file while working on the project (especially edits/additions/deletions to the Highlights section). Most importantly, it is a reflection of all the planning you work you've done in the first iteration. 
 > **This document will serve as a master plan between your team, your partner and your TA.**

## Product Details
 
#### Q1: What are you planning to build?

##### A web app designed to facilitate connection and communication for people with disabilities.

Social isolation and loneliness is a very concerning issue in today’s society. People who are struggling with mental health also struggle socially. By using the app, users can chat and meet each other with common interests based on chosen preferences and requests. In a nutshell, the app matches users according to their abilities and needs.

>UI Demo: [https://balsamiq.cloud/spmkv6e/pcbkd0i/r2278?f=N4IgUiBcCMA0IDkpxAYWfAMhkAhHAsjgFo4DSUA2gLoC%2BQA%3D](https://balsamiq.cloud/spmkv6e/pcbkd0i/r2278?f=N4IgUiBcCMA0IDkpxAYWfAMhkAhHAsjgFo4DSUA2gLoC%2BQA%3D)
>
>Users will be first greeted with a login screen if the app is opened for the first time or the current session is expired. Then there is a nav bar with Home, Match, Friend tabs. Home is the default screen with a list of related postings of requests and offers in their area according to the matching algorithm. They can respond to any posting by clicking on it, which will notify the original poster. Then there's a Match screen, which will show a list of matched users with the highest matching score based on their preferences. And the *Friends *screen, where users can see their chat history and friends list. Preferences (e.g. neighbourhood connect GPS feature, time, location, etc.) can be changed in the User Profile screen, which can be accessed at the top left corner at any time.

#### Q2: Who are your target users?

Our target users are people who self-identify as a person with a disability, both physical or mental health issues who commonly suffer from a lack of social support.  

*   Joe is a war veteran who lives in Thunder Bay and suffers from PTSD and panic attacks from the mental trauma that he experienced during his service in Iraq. Joe is aware of the fact that having a conversation with others can reduce the likelihood of panic attacks. Joe would like to reach out to people who understand his condition and are willing to have a conversation with him.

*   Ryan is a 15-year-old deaf student from Mississauga who suffers from depression because of bullying. He loves to play brain teasers and board games, but due to his physical constraint, it's difficult for him to make friends. Ryan would like to befriend people who might have had similar experiences and have been through what Ryan has been through. Ryan hopes to learn from them on how to overcome his difficulties.

*   Angel is a retired physician living in Toronto, she is paraplegic in a wheelchair that needs the assistance of a specially trained dog to move around. She is an avid traveller. She enjoys sharing stories about her adventures in the various countries she has been to. However, she feels that she has a hard time socializing due to her mobility and it is very rare for her to have visitors who she socializes with.

*   Victoria is an international student from China studying at the University of Toronto. She suffers from stuttering and as a result, has low self-confidence. She needs a friend to take her shopping because of her inability to communicate with the salesperson.

#### Q3: Why would your users choose your product? What are they using today to solve their problem/need?

Our product’s focus is geared towards people with disabilities, and it would be made simple and easy to use. It will provide a wide range of features that meet the needs of customers, including making specific requests and offers, the ability to connect with users physically within a certain distance, and virtually over the internet. 

Currently, our potential users could connect using features over social media such as Facebook and Snapchat. But these platforms often include unrelated features and ads and do not provide specific tools we hope to provide our user. Our product will allow users to define “what they want and what they can provide” preferences, share their location, and use our algorithm to find a good match. This way our users are able to connect much more accurately and effectively when compared to other tools.

Overall our product will introduce efficiency, accuracy, and be simple to use. We hope this product would be valuable to our project partner’s goal of helping people with disabilities thrive and foster meaningful community and relationships.

#### Q4: How will you build it?

*   Frontend
    *   React as UI framework: 
        *   React is powerful at building rich user interactions. Since our app intends to connect people, there might be a log of user-interactions and a need for responsive UI. Working with React will help us quickly implement all the functionality with state implementation. (Also considering Redux as a state container s.t the functional frontend codes can be more expressive)
    *   Polymer as a template: 
        *   *Polymer* is an efficient HTML template library with elegant APIs. It quickly updates the DOM elements in the front-end and structures the UI with models making the whole front-end development more extensible.
    *   Webpack as JS module bundler: 
        *   *Webpack* is a powerful dependency management tool for frontend development since our project requires a lot of external API calls and third-party libraries, it’s important to have *Webpack* to help us.
    *   Websocket as socket programming helper
        *   WebSocket is currently the standard communication protocol for our applications involving TCP. Since chatroom functionality is heavily TCP based, we use WebSocket to handle the client-side chat implementation.
*   Backend
    *   Python3
        *   Python3 has tons of builtin functions and popular libraries like pandas and *NumPy* for scientific computations which can help us with our matching algorithm implementation. To develop a matching algorithm, we might need a lot of computation during development, so python3 is the best choice
    *   Python Flask (framework)
        *   *Flask* is a pretty pythonic framework, and it’s flexible. Since we are using *MVC* architecture for the backend, *Flask* would be a perfect fit due to its strong support for ORM and customizable components.
    *   MongoDB (NoSQL)
        *   *MongoDB* is a *NoSQL* database. *NoSQL* is easier for us to get started and most of the data in our app doesn’t require too many relations and migrations. We emphasize more on scalability. So choosing *NoSQL* is the best choice
    *   MongoEngine
        *   *MongoEngine* is an Object mapper and declarative API designed in python3. It helps python3 manipulate the *MongoDB* in an easy way.
*   Deployment
    *   We will deploy the application on Firebase or Heroku or AWS
    *   Docker, which makes it very easy to package and deliver applications.
*   Architecture: 
    *   Model–view–controller (MVC)
        *   To clearly manage our project, we need to be clear what exactly we’re developing at every phase. So dividing the architecture to model-view-controller is quite important. With MVC, we can assign tasks to our group members more easily and make sure their work won’t overlap and cause conflicts.
    *   REST 
        *   REST is now a really popular way of developing both mobile apps and web apps. Since it’s super extensible, clearly separating the backend and frontend/app and some of us are not good at frontend and GUI, we can make them focus on the aspects they’re good at with REST.
*   External API: 
    *   Google/phone number authentication
        *   To make sure everyone has only one account and be responsible for their activities, as well as avoiding bots.
    *   Google Map API
        *   provides accurate location information of devices, which is used in the matching algorithm
*   Testing Strategy: 
    *   Unit Tests (Unit testing)
        *   Unittest is included in the standard library in python3, this library provides most of the unit test functions we need: mock, assertion and integration testing.
    *   Manual Tests
        *   Manual tests ensure the application is defect & error-free. Automaton is for implementation and manual tests are the part that determines the quality of our app. We will depend heavily on manual tests to adjust our plans and the expectation for our app.

We will build our app first on the web and then transfer to mobiles (Android/IOS) with specific tools. At the front-end, we have two types of tech stacks in use. One is for UI development and the other is for codebase management. *React* is chosen as the GUI development tool thanks to its responsive and stateful design, which improves the UX. For codebase and dependency management, tools such as *Webpack* are chosen to handle automation of tasks such as linting and testing the app. At the backend, *NoSQL* database is chosen for its advantage on agile development, and MVC to structure our work. Applying *Flask *and *MongoEngine* is a smart choice. Also, we may later apply pandas and *NumPy* to help with the matching algorithm.


#### Q5: What are the user stories that make up the MVP?

1. As a new user, I want to create an account with my name, email and password so that I can connect with other users.
    *   The user should be able to create a new login
    
2. As a new user, I want to set my preferences so that I can connect with people who have things in common with me.
    *   The user should be able to modify their preferences
3. As an existing user, I want to login with my username and password so that I can connect with people securely.
    *   The user should be able to securely login to their profile
4. As an existing user, I would like to be able to modify my profile, so that other users can stay up to date to my life.
    *   The user should be able to modify their profile settings
5. As an existing user, I would like to view others' profiles, so that I can determine if I would like to connect with them.
    *   The user should be able to view others’ profile information
6. As an existing user, I want to be able to turn on location sharing and set a location radius in order to be connected with someone in the area. 
    *   The user should be able to be matched with someone closeby
7. As an existing user, I want to be able to choose my preferences in order to be matched with a user like me.
    *   Acceptance Criteria:
        1. Location sorting in match algorithm
        2. Friend request to people the user likes
        3. Matching score system
8. As an existing user, I want to be able to connect with someone nearby without disclosing my location so that I can make a meaningful relationship.
    *   The user should be able to be matched with a user in their area with location sharing turned off
9. As a user, I want to be able to maintain a needs/wants and do/offer list so that I can be assisted.
    *   The user should be able to make a new request or a new offer and see it in the list of active requests/offers in the home screen
10. As an existing user, I want to be able to chat with a matched user within the application, so that I can have a conversation before meeting in person.
    *   The user should be able to start a chat once they have been matched with another user
11. As an existing user, I want to look at my chat history with every connection I’ve made so that I can check how I have been socializing.
    *   The user should be able to view their list of chats along with recent messages of each chat
12. As an existing user, I want to set a radius from my location and see the available requests in the area, so that I can decide manually which request will be suitable for me.
    *   The user should be able to filter requests based on a specified radius
13. As an admin, I want to register other admin users, so they can perform administrative actions.
    *   The app should allow admin users to register, and receive admin privileges.
14. As an admin, I want to be able to flag high-risk requests in order to redirect users to appropriate support.
    *   An admin should be able to modify/remove messages.
    *   Ad admin should be able to create warning flags.
15. As an admin, I want to be able to modify matching criteria  as needed in order to run the application with best practices
    *   An admin should be able to modify inputs of the matching criteria, i.e. input variables and multipliers.

## Process Details

#### Q6: What are the roles & responsibilities on the team?

William: Chief Project manager
*   Facilitate communication with members of the project partner, schedule and guide weekly meetings. 
*   Lead development in database design and data privacy, support in the user profile.

Truman: Lead Front End Developer
*   Having experience with building PWAs, he will provide total technical support for his team.
*   Lead the front-end with a progressive codebase that is efficient and able to work offline.
*   Responsible for overall UX, UI design, and page load performance.

Henry: 	Backend developer
*   Focus on API implementation, associate with the chat features and user profile development.

David: Full-stack developer
*   Help out in the frontend and backend, particularly UI, matching algorithm, user profile, and firebase.

Asad: Data specialist, algorithm developer
*   Work with William on data encryption,
*   Work on the matching algorithm with David and Junxuan.

Junxuan: Lead backend developer, Chat system designer, algorithm developer
*   Work on the chat system and matching algorithm

---
Front-end
*   API calls: Henry
*   Design: Truman, William, David
*   UI: Truman
*   User Profile: David 


Backend (Python):
*   Chat: Junxuan, Henry
*   Privacy(data encryption): William, Asad
*   Matching (algorithm & implementation): Junxuan, David, Asad
*   User Profile: David, William, Henry
*   Other Enhancements: TBA

Deployment: Truman 

Database: William, David, Junxuan

MongoDB Backend (database, backend code running): David, Truman

QA: David, William, Asad, Henry

Communication with Project Partner: Truman, William

<table>
  <tr>
   <td>
   </td>
   <td>Strengths
   </td>
   <td>Weaknesses
   </td>
  </tr>
  <tr>
   <td>Truman
   </td>
   <td>PWA frameworks, services, UI design
   </td>
   <td>N/A
   </td>
  </tr>
  <tr>
   <td>Weiyi (Henry)
   </td>
   <td>API design, REST, QA
   </td>
   <td>language, algorithm, UI
   </td>
  </tr>
  <tr>
   <td>David
   </td>
   <td>Python, SQL, UI
   </td>
   <td>Firebase, backend, matching algorithm
   </td>
  </tr>
  <tr>
   <td>Willian
   </td>
   <td>Java, Python, algorithm, Software Development cycle
   </td>
   <td>UI, HTML, CSS, Javascript
   </td>
  </tr>
  <tr>
   <td>Asad
   </td>
   <td>Python, SQL, Java
   </td>
   <td>UI, HTML
   </td>
  </tr>
  <tr>
   <td>Junxuan
   </td>
   <td>Java, Python, TCP/UDP protocols
   </td>
   <td>UI, mobile, pixel adaptation, deployment
   </td>
  </tr>
</table>

#### Q7: What operational events will you have as a team?

Weekly full team standups: 



*   Time: Friday afternoon at 4 pm (4:10 U of T time), or Saturday at noon
*   Location: BA, SS, or study room in Kelly Library
*   Purpose: Updates on individual progress, discuss any problems encountered, decide on a solution/resolution, and assign priorities. We believe meeting at least once every week as a team will help with developing responsibilities and have everyone held accountable for their tasks.

Code Nights:



*   Friday evening(after the meeting) or Saturday Afternoons
*   Locations:  BA, SS, or study room in Kelly Library
*   Purpose: create a hackathon-like environment where our team can code together, ask questions, decide on details, review code.

Sectional meetings: 



*   These are short meetups that could be anytime during the week between members working on a part of the project (ex. Server database, GUI, etc). 
*   Location: could be online or in-person, decide among the participating members
*   Purpose: discuss any issues that need to be resolved with the section.

Meeting with the Constanza (Project Partner):



*   Fridays afternoon 4:30 pm 
*   Location: BA, SS, or study room in Kelly Library or through Zoom
*   Purpose: update partner with our progress, discuss any design/implementation details.

#### Q8: What artifacts will you use to self-organize?

Individual tasks are assigned in this document, each section has a lead, and will distribute workload to other members with instructions.

**Slack** for communication, we have a set meeting schedule. Any amendment or cancellation will be done so via slack. 

**Asana** for helping teams manage projects and tasks in one tool. Teams can create projects, assign work to teammates, specify deadlines, and communicate about tasks directly in Asana. 

#### Q9: What are the rules regarding how your team works?

Agile software development and flat structure: agile, flexible, easy-going, engaging and impact learning, positive environment. However, members are to be held accountable for their individual part and must <span style="text-decoration:underline;">take ownership </span>of their work. We expect to <span style="text-decoration:underline;">complete the task on time </span>and allocate sufficient time for testing, discussion and wrap up.


#### Communications

Slack:



*   Channel for communication with our TA Neeraja: used for asking questions to the TA.
*   General Discussion (team members): Any high-level topics with regards to the project, meeting times, etc. 
*   Dev (team members): Any topics and issues related to the coding details. We expect all members to regularly look up information and discussion of the project, hold self and each other accountable.
*   Members are expected to check slack at least once every 24 hours and respond to any messages related to the individual. 



#### Communication With Partner



*   Weekly progress report via Zoom, any topic discussions. 
*   Separate Slack channel for communication with the partner, primarily communication between PM and team lead to Constanza (project partner).


#### Meetings



*   There will be one in-person meeting almost every Friday. Everyone is expected to be present and on time (4:10 pm, UofT time).
*   Team members will go in a circle starting with the PM to update individual progress, discuss and issues that need to be resolved. Our team lead and PM will conclude with remarks of each section and assign any task. Lastly, any member can ask questions and discuss topics.
*   If any disagreement comes across after thorough discussion, our team will perform an anonymous democratic vote, and go with the majority (there are no ties since we have 7 people.


#### Problem/Conflict & Resolution

As our project partner mentioned, she will provide general support 



*   **Problem**: 	Team conflict in general.
    *   **Resolution**: 	We will talk with the members involved. Everyone is expected to present their opinions on that issue in chat groups or a short meeting up.

*   **Problem**: 	A teammate who rarely responds or has a slow response time.
    *   **Resolution**: 	We will identify the cause of it, and figure out a more feasible way.

*   **Problem**: 	The project progress tool shows that a teammate was underperforming.
    *   **Resolution**: 	We will also identify the cause of it, create a more frequent checkup to ensure everyone's is up for the task.

*   **Problem**: 	We cannot deliver all the criteria specified in the deliverable.
    *   **Resolution**: 	We will communicate with our project partner and our TA, assign priority to core features that could be completed in a timely manner.

*   **Problem**: 	Our project partner is unfortunately not interested in the project anymore.
    *   **Resolution**: 	We will ask our TA for assistance in this case.


#### Team culture



*   We’re a group of team-first players. All the people in our team are at the center of what we do. 
*   We believe in building skills and improving during development. Our team members will help each other during the development process. We support and encourage each other to achieve success -- inside and outside school.
*   Our team is always Reinvent, we challenge each other and the norm. 


### 


----
### Highlights

1. **Why are we making Progressive Web App (PWA)?**

    To make an application that works on any devices including desktop and mobiles under a time constraint, we decided to take advantage of PWA due to its universality while the performance is not being compromised [1]. It does not matter what device is being used, a PWA can be consumed anywhere at any time, even offline [2].


     "[1] PWA vs Native App (and How to Choose Between Them)." 17 Sep. 2018, https://blog.magestore.com/pwa-vs-native-app/.
     "[2] Offline Storage for Progressive Web Apps - Google Developers." 12 Feb. 2019, https://developers.google.com/web/fundamentals/instant-and-offline/web-storage/offline-for-pwa.



2. **Why do we use python3 instead of traditional server language like Java?**

    Python3 has powerful and expressive built-in syntax and computation functions like ZIP. As a server-side language, it enables the programmer to write less code and get more done. For Java, writing a section of computation code is complicated involving Stream API and multiple third-party libraries. But with python3, a simple *NumPy *might solve all the problems. 

3. **Will we focus more on asynchronous programming or synchronous programming?**

    We’ll focus more on asynchronous programming since python3 also provides an asynchronous library (Async IO). Since our app also provides channels for chatting, this process is best to implement with an asynchronous methodology. And sometimes we need to fetch data from external databases, doing an asynchronous request is better than handling it with asynchronous thread.

4. **Why do we choose NoSQL instead of SQL?**

    Although SQL is powerful, *NoSQL* is easier to start with and provides most of the functionalities SQL has. Most of us don’t have rich experience with databases, so choosing *NoSQL* as a start will be a good choice. Also considering that we might modify some of the plans during the development for MVP, we might need the scalability *NoSQL* has.

5. **Why do we choose React?**

    React is powerful at building rich user interactions. Since our app intends to connect people, there might be a log of user-interactions and need of responsive UI. Working with React will help us quickly implement all the functionality with state implementation. (Also considering Redux as a state container s.t the functional frontend codes can be more expressive)
 useful for important information regarding your decision making process that may not necessarily fit in other sections. 
