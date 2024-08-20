# HomeDecor/API

This is my fifth milestone project with Code Institute. It involves building the backend API for the HomeDecor frontend React app. The API provides the models and logic that enable the frontend to perform CRUD operations.

HomeDecor is a content-sharing platform focused on home decor ideas. Users can sign up, share their decor inspirations, like or unlike posts, and follow or unfollow other users.

[View the Deployed Backend here.](https://fifth-project-b52d7d161462.herokuapp.com/)

[View the Deployed Fontend here.](https://moments-fat-771e386813d1.herokuapp.com/)

## Index – Table of Contents
* [Data Structure](#data-structure)
* [User Story](#user-story)
* [API Routes](#API-routes)

* [Technologies Used](#technologies-used)
  * [Languages Used:](#languages-used)
  * [Frameworks and Libraries Used:](#frameworks-and-libraries-used)
  * [Software and Web Applications Used:](#software-and-web-applications-used)
* [Testing](#testing)
  * [Browser Testing](#browser-testing)
  * [Responsiveness](#responsiveness)
  * [Validator Testing](#validator-testing)
    * [W3C Markup Validator:](#w3c-markup-validator)
    * [W3C CSS Validator:](#w3c-css-validator)
    * [JSHint:](#jshint)
    * [PEP8 Online:](#pep8-online)
    * [Lighthouse:](#lighthouse)
  * [Test Cases for Models](#test-cases-for-models)
  * [Solved bugs](#solved-bugs)
  * [Known bugs](#known-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## Data Structure
The plan for this project was loosely based on the Code Institute Moments walkthrough project.
Most of the models are similar except for the Saved model, which has been customised to better suit the needs of MewMes app users.
<img width="824" alt="Data structure" src="https://github.com/user-attachments/assets/f80b4b04-67df-4849-9868-cfc11eb556ae">

## User Story

This project was developed using agile methodologies, with user stories, upcoming features, and unresolved bugs tracked on the GitHub Project Board. The board organizes user stories for  the back-end components, categorized with distinct labels for better visibility and management.

 * [Backend User Story](https://github.com/users/fh255/projects/8/views/1)
 * [Frontend User Story](https://github.com/users/fh255/projects/10/views/1?layout=board)
  
## API Routes

 ```bash
  dj-rest-auth/login/
  dj-rest-auth/logout/
  dj-rest-auth/registration/
  dj-rest-auth/password/change/
  dj-rest-auth/token/refresh/
  profiles/
  profiles/<int:pk>/
  posts/
  posts/<int:pk>/
  comments/
  comments/<int:pk>/
  likes/
  likes/<int:pk>/
  tags/
  tags/<int:pk>/
  followers/
  followers/<int:pk>/
  following/
  following/<int:pk>/
   ```








