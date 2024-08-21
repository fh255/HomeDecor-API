# HomeDecor/API

This is my fifth milestone project with Code Institute. It involves building the backend API for the HomeDecor frontend React app. The API provides the models and logic that enable the frontend to perform CRUD operations.

HomeDecor is a content-sharing platform focused on home decor ideas. Users can sign up, share their decor inspirations, like or unlike posts, and follow or unfollow other users.

[View the Deployed Backend here.](https://fifth-project-b52d7d161462.herokuapp.com/)

[View the Deployed Fontend here.](https://moments-fat-771e386813d1.herokuapp.com/)

## Index – Table of Contents
* [Data Structure](#data-structure)
* [User Story](#user-story)
* [API Routes](#api-routes)

* [Technologies Used](#technologies-used)
  * [Languages Used:](#languages-used)
  * [Frameworks and Libraries Used:](#frameworks-and-libraries-used)
  * [Software and Web Applications Used:](#software-and-web-applications-used)
* [Testing](#testing)
  * [Unit Testing](#unit-testing)
  * [Manual Testing](#manual-testing)
  * [Test Cases](#test-cases)
  * [Testing CRUD functionality](#testing-crdu-functionality)
  * [Validator Testing](#validator-testing)
    * [PEP8 Online:](#pep8-online)
    * [Lighthouse:](#lighthouse)
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

## Technologies Used
### Languages Used:

### Frameworks and Libraries Used:

### Software and Web Applications Used:


## Testing

### Unit Testing
The following tests were created following the CI walkthrough.

#### Posts Detail View testing:
<img width="606" alt="Post detaiView1" src="https://github.com/user-attachments/assets/3170c428-4ee2-42f6-ad55-d198cf1e1780">
<img width="694" alt="PostDetailView2" src="https://github.com/user-attachments/assets/070679f3-da18-4b77-98fd-485fe5b7e532">
<img width="778" alt="PostDetailView3" src="https://github.com/user-attachments/assets/fe254341-8a20-4491-a7d5-5cdc1b304be3">

#### Posts List View testing:
<img width="820" alt="PostListView 1" src="https://github.com/user-attachments/assets/01f9297f-af5e-4b10-b14a-8729bb8e1fe2">
<img width="749" alt="PostListView 2" src="https://github.com/user-attachments/assets/7318f041-c3f0-4276-b8d5-f55b99a0a242">

### Manual Testing
The HomeDecor API was manually tested throughout development using the Django REST framework. Each feature’s API endpoints and CRUD functionality were thoroughly tested to ensure proper operation. Additionally, the endpoints were verified on the deployed site and continuously checked during front-end development to confirm seamless integration between the front and back ends as new features were implemented in the React app.

### Test Cases
Test Cases Implemented for Functionality Checks:
 * Tested login, logout, and registration functionality.
 * Verified that POST, PUT, and DELETE methods for posts, profiles, followers, tags, comments, and likes are restricted to authorized users.
 * Confirmed GET methods work correctly via API endpoints.
 * Checked the filter functionality using keywords.
 * Tested POST requests for creating posts, comments, likes, tags, and followers.
 * Tested PUT requests for updating profiles, posts, and comments by ID.
 * Tested DELETE requests for deleting posts, comments, likes, and followers by ID.

### Testing CRUD functionality
<img width="525" alt="CRDU" src="https://github.com/user-attachments/assets/43527766-c63d-475a-9274-3b4dc4160be0">

### Validator Testing

#### PEP8 Online:
The Python code was checked for errors using the Problems tab in Gitpod. Each file was reviewed and fixed for PEP8 compliance, mainly minor issues like missing blank lines.
The only remaining warnings are for long lines in settings.py under AUTH_PASSWORD_VALIDATORS. These were left unchanged to avoid potential issues, following advice from the Code Institute Slack channels.
<details>
<summary>The issues</summary>
<img width="1141" alt="Long string" src="https://github.com/user-attachments/assets/be27f5ef-82b3-4084-bfc6-939bad7f7efc">
</details>

#### Lighthouse:
I have verified that the page is easy to read and accessible by running them through Lighthouse in Chrome Developer Tools on the following pages:
<img width="673" alt="Light House" src="https://github.com/user-attachments/assets/2eb54945-db60-4acb-bb9d-93835475421c">

### Solved bugs:


### Validator Testing
#### Lighthouse
#### PEP8 Online







