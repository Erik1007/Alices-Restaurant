
# Alice's Restaurant
********************


## You can get anything you want, at Alice's Restuarant
********************


********************
## Table of contents
1. [Introduction](#Introduction)
2. [Program Features](#Program-Features)
3. [Future Implementations](#Future-Implementations)
4. [Testing and Validation](#Testing-and-Validation)
5. [Unfixed Bugs](#Unfixed-Bugs)
6. [Deployment](#Deployment)
7. [Credits](#Credits)
********************



## Introduction
********************


This website introduces the user/world to a fictional restuarant (inspired by a 60's counterculter anthem) that is set in the luxurious inner downtown harbour archipelego in Stockholm Sweden. Using real landmarks for inspiration with a twist of fiction, this website aims to provide the user with something fun and functional.

This project represents an imaginary restuarant (semi-set in Stockholm Sweden) that is designed to be interactive and informative. The goal of the project is to combine django foundations and bootsrap elements that facilitate a working database on the back end of the project that a user can interact with using every element of the C.R.U.D. model. A custom reservation app is the heart of the user interaction with the database along with a secondary app for users to signup and leave comments about the site.



## Program Features
********************

This app is set up to mimic a real world website for a restuarant, therefor it has a number of essentail features for any real world business. From the fully functional navigation bar to the informative footer, the central features of the website are the reservaation system and the review section which are both interactive and function with the users input. The reservation system is an open system that anyone can interact with the website to make a reservation; however, to be able to leave a review or comment, one has to signup to be a member of the restuarant. As this website is designed with bootstrap it is a moblie first design and there for is fully responsive, thereby meeting the needs to be informative and look good on multiple screen sizes.

The main page is designed to entice the user to click further and explore the website.
This main page uses a looping background video that shows many highlights of the restuarant, from the food, to people enjoying themselves at the establishment. ![Main Page Screenshot](/media/main%20page%20screenshot%201.jpg)

On the main page, just below the main background video, there is a link that whisks the user to the booking system,for those that instantly want to come join us for a good time, so that they can start interacting with the website and entering information.

On the top of the main page there is a navigation bar that allows the user to easily move from page to page of the restuarant to fully explore and become inticed by the restaurant. This navigation bar is preseant on every page, along with the footer for easy navigation through the webite. Links to the signup page, the food and drink menu's, the page telling a bit of a fictional backstory and of course to the reservation system are all preseant. ![navbar screenshot](/media/nav%20bar%20screenshot.jpg)

At the bottom of the main page the footer can be found. In the footer section alot of vital business inforation can be found. On the left hand side there is a column providing the important business information for the address location, phone number and the website, along with a link to google maps that provides an interactive geo-location for the restuarant.
In the middle section of the footer, the user can find interactive shortcut links that help to navigate around the webiste. On the right hand side of the footer, the last of the vital information is found concerning the open hours and social links to the major social networks. ![footer screenshot](/media/footer%20screenshot.jpg)

From the navigation bar, the signup page is fairly straightforward, proding interactive prompts for the user to create a log in username and password to be a memeber of the restuarant.![sign-up screenshot](/media/signup%20screenshot.jpg) The seond link from the navigation bar is for member to log in so that they can leave a review or comment on the review page.![sign-in screenshot](/media/signin%20screenshot.jpg) The next link in the navigation bar brings the user to the food menu so that the user can see descriptions of the mouth watering food selection.![alt text](image_url) After the food menu, the following link provides the option for the user to the next main reason to visit the restuarant, its incredible and vast selction of drinks, which are fully described in the drink menu.![alt text](image_url) From there the navigation bar provides the user to see other customers thoughts/opinions of the resturant and dining expericnce on the review page.![review page](/media/reviews%20screenshot.jpg) And finally the navigation bar provides the customer the link to the reservation system so that they can make their booking.![alt text](image_url)

Both the Sign up and Log in pages have color coded alert messages to inform the user of success or failures in their attempt to sign up, log in and log out (green for success, red for unsuccessful). ![successful alert](/media/success%20alert%20screenshot.jpg)

The reservation page opens with a welcoming message inspiring the user to start the reservation process. By entering thier name, number of guests and to select a date for a visit, the user is then prompted to select their desired meal time based on table availability. [screenshot]
Once the user has selected their date and time, they are prompted to confirm the reservation via a popup modal that provides the opportunity to either delete the booking or to move forward and confirm their reservation time. [screenshot].

On the back end side of this project there is a fully functioning Admin page that supports the admin with a number of options to help the fictional restuarant run and to be successful. ![Admin screenshot](/media/admin%20screenshot.jpgT). On the righthand side of the Admin page, there is a selection of options for the admin to navigate through including the options to see comments and posts, users, emails, reservations, tables and more. Each page in the admin has a display list of methods to search the barious topics for ease of use and navigation.The Admin page for reservations provides controls for the reservations ![Reservations Admin](/media/table%20admin%20screenshot.jpg) and for tables and seating capacity assigned to each table ![Tables Admin](/media/Table%20Admin%202.jpg).






## Future Implementaions
********************

In the future, there are a few additonal interactive steps that I would like to add that would increase the satisfaction feelings of using this site:

The first and formost addional step that I would like to make would be to make both the restuarant and the bar menus fully interactive when each item was hovered over a widget image would pop up on the side of the page displaying the item in all its glory in an attempt to inspire the users appetite desires. In a perfect world, each menu item(both food and drinks) would link to an image of that item with a backdrop of the restuarant of harbour view. 

Secondly, I would like to include more background images and videos for every template page that would increa the viewing pleasure for the user and hopefully increase the visitor traffic to the imaginary restuarant.

On the Admin side, one of the main feature that I would like to include in the next round of improvements would be to code the automatic deletion of reservations that have surpased the reservation date. As of now, deleting reservations falls to Admin manual deletion.




## Testing and Validation
********************

This project was designed and releid upon the Red/Green/Refactor testing method for the development of many of the functions that are the hghlights of the site. This method is derived in methodically using basic additions to code that build to a working function or app. 

The project also uses Pep8 for code validation to ensure that all code is error free/bug free and user friendly [screenshot]


## Unfixed Bugs
********************

This project has seen a number of bugs and issues, but as of right now, there are no unfixed bugs that I am aware of (that doesnt mean that there arent any, it just means that I am unaware of them).
In the creation of the blog app that is the means for users to signup/log-in and leave reviews about the resturant; there were significant issues maintinaing the url connections to the project. Those url issues gave way to bugs connecting the project to the database.

One of the main issues came from the migration of the database from Heroku to Elephantsql, which at one point resulted in the need to recover the database. 
Most recently a bug in Gitpod erased the environmental skeleton of the project including the env.py file, the djago downoad and all of the connecting url paths in the settings. 

As far as bugs in the actual project, there were significant issues building the tables/seats in the shell connecting to the database for the function to prevent a double booking on a specific date and time. There were also bugs surrounding the javascript code for the pop up modal in the interactive delete/confirm pop up modal in the reservation system.

However, as each new issue presented itself, a solution was found to allieviate the problem.


## Deployment
********************


There are multiple provides supporting the deployment of this project. The code was written and stored in the[Alices Restuarant GitHub repository](https://github.com/Erik1007/Alices-Restaurant). This was migrated to [Heroku Alices Restuarant](https://dashboard.heroku.com/apps/alices-restaurant-eh) to deploy the inbedded Django and python code. [ElephantSQL](https://api.elephantsql.com) was linked into to house the databases used for this project. And lastly, [Cloudinary](https://console.cloudinary.com) was linked in and used as the media storage.


## Credits
********************

Many different sources have been used as insipration and for multiple levels of assistance in the creation of this project. The sources used in the development process of this poject will be presented in two main groups code and media:

## Code:
********************

- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) was  used for assistance in the development and execution of the interactive and style process for this project.

- [Django Documentation](https://www.djangoproject.com/) became both the holy grail and nightly bed time reading for references, code help and inspiration for numerous aspects of this project.

- The Code Institute 'I think therefor I blog' walk through project was used for the Django development and database development in this project. Much of the code used in teh reviews section was taken directly from the 'think before I blog' tutorial so that patrons of the resturant could leave reviews and like for their experiences and others comments.

- The Code Institute 'Resume' walk through project was used for assistance in bootstrap and styling code for this project.

- [Oxen Restaurant](https://oaxen.com/en/home/) was used for design inspiration, project layout and some code was used for inspiration for the html and style pages in this project.

- [Glasshouse Restaurant](https://www.glashuset.com/) was used for design inspiration, project layout, and html and style code was used for inspiration and guidance for the development and execution of this project. Food menu content was used for inspiration and assistance.

- [All in One Bar](https://www.allbarone.co.uk/drink#) was used for drink content and design inspiration

- For assistance with developing the reservation form, the [YouTube tutorial](https://www.youtube.com/watch?v=TuXFAl8aMvc) and [YouTube tutorial](https://www.youtube.com/watch?v=xcsbQHdtI2k) were used for code assistance and app setup.

- For addiditional code assistance, [the restuarant booking system](https://github.com/andreagrandi/booking-example/tree/master/booking/restaurants) found in githu was used for a guide and reference as to different ways to set up the reservation system.

- [Open AI Chatbot](https://chat.openai.com/) was used for tutorial help, code help, trouble shooting, assistance, support and code development through the building process of this project. The AI bot was crucial getting help with: JS onclick linsteners, reservation modal, confirmation views, creating modals, connecting urls, running tests, manipulating the DOM, inserting JS, using bootstrap features, inserting bootstrap code, using JS code, and much more.

- [Github Date-Picker](https://github.com/monim67/django-bootstrap-datepicker-plus) was used for as a reference for the date/time picker used in the reservation app, template and view.

- [Stackoverflow jquery](https://stackoverflow.com/questions/68482695/how-to-use-jquery-on-django-media-form) was used for help setting the widgets in to the reservation system.

- [Stackoverflow date-time](https://stackoverflow.com/questions/8474670/pythonic-way-to-combine-datetime-date-and-datetime-time-objects) was used for help with setting up the date and time widget on the reservation system. 

- [Stackoverflow date-range-overlap](https://stackoverflow.com/questions/9044084/efficient-date-range-overlap-calculation) was used for code help and as a reference for creating code that prevents an overlapping booking at the same time and date.

- [Stackoverflow time-period-overlap](https://stackoverflow.com/questions/69015339/how-to-check-two-time-period-for-overlap-in-django) was used for code help and as a reference for creating code that prevents an overlapping booking at the same time and date.

- [StackoverFlow JS manipulating the DOM/SCript conversion](https://stackoverflow.com/questions/3103962/converting-html-string-into-dom-elements) This page was used extensivly for help writing the JavaScript code used in the reservation system modal linking the 'submit' button with the first confirmation pop up modal.

- [StackoverFlow Preventing Sumission to the database](https://stackoverflow.com/questions/8664486/javascript-code-to-stop-form-submission) This page was used extensivly for help writing the JavaScript code used in the reservation system modal preventing the 'submit' button fron linking with the first confirmation pop up modal.

- [StackoverFlow creating choicefeilds in forms](https://stackoverflow.com/questions/22255759/django-forms-dynamic-choices-for-choicefield) This page was used as guidance and code for creating an available times choicefield in the reservation forms.

- [StackoverFlow many to many models validaiton](https://stackoverflow.com/questions/7986510/django-manytomany-model-validation/7986937#7986937) This page was used for guidance in developing a method for preventing overlaping bookings

- [StackoverFlow many to many models validaiton](https://stackoverflow.com/questions/7986510/django-manytomany-model-validation)This page was used for guidance in developing a method for preventing overlaping bookings.

- [StackoverFlow many to many filters](https://stackoverflow.com/questions/2218327/django-manytomany-filter) This page was used for guidance in developing a method for preventing overlaping bookings.

- [StackoverFlow zime zone settings](https://stackoverflow.com/questions/15980302/django-set-datetime-in-views-to-utc1) This page was used for guidance on reseting the curent time for the current location time zone


## Media:
********************

- [Background image/video loop](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.millerandcarter.co.uk%2Frestaurants%2Fscotland-and-northern-ireland%2Fmillerandcarteredinburghcitycentre&psig=AOvVaw0BcdhbWh6sSdGkmrm9zBoj&ust=1669377418830000&source=images&cd=vfe&ved=0CA8QjhxqFwoTCPjNg9LhxvsCFQAAAAAdAAAAABAE) was used for a background video loop.

- [Backround image of a bartender](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.sfgate.com%2Fwine%2Fspirits%2Farticle%2FFive-drinks-that-bartenders-just-hate-to-make-2500138.php&psig=AOvVaw15YutI6WYRkbXBZzARNYCh&ust=1669299861155000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCMip5O_hxvsCFQAAAAAdAAAAABAD)  used in this project

- [Image of people at a bar](https://www.google.com/url?sa=i&url=https%3A%2F%2Fthenounproject.com%2Fphoto%2Fgroup-of-young-people-having-drinks-at-bar-41d2N5%2F&psig=AOvVaw0LUIQY1-saAq8t39rksS0g&ust=1669299224807000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCKCvrJXixvsCFQAAAAAdAAAAABAb) that was used for this project

- [Harbor image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flickr.com%2Fphotos%2Fventeco%2F671328968&psig=AOvVaw0iiN8iburCgWVi5TFiDYJw&ust=1670863908840000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCPi_t7mT8vsCFQAAAAAdAAAAABAE) that was used for this project.

- [A second harbor image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dstrandvagen&psig=AOvVaw0iiN8iburCgWVi5TFiDYJw&ust=1670863908840000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCODx6feT8vsCFQAAAAAdAAAAABAD) that was used for  background in this project.



# Data schema

## entities
- User
- Tables
- Reservation
- slots

## Relationship
- user makes a reservation
- reservation are for an available slot
- slots are free tables that can be reserved for a given datetime

## schema

### User    Reservation   Slot     Table
pk          pk            pk       pk 
username    user          table    slug/name
            slot          date     capacity
                          Time     location


MOdel driven develope