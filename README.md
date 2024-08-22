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
  * [Languages ](#languages-used)
  * [Frameworks and Libraries ](#frameworks-and-libraries-used)
  * [Database](#database)
  * [Cloud Storage and Deployment Services](cloud-storage-and-deployment-services)
* [Testing](#testing)
  * [Unit Testing](#unit-testing)
  * [Manual Testing](#manual-testing)
  * [Test Cases](#test-cases)
  * [Testing CRUD functionality](#testing-crdu-functionality)
  * [Validator Testing](#validator-testing)
    * [PEP8 Online](#pep8-online)
    * [Lighthouse](#lighthouse)
  * [Solved bugs](#solved-bugs)
  * [Known bugs](#known-bugs)
* [Deployment](#deployment)
* [Fork the Repository](fork-the-repository)
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
### Languages :
 * [Python](https://www.python.org/)
 * [HTML](https://www.w3schools.com/html/default.asp)
 * [CSS](https://www.w3schools.com/css/default.asp)
 * [JS](https://react.dev/)

### Frameworks and Libraries :
#### API Backend
 * [Django Rest Framework](https://www.django-rest-framework.org/)
 * [Psycopg2](https://pypi.org/project/psycopg2/)
 * [django_filters](https://django-filter.readthedocs.io/en/stable/guide/install.html)
 * [rest_framework.authtoken](https://pypi.org/project/django-rest-authtoken/)
 * [dj_rest_auth](https://pypi.org/project/django-rest-authtoken/)
 * [JSON WEB tokens](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
 * [corsheaders](https://pypi.org/project/django-cors-headers/)
 * [dj_rest_auth.registration](https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html)
 * [dbdiagram.io](https://dbdiagram.io/home)
 * [Google Sheets](https://docs.google.com/spreadsheets/)

### Database
 * [PostgreSQL](https://www.postgresql.org/)
 * [ElephantSQL](https://customer.elephantsql.com/login)

### Cloud Storage and Deployment Services
 * [Cloudinary](https://cloudinary.com/)
 * [Heroku](https://id.heroku.com/login)


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
 * The deployment failed multiple times due to a CORS (Cross-Origin Resource Sharing) error. After revisiting the Code Institute walkthrough and with help from tutor support, I successfully configured the CORS settings in the backend settings.py file.
 * Another issue occurred with loading the default profile image, caused by an outdated version of Cloudinary. I resolved this with guidance from tutor support.

### Known bugs:
As of now, there are no known bugs in the back-end based on my testing and knowledge.

## Deployment
The application was successfully deployed to Heroku with the following steps:
 - Login to Heroku dashboard to view installed apps.
 - Click on **New** => **Create new app**.
 - Choose a unique name for your application and select your region.
 - Click on Create app.
 - Once your application is created, navigate to the Settings tab => click on Reveal Config Vars.
    - Copy the DATABASE_URL value to the clipboard.
    - Copy the url for client origin and client origin dev to the clipboard.
 - In GitPod, create a new env.py file at the top level directory.
 - In the env.py file
    - Set environment variables: **os.environ["DATABASE_URL"]** = **"Paste in Heroku DATABASE_URL Link"**
    - Add in secret key: **os.environ[”SECRET_KEY"]** = **"Generate your own randomSecretKey”**
 - In Heroku, navigate to the Settings tab => click on Reveal Config Vars.
 - Add SECRET_KEY to Config Vars using the randomSecretKey you generated.
 - In the settings.py file:
    - Replace the insecure secret key with: **SECRET_KEY = os.environ.get("SECRET_KEY")**
    - Update to use the DATABASE_URL: import dj_database_url and DATABASES['default'] = dj_database_url.parse(os.environ.get("DATABASE_URL"))
    - set the CSRF_TRUSTED_ORIGINS values , CORS_ALLOW_CREDENTIALS to True and JWT_AUTH_SAMESITE to None.
    - Replace the DEBUG Setting to be only true in Dev and False in Prod Mode
- Save all files and run migrations: python3 manage.py migrate
- Log in to Cloudinary and navigate to the Cloudinary Dashboard.
- Copy your CLOUDINARY_URL API Environment Variable to the clipboard.
- In the env.py file
    - Add Cloudinary **URL: os.environ["CLOUDINARY_URL"] = "cloudinary://paste in your API Environment Variable"**
  - In Heroku, go to the Settings tab => click on Reveal Config Vars.
  - Add 'CLOUDINARY_URL' to Config Vars with the API Environment Variable value.
  - Add 'DISABLE_COLLECTSTATIC' = 1 to Heroku Config Vars (temporary, remove before final deployment).
  - In the settings.py file:
    - Add Cloudinary Libraries to installed apps (order matters): **'cloudinary_storage', 'django.contrib.staticfiles', 'cloudinary'**
    - Add the following code below STATIC_URL = ’/static/' to use Cloudinary to store media and static files:
      - STATICFILES_STORAGE = ’cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      - STATICFILES_DIRS = [os.path.join(BASE_DIR, ’static')]
      - STATIC_ROOT = os.path.join(BASE_DIR, ’staticfiles')
      - MEDIA_URL = '/media/'
      - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    - Link file to the templates directory in Heroku: **TEMPLATES_DIR = os.path.join(BASE_DIR, ’templates')**
    - Change the templates directory to: TEMPLATES_DIR: 'DIRS': [TEMPLATES_DIR],
    - Add Heroku Hostname to ALLOWED_HOSTS: ALLOWED_HOSTS = [”Your_Project_name.herokuapp.com”, ”localhost”]
  - Create a Procfile on the top level directory
  - In the Procfile file:
    - Add the following code: release: python manage.py makemigrations && python manage.py migrate
                              web: gunicorn drf_api.wsgi
  - In the terminal: Add, Commit and Push.
  - In Heroku navigate to the Deploy tab => click on Deploy Branch.
  - When build process is finished click on Open App to visit the live site.

## Fork the Repository
Log in to GitHub, go to the repository "[HomeDecor-API](https://github.com/fh255/HomeDecor-API)" click the Fork button in the top right-hand corner, and a copy of the repo will be available in your GitHub repositories list.

## Credits
  - [Code Institute:](https://codeinstitute.net/) Walkthrough modules in Full Stack Frameworks.
  - [Code Institute Slack Community:](https://app.slack.com/) Slack community for troubleshooting and FAQ.
  - [Code Institute Tutor Support:](https://app.slack.com/) For help and support.
  - [Django documentation:](https://docs.djangoproject.com/en/4.1/) Everything you need to know about Django.
  - [Stack Overflow:](https://stackoverflow.com) For troubleshooting and FAQ.
  - [W3Schools:](https://www.w3schools.com) Online Web Tutorials.

### Acknowledgements

  - Special thanks to the tutor assistance and my mentor at Code Institute, Martina Terlevic, for their invaluable support with code reviews, assistance, and feedback. It has been immensely appreciated!






