# < app name >

< Short description about what the app is and what it is for. >

![<application name> app shown on a range of devices](/readme-docs/devices-showcase.png)

[View < application name > on Github Pages](https://arun-dhanjal.github.io/<application-name>/)

## CONTENTS

* [Purpose and Value](#Purpose-and-Value)
  * [Application Purpose](#Application-Purpose)
  * [User Value](#User-Value)

* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Typography](#Typography)
  * [Page Layout](#Page-Layout)
  * [Database Structure](#Database-Structure)
  * [Features](#Features)
  * [Accessibility](#Accessibility)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks-Libraries--Programs-Used)

* [Deployment](#Deployment)

* [Testing](#Testing)
* [Validation](#Validation)

* [AI Usage](#AI-Usage)

* [Credits](#Credits)

- - -

## Purpose and Value

### Application Purpose
 
This application is designed to give a specific group of users (twisty puzzle enthusiasts) a platform on which they can interact as a community in a number of ways. The main use cases would be: a feed section for viewing, submitting, and commenting on posts; a reviews section to read and submit reviews on a number of puzzles; and a leaderboards section to see solve-time rankings and even add your own. The application would be used in a similar way to other social media apps, albeit on a smaller scale and in a much more specific way.

### User Value

User stories with relevant acceptance criteria have been created to demonstrate the value that users would derive from using this app. These user stories are listed below:

### #1 Paginated Post Feed

As a user, I want to see a feed of posts so I can browse recent updates from others.

**Acceptance Criteria**

- Posts are displayed in reverse chronological order.
- Only a limited number of posts are shown per page.
- Pagination controls allow navigation between pages.

### #2 Registration and Login

As a new user, I want to register and log in so I can access and contribute to the platform.

**Acceptance Criteria**

- Registration form includes username and password.
- Login form accepts valid credentials.
- Users can logout.

### #3 Create Posts

As a logged-in user, I want to create a post so I can share updates with the community.

**Acceptance Criteria**

- Post form includes body and optional image.
- Posts are saved with author and timestamp.
- Only logged-in users can create posts.

### #4 View Individual Posts

As a user, I want to view a single post in detail so I can read and comment on it.

**Acceptance Criteria**

- Clicking a post opens a detail page.
- Detail page shows full post content and comments.

### #5 Comment on Posts

As a logged-in user, I want to comment on posts so I can join the conversation.

**Acceptance Criteria**

- Comment form appears on post detail page only for logged-in users.
- Comments are saved with author and timestamp.
- Comments display under the correct post.

### #6 Users Can Manage Their Own Content

As a logged-in user, I want to edit or delete my own posts and comments so I can control my contributions.

**Acceptance Criteria**

- Edit and delete options appear only for the content owner.
- Edits update the content and timestamp.
- Deletions remove the content from the database.

### #7 Admin Approves All Submitted Content

As the admin, I want to approve all posts, comments, and reviews before they appear publicly.

**Acceptance Criteria**

- New content is marked as pending by default.
- Admin can approve content via the Django admin panel.
- Only approved content is visible to users.

### #8 Puzzle List Page

As a user, I want to browse puzzles so I can learn about different twisty puzzles and see how the community has rated them.

**Acceptance Criteria**

- Review page lists all puzzles.
- Each listing shows puzzle name, average rating, number of reviews, picture, and description.

### #9 Post Puzzle Reviews and Submit a Rating

As a logged-in user, I want to submit a review and rating for a puzzle so I can share my opinion.

**Acceptance Criteria**

- Review form includes puzzle name, rating (1–5), and review text.
- Reviews are saved with author and timestamp.
- Reviews are hidden until approved by admin.

### #10 Leaderboard Page

As a user, I want to view a leaderboard so I can compare solve times with others.

**Acceptance Criteria**

- Leaderboard shows submitted times per puzzle, with the fastest at the top.
- Displays puzzle name, rank, usernam, time, and submission date.

### #11 Submit Solve Times

**User Story**

As a logged-in user, I want to submit my solve time so I can compete on the leaderboard.

**Acceptance Criteria**

- Submission form includes puzzle name and time.
- Times are saved with user, time, and timestamp.

- - -

In addition, a dedicated GitHub project board has been created and used to drive development and manage project tasks. This project board is linked below:

[GitHub Project Board](https://github.com/users/arun-dhanjal/projects/7)

- - -

## Design

### Colour Scheme

![< app name > Colour Palette](/readme-docs/appname-palette.png)

< Description of colour palette and reasons for choices. > The colour palette was created using the [Coolors](https://coolors.co/) website.

### Typography

< Description of the chosen fonts and reasons for these choices. >

### Page Layout

Wireframes were created based on the initial page layout designs for various screen sizes. < The final deployed application has some minor changes/additions, for example < describe the changes >. > Wireframes shown below:

#### Wireframe 1
![Wireframe 1](/readme-docs/wireframe-1.png)
#### Wireframe 2
![Wireframe 2](/readme-docs/wireframe-2.png)
#### Wireframe 3
![Wireframe 3](/readme-docs/wireframe-3.png)

### Database Structure

The back-end database was designed at the start of the project with the intention of remaining unchanged througout the development in order to avoid later complications. The relevant Entity Relationship Diagrams (ERDs) can be viewed below:

#### < ERD 1 >
![< ERD 1 >](/readme-docs/erd-1.png)

#### < ERD 2 >
![< ERD 2 >](/readme-docs/erd-2.png)

#### < ERD 3 >
![< ERD 3 >](/readme-docs/erd-3.png)

### Features

* < App Feature 1: >

  * < App Feature bullet point 1 >

  * < App Feature bullet point 2 >

  * < App Feature bullet point 3 >

  ![< App Feature 1 >](/readme-docs/app-feature-1.png)

* < App Feature 2: >

  * < App Feature bullet point 1 >

  * < App Feature bullet point 2 >

  * < App Feature bullet point 3 >

  ![< App Feature 1 >](/readme-docs/app-feature-2.png)

* < App Feature 3: >

  * < App Feature bullet point 1 >

  * < App Feature bullet point 2 >

  * < App Feature bullet point 3 >

  ![< App Feature 1 >](/readme-docs/app-feature-3.png)

* Future implementations:

  * < Future implementation 1 >

  * < Future implementation 2 >

  * < Future implementation 3 >

### Accessibility

Mindful development has been exercised throughout the project to ensure the app is as accessible and user-friendly as possible. This includes:

* Using semantic HTML.

* Ensuring that there is a sufficient colour contrast throughout the site.

* Ensuring that navigation is intuitive and easy.

* Ensuring interactive elements and inputs are easy to recognise and use.

* Including appropriate aria labelling.

* < additional considerations >

- - -

## Technologies Used

### Languages Used

< delete as appropriate: HTML, CSS, JavaScript, and Python > were used to create this app.

### Frameworks, Libraries & Programs Used

< delete the following entries as appropriate >

Git - For version control.

GitHub - To save and store the files for the app, as well as for project management.

Django version < version number > - Used as the full stack framework to connect the front and back end using MVT (model-view-template) methodology.

PostgreSQL - The chosen RDBMS for this project.

Bootstrap version < version number > - < Code used mainly for < describe features that used BS >. Additional CSS styling was also implemented in style.css. >

Browser Dev Tools - To troubleshoot and test features, solve issues with responsiveness, and styling.

Microsoft PowerPoint - To create the initial wireframes.

Microsoft Excel - To create the databas structure ERDs.

Microsoft Copilot - For code queries and resolution of coding issues.

OpenAI ChatGPT - For code queries and resolution of coding issues.

[Heroku](https://www.heroku.com/) - To host the web application via Eco Dynos. This has been chosen as it allows for full-stack web applications to be hosted, as apposed to GitHub which only allows for front-end applications.

[Cloudinary](https://cloudinary.com/) - To host user-uploaded images via a cloud-based server; this is necessary given Heroku's ephemeral file system on Eco Dynos.

[Am I Responsive?](http://ami.responsivedesign.is/) - To show the app image on a range of devices.

< additional frameworks, libraries, or packages >

- - -

## Deployment

< If deployed via GitHub, use the following steps and delete the Heroku steps.>

GitHub Pages was used to deploy the live app. The instructions to achieve this are below:

1. Log in to GitHub.
2. Find the repository for this project: hackathon-quiz-app.
3. Click on the Settings link.
4. Click on the Pages link in the left hand side navigation bar.
5. In the Source section, choose main from the drop down select branch menu. Select Root from the drop down select folder menu.
6. Click Save. Your live GitHub Pages site is now deployed at the URL shown.

< If deployed via Heroku, use the following steps and delete the GitHub steps.>

Heroku was used to deploy the live app. The instructions to achieve this are below:

1. Log in to Heroku and navigate to your dashboard.
2. Create a new app with a unique name.
3. Go back to your workspace and install a production-ready webserver for Heroku, e.g. Gunicorn.
4. Add the webserver to your requirements.txt file.
5. Create a Procfile in your root directory and declare the Gunicorn web process.
6. Add the '.herokuapp.com' hostname to the list of ALLOWED_HOSTS.
7. Add, commit, and push your changes to GitHub.
8. Move back to Heroku and click the Deploy tab.
9. In Deployment method, choose Connect to GitHub and select your GitHub repo.
10. Scroll to the bottom of the page and click Deploy Branch to start a manual deployment.

- - -

## Testing

Testing was ongoing throughout the entire development process. Browser developer tools were used while building to pinpoint and troubleshoot any issues as development progressed, as well as Microsoft Copilot/OpenAI ChatGPT to query specific coding logic queries.

Manual testing was carried out upon completion of the initial development to ensure all acceptance criteria had been met for all user stories. The results of these tests can be viewed below:

### < Functionality 1 >

< The web application should be able to do this. >

#### Test and Result

< The following test was carried out and the result was this. >

### < Functionality 2 >

< The web application should be able to do this. >

#### Test and Result

< The following test was carried out and the result was this. >

### < Functionality 3 >

< The web application should be able to do this. >

#### Test and Result

< The following test was carried out and the result was this. >

## Validation

Various validation software were used to validate and/or lint the code in each of the files written for this project, with any raised errors being fixed before closing off the project. The screenshots below show evidence of this:

< delete the following as appropriate >

#### W3C Validator: HTML

![HTML validation screenshot](/readme-docs/html-validation.png)

#### W3C Validator: CSS

![CSS validation screenshot](/readme-docs/css-validation.png)

#### JSHint: JavaScript

![JS lint screenshot](/readme-docs/js-lint.png)

#### CI Python Linter: Python

![Python lint screenshot](/readme-docs/python-lint.png)

#### WAVE: Web Accessibility Evaluation Tool

![WAVE validation](/readme-docs/wave.png)

#### Lighthouse: Mobile

![Lighthouse mobile validation screenshot](/readme-docs/lighthouse-mobile.png)

#### Lighthouse: Desktop

![Lighthouse desktop validation screenshot](/readme-docs/lighthouse-desktop.png)

- - -

## AI Usage
< note on the way AI has been used during the project, with bullet points below: >

* < bullet point 1 >

* < bullet point 2 >

* < bullet point 3 >

Please note: although AI has been utilised during the development of this app, any and all AI outputs have been scrutinised and considered carefully before being implemented. The developer appreciates that AI is a tool to be used and not relied on without complete understanding of the output.

## Credits
### Content

< description of where any content came from, e.g. images, written content, blog posts, etc. >

< The favicons were sourced from: https://favicon.io/ >

### Contributors

* Contributor 1 - https://github.com/< contributor 1 >
* Contributor 2 - https://github.com/< contributor 2 >
* Contributor 3 - https://github.com/< contributor 3 >