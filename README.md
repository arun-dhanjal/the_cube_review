# The Cube Review

The Cube Review is a mini social platform built for twisty puzzle enthusiasts. It provides numerous ways for this community of hobbyists to interact, including a post feed to share thoughts, a reviews section to rate puzzles, and a leaderboards section to compete against peers.

**!!! STILL NEED TO UPDATE AMIRESPONSIVE !!!**

![The Cube Review shown on a range of devices](/readme-docs/devices-showcase.png)

[View The Cube Review on Heroku](https://the-cube-review-b38a16dd5f1d.herokuapp.com/)

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
  * [Manual Functionality Testing](#Manual-Functionality-Testing)
  * [Device Responsivity Testing](#Device-Responsivity-Testing)

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

![The Cube Review Colour Palette](/readme-docs/the-cube-review-palette.png)

A palette of mainly differing shades of red was chosen for the theme of this application. The intention was to keep things looking relatively minimalistic with splashes of a key colour throughout. The majority of buttons use these shades of red with white text. Edit and delete icons are grey whilst inactive, turning red on hover, fitting the minimalistic style. Navigation icons are bold in black, but also turn red on hover or when active.

One key exception to the overarching colour scheme applies to content that is pending approval. Posts, comments, and reviews that are yet to be approved will be highlighted in a pale, muted yellow with 'Pending approval' text written in a shade of blue. This combination has been chosen to make it clear when content is pending approval whilst remaining easy on the eye, and most importantly retaining stark contrast for accessibility.

The colour palette was created using the [Coolors](https://coolors.co/) website.

### Typography

< Description of the chosen fonts and reasons for these choices. >

### Page Layout

Wireframes were created based on the initial page layout designs for various screen sizes. The final deployed application has some minor stylistic changes/additions, but for the most part follows the same general design. Wireframes shown below:

#### Wireframe Mobile
![Wireframe 1](/readme-docs/wireframe-mobile.png)
#### Wireframe Tablet
![Wireframe 2](/readme-docs/wireframe-tablet.png)
#### Wireframe Desktop
![Wireframe 3](/readme-docs/wireframe-desktop.png)

### Database Structure

The back-end databases were designed at the start of the project with the intention of remaining unchanged througout the development in order to avoid later complications. The Entity Relationship Diagram (ERD) can be viewed below:

![< ERD 1 >](/readme-docs/erd.png)

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

Python (Django) - For backend logic, models, views, and routing.

HTML & CSS - For structure and styling.

Django Template Language (DTL) - For dynamic rendering and template logic.

### Frameworks, Libraries & Programs Used

Git - For version control.

GitHub - To save and store the files for the app, as well as for project management.

Django version 4.2 - Used as the full stack framework to connect the front and back end using MVT (model-view-template) methodology.

PostgreSQL - The chosen RDBMS for this project.

Bootstrap version 5.3 - To utilise a number of Bootstrap components, including cards, buttons, and classes for styling. Additional CSS styling was also implemented in style.css.

Django crispy forms - Used for responsive form rendering with Bootstrap 5.

Browser Dev Tools - To troubleshoot and test features, solve issues with responsiveness, and styling.

Microsoft PowerPoint - To manually create the initial wireframes, site logo, site title, and ERD diagram.

Microsoft Excel - To create the database structure ERD tables, and to track and manage code checking and testing exercises.

Microsoft Copilot - For code queries, troubleshooting Django views and templates, refining logic, and converting Excel tables into Markdown format.

OpenAI ChatGPT - For code queries and resolution of coding issues.

[Heroku](https://www.heroku.com/) - To host the web application via Eco Dynos. This has been chosen as it allows for full-stack web applications to be hosted, as apposed to GitHub which only allows for front-end applications.

[Cloudinary](https://cloudinary.com/) - To host user-uploaded images via a cloud-based server; this is necessary given Heroku's ephemeral file system on Eco Dynos.

[Am I Responsive?](http://ami.responsivedesign.is/) - To show the app image on a range of devices.

- - -

## Deployment

Heroku was used to deploy the live application. The instructions to achieve this are below:

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

### Manual Functionality Testing

Manual testing was carried out to ensure functionality of all processes was as expected. The results of these tests are below:

| **Site Area**         | **User Action**                                                                                      | **Expected Result**                                                                                                                       | **Pass/Fail** |
|-----------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Header                | Click site logo/title                                                                                | Redirect to Feed page                                                                                                                     | Pass         |
| Header                | Click Sign Up button                                                                                 | Redirect to Sign Up page                                                                                                                  | Pass         |
| Sign Up page          | Fill out Sign Up form correctly and click Submit                                                     | Redirect to Feed page as new logged-in user, displaying feedback message at top of page                                                  | Pass         |
| Sign Up page          | Fill out Sign Up form incorrectly and click Submit                                                   | Validation error displays with instructions to amend                                                                                      | Pass         |
| Header                | Click Log In button                                                                                  | Redirect to Log In page                                                                                                                   | Pass         |
| Log In page           | Fill out Log In form correctly and click Submit                                                      | Redirect to Feed page as logged-in user, displaying feedback message at top of page                                                      | Pass         |
| Log In page           | Fill out Log In form incorrectly and click Submit                                                    | Validation error displays with instructions to amend                                                                                      | Pass         |
| Header                | Click Log Out button                                                                                 | Redirect to Log Out page                                                                                                                  | Pass         |
| Log Out page          | Click Log Out button                                                                                 | Redirect to Feed page as logged-out user, displaying feedback message at top of page                                                     | Pass         |
| Nav icons             | Click Home icon                                                                                      | Redirect to Feed page                                                                                                                     | Pass         |
| Nav icons             | Click Reviews icon                                                                                   | Redirect to Puzzle List page                                                                                                              | Pass         |
| Nav icons             | Click Leaderboards icon                                                                              | Redirect to Leaderboards page                                                                                                             | Pass         |
| Feed page             | Click Sign Up button                                                                                 | Redirect to Sign Up page                                                                                                                  | Pass         |
| Feed page             | Click New Post button                                                                                | Redirect to Create a Post page                                                                                                            | Pass         |
| Create a Post page    | Fill out Create a Post form and click Submit                                                         | Redirect to Feed page with new unapproved post at top of feed, displaying feedback message at top of page                                | Pass         |
| Feed page             | Click Edit button on user-owned post                                                                 | Redirect to Edit Post page                                                                                                                | Pass         |
| Edit Post page        | Update Post form and click Save                                                                      | Redirect to Post Detail page for that post displaying updated and now unapproved post, also displaying feedback message at top of page   | Pass         |
| Feed page             | Click Delete button on user-owned post                                                               | Display Delete Post modal                                                                                                                 | Pass         |
| Delete Post modal     | Click X button                                                                                       | Closes modal                                                                                                                              | Pass         |
| Delete Post modal     | Click Cancel button                                                                                  | Closes modal                                                                                                                              | Pass         |
| Delete Post modal     | Click Delete button                                                                                  | Deletes post and redirects to Feed page, displaying feedback message at top of page                                                      | Pass         |
| Feed page             | Click View Post button on a post                                                                     | Redirect to Post Detail page of that post                                                                                                 | Pass         |
| Feed page             | Click Previous pagination button                                                                     | Go to previous page of feed                                                                                                               | Pass         |
| Feed page             | Click Next pagination button                                                                         | Go to next page of feed                                                                                                                   | Pass         |
| Post Detail page      | Click Edit button on user-owned post                                                                 | Redirect to Edit Post page                                                                                                                | Pass         |
| Edit Post page        | Update Post form and click Save                                                                      | Redirect to Post Detail page for that post displaying updated and now unapproved post, also displaying feedback message at top of page   | Pass         |
| Post Detail page      | Click Delete button on user-owned post                                                               | Display Delete Post modal                                                                                                                 | Pass         |
| Delete Post modal     | Click X button                                                                                       | Closes modal                                                                                                                              | Pass         |
| Delete Post modal     | Click Cancel button                                                                                  | Closes modal                                                                                                                              | Pass         |
| Delete Post modal     | Click Delete button                                                                                  | Deletes post and redirects to Feed page, displaying feedback message at top of page                                                      | Pass         |
| Post Detail page      | Fill out Comment form and click Submit                                                               | New unapproved comment shows in comment list, and feedback message displays at top of page                                               | Pass         |
| Post Detail page      | Click Edit button on user-owned comment                                                              | Redirect to Edit Comment page                                                                                                             | Pass         |
| Edit Comment page     | Update Comment form and click Save                                                                   | Redirect to Post Detail page of related post, displaying updated and now unapproved comment, also displaying feedback message at top of page     | Pass         |
| Post Detail page      | Click Delete button on user-owned comment                                                            | Display Delete Comment modal                                                                                                              | Pass         |
| Delete Comment modal  | Click X button                                                                                       | Closes modal                                                                                                                              | Pass         |
| Delete Comment modal  | Click Cancel button                                                                                  | Closes modal                                                                                                                              | Pass         |
| Delete Comment modal  | Click Delete button                                                                                  | Deletes comment and redirects to related post's Post Detail page, displaying feedback message at top of page                             | Pass         |
| Puzzle List page      | Click See Reviews button on a puzzle                                                                 | Redirects to Puzzle Detail page                                                                                                           | Pass         |
| Puzzle List page      | Click Previous pagination button                                                                     | Go to previous page of Puzzle List                                                                                                        | Pass         |
| Puzzle List page      | Click Next pagination button                                                                         | Go to next page of Puzzle List                                                                                                            | Pass         |
| Puzzle Detail page    | Fill out Review form and click Submit                                                                | New unapproved review shows in review list, displaying feedback message at top of page                                                   | Pass         |
| Puzzle Detail page    | Click Edit button on user-owned review                                                               | Redirect to Edit Review page                                                                                                              | Pass         |
| Edit Review page      | Update Review form and click Submit                                                                  | Redirect to Puzzle Detail page of related puzzle, displaying updated and now unapproved review, and displaying feedback message at top of page   | Pass         |
| Puzzle Detail page    | Click Delete button on user-owned review                                                             | Display Delete Review modal                                                                                                               | Pass         |
| Puzzle Detail page    | Click X button                                                                                       | Closes modal                                                                                                                              | Pass         |
| Puzzle Detail page    | Click Cancel button                                                                                  | Closes modal                                                                                                                              | Pass         |
| Puzzle Detail page    | Click Delete button                                                                                  | Deletes review and redirects to related puzzle's Puzzle Detail page, displaying feedback message at top of page                          | Pass         |
| Leaderboards page     | Click Sign Up button                                                                                 | Redirects to Sign Up page                                                                                                                 | Pass         |
| Leaderboards page     | Click Submit Time button                                                                             | Redirects to Submit Time page                                                                                                             | Pass         |
| Submit Time page      | Fill out Submit Time form correctly and click submit                                                 | Redirect to Leaderboards page with submitted time now showing in relevant puzzle's leaderboard                                           | Pass         |
| Submit Time page      | Fill out Submit Time form incorrectly and click submit                                               | Validation error displays with instructions to amend                                                                                      | Pass         |
| Submit Time page      | Fill out Submit Time form for puzzle that already has your time                                      | Error message displays advising that only one time can be submitted per puzzle                                                           | Pass         |
| Leaderboards page     | Click Update Time button                                                                             | Redirect to Update Time page                                                                                                              | Pass         |
| Update Time page      | Fill out Update Time form correctly and click submit                                                 | Redirect to Leaderboards page with updated time now showing in relevant puzzle's leaderboard                                             | Pass         |
| Update Time page      | Fill out Update Time form incorrectly and click submit                                               | Validation error displays with instructions to amend                                                                                      | Pass         |

### Device Responsivity Testing

Responsivity tests were carried out to ensure that the application displayed correctly on a number of different device sizes. For completeness, all of the default device sizes in Google Chrome's Developer Tools were tested for responsiveness by emulating each device and then navigating through the web application to note any layout or formatting issues. Almost all devices returned zero issues with two exceptions, detailed below:

- Microsoft Lumia 550: Dev Tools defaults to a landscape view for this device, which makes the viewport height very short, leading to a sub-optimal user experience. However, the application is not intended to be used in landscape mode on mobile devices, and in fact the default landscape view for this device in Dev Tools is a known error, with the expecting view being portrait as is the case with most mobile devices. As such, this case is of no concern for this application.

- JioPhone 2: The viewport for this device is very small at just 240 x 320 px (it is defined as as "compact device") which causes issues with layout. However, this application is not intended to be used on such small devices, and so is of no concern for this application.

## Validation

Various validation software were used to validate and/or lint the code in each of the files written for this project, with any raised errors being fixed before closing off the project. The screenshots below show evidence of this:

### [W3C Validator: HTML](https://validator.w3.org/)

Feed page
![HTML validation Feed page screenshot](/readme-docs/html-validation-feed-page.png)

Sign Up page
![HTML validation Sign Up page screenshot](/readme-docs/html-validation-sign-up-page.png)

Log In page
![HTML validation Log In page screenshot](/readme-docs/html-validation-log-in-page.png)

Log Out page
![HTML validation Log Out page screenshot](/readme-docs/html-validation-log-out-page.png)

Create Post page
![HTML validation Create Post page screenshot](/readme-docs/html-validation-create-post-page.png)

Edit Post page
![HTML validation Edit Post page screenshot](/readme-docs/html-validation-edit-post-page.png)

Post Detail page
![HTML validation Post Detail page screenshot](/readme-docs/html-validation-post-detail-page.png)

Edit Comment page
![HTML validation Edit Comment page screenshot](/readme-docs/html-validation-edit-comment-page.png)

Puzzle List page
![HTML validation Puzzle List page screenshot](/readme-docs/html-validation-puzzle-list-page.png)

Puzzle Detail page
![HTML validation Puzzle Detail page screenshot](/readme-docs/html-validation-puzzle-detail-page.png)

Edit Review page
![HTML validation Edit Review page screenshot](/readme-docs/html-validation-edit-review-page.png)

Leaderboards page
![HTML validation Leaderboards page screenshot](/readme-docs/html-validation-leaderboards-page.png)

Submit Time page
![HTML validation Submit Time page screenshot](/readme-docs/html-validation-submit-time-page.png)

Update Time page
![HTML validation Update Time page screenshot](/readme-docs/html-validation-update-time-page.png)

### [W3C Validator: CSS](https://jigsaw.w3.org/css-validator/)

![CSS validation screenshot](/readme-docs/css-validation.png)

### [CI Python Linter: Python](https://pep8ci.herokuapp.com/)

config/asgi.py
![Python linter config/asgi.py screenshot](/readme-docs/python-linter-config-asgi.png)

config/settings.py
![Python linter config/settings.py screenshot](/readme-docs/python-linter-config-settings.png)

config/urls.py
![Python linter config/urls.py screenshot](/readme-docs/python-linter-config-urls.png)

config/wsgi.py
![Python linter config/wsgi.py screenshot](/readme-docs/python-linter-config-wsgi.png)

feed/admin.py
![Python linter feed/admin.py screenshot](/readme-docs/python-linter-feed-admin.png)

feed/apps.py
![Python linter feed/apps.py screenshot](/readme-docs/python-linter-feed-apps.png)

feed/forms.py
![Python linter feed/forms.py screenshot](/readme-docs/python-linter-feed-forms.png)

feed/models.py
![Python linter feed/models.py screenshot](/readme-docs/python-linter-feed-models.png)

feed/urls.py
![Python linter feed/urls.py screenshot](/readme-docs/python-linter-feed-urls.png)

feed/views.py
![Python linter feed/views.py screenshot](/readme-docs/python-linter-feed-views.png)

leaderboards/admin.py
![Python linter leaderboards/admin.py screenshot](/readme-docs/python-linter-leaderboards-admin.png)

leaderboards/apps.py
![Python linter leaderboards/apps.py screenshot](/readme-docs/python-linter-leaderboards-apps.png)

leaderboards/forms.py
![Python linter leaderboards/forms.py screenshot](/readme-docs/python-linter-leaderboards-forms.png)

leaderboards/models.py
![Python linter leaderboards/models.py screenshot](/readme-docs/python-linter-leaderboards-models.png)

leaderboards/urls.py
![Python linter leaderboards/urls.py screenshot](/readme-docs/python-linter-leaderboards-urls.png)

leaderboards/views.py
![Python linter leaderboards/views.py screenshot](/readme-docs/python-linter-leaderboards-views.png)

reviews/admin.py
![Python linter reviews/admin.py screenshot](/readme-docs/python-linter-reviews-admin.png)

reviews/apps.py
![Python linter reviews/apps.py screenshot](/readme-docs/python-linter-reviews-apps.png)

reviews/forms.py
![Python linter reviews/forms.py screenshot](/readme-docs/python-linter-reviews-forms.png)

reviews/models.py
![Python linter reviews/models.py screenshot](/readme-docs/python-linter-reviews-models.png)

reviews/urls.py
![Python linter reviews/urls.py screenshot](/readme-docs/python-linter-reviews-urls.png)

reviews/views.py
![Python linter reviews/views.py screenshot](/readme-docs/python-linter-reviews-views.png)

manage.py
![Python linter manage.py screenshot](/readme-docs/python-linter-manage.png)


### [WAVE: Web Accessibility Evaluation Tool](https://wave.webaim.org/)

![WAVE validation](/readme-docs/wave.png)

### Lighthouse: Mobile

![Lighthouse mobile validation screenshot](/readme-docs/lighthouse-mobile.png)

### Lighthouse: Desktop

![Lighthouse desktop validation screenshot](/readme-docs/lighthouse-desktop.png)

- - -

## AI Usage
AI has been used extensively throughout this project, with the main assistant of choice being Microsoft Copilot, however OpenAI's ChatGPT has also been used on occassion. Listed below are the ways AI has specifically been used during this project:

* Troubleshooting Django logic in Python files

* Refining template logic in HTML files

* Generating dummy usernames for site users

* Converting Excel files into markdown format (e.g. for the markdown table featured in the Testing section of this README)

* Scanning code files for formatting and PEP8 issues to expedite the code-tidying process

* General sounding board (e.g. asking if certain implementations or functionalities would be a good idea before commiting to them)

Please note: although AI has been utilised during the development of this app, any and all AI outputs have been scrutinised and considered carefully before being implemented. The developer appreciates that AI is a tool to be used and not relied on without complete understanding of the output.

## Credits
### Content

< description of where any content came from, e.g. images, written content, blog posts, etc. >

< The favicons were sourced from: https://favicon.io/ >

### Contributors

* Contributor 1 - https://github.com/< contributor 1 >
* Contributor 2 - https://github.com/< contributor 2 >
* Contributor 3 - https://github.com/< contributor 3 >