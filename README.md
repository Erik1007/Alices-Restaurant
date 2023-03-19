
# Alice's Restaurant
********************


## You can get anything you want, at Alice's Restaurant
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


This website introduces the user/world to a fictional restaurant (inspired by a 60's counter-culture anthem) that is set in the luxurious inner downtown harbour archipelago in Stockholm Sweden. Using real landmarks for inspiration with a twist of fiction, this website aims to provide the user with something fun and functional.

This project represents an imaginary restaurant (semi-set in Stockholm Sweden) that is designed to be interactive and informative. The goal of the project is to combine Django foundations and Bootstrap elements that facilitate a working database on the back end of the project that a user can interact with using every element of the C.R.U.D. model. A custom reservation app is the heart of the user interaction with the database along with a secondary app for users to signup and leave comments about the site.



## Program Features
********************

This app is set up to mimic a real world website for a restaurant, therefor it has a number of essential features for any real world business. From the fully functional navigation bar to the informative footer, the central features of the website are the reservation system and the review section which are both interactive and function with the user's input. The reservation system is an open system that anyone can interact with the website to make a reservation; however, to be able to leave a review or comment, one has to signup to be a member of the restaurant. As this website is designed with bootstrap it is a mobile first design and there for is fully responsive, thereby meeting the needs to be informative and look good on multiple screen sizes.

The main page is designed to entice the user to click further and explore the website.
This main page uses a looping background video that shows many highlights of the restaurant, from the food, to people enjoying themselves at the establishment. ![Main Page Screenshot](/media/main%20page%20screenshot%201.jpg)

On the main page, just below the main background video, there is a link that whisks the user to the booking system, for those that instantly want to come join us for a good time, so that they can start interacting with the website and entering information.

On the top of the main page there is a navigation bar that allows the user to easily move from page to page of the restaurant to fully explore and become enticed by the restaurant. This navigation bar is present on every page, along with the footer for easy navigation through the website. Links to the signup page, the food and drink menu's, the page telling a bit of a fictional backstory and of course to the reservation system are all present. 

At the bottom of the main page the footer can be found. In the footer section alot of vital business information can be found. On the left hand side there is a column providing the important business information for the address location, phone number and the website, along with a link to google maps that provides an interactive geo-location for the restaurant.
In the middle section of the footer, the user can find interactive shortcut links that help to navigate around the website. On the right hand side of the footer, the last of the vital information is found concerning the open hours and social links to the major social networks. ![footer screenshot](/media/footer%20screenshot.jpg)

From the navigation bar, the signup page is fairly straightforward, prodding interactive prompts for the user to create a log in username and password to be a member of the restaurant.![sign-up screenshot](/media/signup%20screenshot.jpg) The second link from the navigation bar is for member to log in so that they can leave a review or comment on the review page.![sign-in screenshot](/media/signin%20screenshot.jpg) The next link in the navigation bar brings the user to the food menu so that the user can see descriptions of the mouth watering food selection.![alt text](image_url) After the food menu, the following link provides the option for the user to the next main reason to visit the restaurant, its incredible and vast selection of drinks, which are fully described in the drink menu.![alt text](image_url) From there the navigation bar provides the user to see other customers thoughts/opinions of the restaurant and dining experience on the review page.![review page](/media/reviews%20screenshot.jpg) And finally the navigation bar provides the customer the link to the reservation system so that they can make their booking.![alt text](image_url)


Both the Sign up and Log in pages have color coded alert messages to inform the user of success or failures in their attempt to sign up, log in and log out (green for success, red for unsuccessful). ![successful alert](/media/success%20alert%20screenshot.jpg)


The reservation page opens with a welcoming message inspiring the user to start the reservation process. By entering their name, number of guests and to select a date for a visit, the user is then prompted to select their desired meal time based on table availability. ![reservation screenshot](/media/reservation%20screenshot.jpg)


Once the user has selected their date and time, they are prompted to confirm the reservation via a popup modal that provides the opportunity to either delete the booking or to move forward and confirm their reservation time. ![confirm pop-up modal](/media/confirm%20popup%20modal.jpg).


Included in the reservation system there are controls that interact with the user. For example, if the user enters a number that is not larger than 1, they get a warning message ![number of people warning](/media/number%20of%20people.jpg).


In the case the user accidently enters a date that is in the 'past', an interactive pop-up warning explaining that they need to enter a valid date ![past date pop up](/media/past%20date.jpg)

And when the user enters a valid number of guests along with a valid date and time, they get a success message ![success message](/media/success%20message.jpg)


On the back end side of this project there is a fully functioning Admin page that supports the admin with a number of options to help the fictional restuarant run and to be successful. ![Admin screenshot](/media/admin%20screenshot.jpgT). On the righthand side of the Admin page, there is a selection of options for the admin to navigate through including the options to see comments and posts, users, emails, reservations, tables and more. Each page in the admin has a display list of methods to search the various topics for ease of use and navigation. The Admin page for reservations provides controls for the reservations ![Reservations Admin](/media/table%20admin%20screenshot.jpg) and for tables and seating capacity assigned to each table ![Tables Admin](/media/Table%20Admin%202.jpg).

This project has combined numerous aspects of the full stack process, from Agile development process to front and backend languages; it has been a full spectrum project. To compliment such an undertaking there have been numerous production thought processes and designs to make it possible. 
![front end wireframe](/media/front%20end%20wireframe.jpg)
![full project wireframe](/media/full%20project%20wireframe.jpg)
![reservation app wireframe](/media/reservation%20app%20wireframe%20-%20Copy.jpg)
![agile example](/media/agile%20porcess%20screenshot%20-%20Copy.jpg)
![Reservation flow](/media/reservation%20flow%20wire.jpg)


## Future Implementations
********************

In the future, there are a few additional interactive steps that I would like to add that would increase the satisfaction feelings of using this site:

The first and fore most additional step that I would like to make would be to make both the restaurant and the bar menus fully interactive when each item was hovered over a widget image would pop up on the side of the page displaying the item in all its glory in an attempt to inspire the user's appetite desires. In a perfect world, each menu item (both food and drinks) would link to an image of that item with a backdrop of the restaurant of harbour view. 

Secondly, I would like to include more background images and videos for every template page that would increase the viewing pleasure for the user and hopefully increase the visitor traffic to the imaginary restaurant.

On the Admin side, one of the main features that I would like to include in the next round of improvements would be to code the automatic deletion of reservations that have surpassed the reservation date. As of now, deleting reservations falls to Admin manual deletion.

Another concept that will be involved in the next round of improvments will be the re-insertion of the favicon icon that initially was installed but was removed at the last moment as it was not rendering consistenly or correctly.

In the next round of deployment, I will reintroduce the javascript that was previously working to create a message inside of the pop up modal, that for some reason decided not to work any longer, so it was removed to prevent it from causing an other issues.

Lastly, in the next round of development for this project, I intend on adding a success and failure html pages that will link off of the confirm button in the rservation modal. There were many attempts made pre-submission to make this a possibility, however, I determined that the confirm modal was enough of an user C.R.U.D. interaction and that the additional pages would be for the net round of development.


## Testing and Validation
********************

This project was designed and relied upon the Red/Green/Refactor testing method for the development of many of the functions that are the highlights of the site. This method is derived in methodically using basic additions to code that build to a working function or app. 

The red/green/refractor process was especially essential for the process of building the reservation manager which controls the incoming reservation request from the user, checks for table availability by date, time and number of persons and provides a success or failure response to the user. 
The testing process was also especially essential in the development of the JavaScript code controlling the user interaction with the confirmation button, linking the confirm modal with the success page to provide the user feedback.


Pep8 was installed in the gitpod for developmental control ensuring that during the whole process all for the code written complied with the accessibility and readability standards.

Jasmine was used for javascript testing.

W3C html validator was used for debugging errors in all of the html pages. The one flaw that this validator has is that it does not like the python extensions and throws errors for the pythonic setups. However, it was essentail in tracking down and correcting numerous html and css bugs.
![w3c html validator screenshot](/media/W3C%20html%20validator.jpg)
![w3s css validator](/media/css%20validator.jpg)



## Unfixed Bugs
********************

As far as continuing unfixed bugs, there are a couple that exist that do not impede the functionality of the project:

In the creation of the blog app that is the means for users to signup/log-in and leave reviews about the restaurant; there were significant issues maintaining the url connections to the project. Those url issues gave way to bugs connecting the project to the database.

One of the main issues came from the migration of the database from Heroku to Elephantsql, which at one point resulted in the need to recover the database. 
Most recently a bug in Gitpod erased the environmental skeleton of the project including the env.py file, the djago download and all of the connecting url paths in the settings. 

As far as bugs in the actual project, there were significant issues building the tables/seats in the shell connecting to the database for the function to prevent a double booking on a specific date and time. There were also bugs surrounding the javascript code for the pop up modal in the interactive delete/confirm pop up modal in the reservation system.

The many to many object combining the reservation with the tables to save the reservation and reserve the table (checking for availability) created many bugs and error codes that needed to be systematically tracked down and solved.

The favicon icon is set to appear in the browser tab for the project, to provide a symbol or icon for the user to identify the website easily on their browser, however, despite multiple attempts to create a path and test for the path to work, the icon itself has not rendered and instead provides an error code. Although this is not essential for the project, it is never the less on ongoing bug. At the last moment I decided to remove the favicon icon code as it was causing more issues while not displaying the icon; there for this will now be another concept for the next round in the future.

The javascript controlling the inner message for the pop up modal stopped working today, so instead of leaving non fucntioning script in the project, I removed it.


## Deployment
********************


There are multiple provides supporting the deployment of this project. The code was written and stored in the[Alices restaurant GitHub repository](https://github.com/Erik1007/Alices-Restaurant). This was migrated to [Heroku Alices restaurant](https://dashboard.heroku.com/apps/alices-restaurant-eh) to deploy the imbedded Django and python code. [ElephantSQL](https://api.elephantsql.com) was linked into to house the databases used for this project. And lastly, [Cloudinary](https://console.cloudinary.com) was linked in and used as the media storage.


## Credits
********************

Many different sources have been used as inspiration and for multiple levels of assistance in the creation of this project. The sources used in the development process of this project will be presented in two main groups code and media:

## Code:
********************

- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) was  used for assistance in the development and execution of the interactive and style process for this project.

- [Django Documentation](https://www.djangoproject.com/) became both the holy grail and nightly bed time reading for references, code help and inspiration for numerous aspects of this project.

- The Code Institute 'I think therefor I blog' walk through project was used for the Django development and database development in this project. Much of the code used in the reviews section was taken directly from the 'think before I blog' tutorial so that patrons of the restaurant could leave reviews and like for their experiences and others' comments.

- The Code Institute 'Resume' walk through project was used for assistance in bootstrap and styling code for this project.

- [Oxen Restaurant](https://oaxen.com/en/home/) was used for design inspiration, project layout and some code was used for inspiration for the html and style pages in this project.

- [Glasshouse Restaurant](https://www.glashuset.com/) was used for design inspiration, project layout, and html and style code was used for inspiration and guidance for the development and execution of this project. Food menu content was used for inspiration and assistance.

- [All in One Bar](https://www.allbarone.co.uk/drink#) was used for drink content and design inspiration

- For assistance with developing the reservation form, the [YouTube tutorial](https://www.youtube.com/watch?v=TuXFAl8aMvc) and [YouTube tutorial](https://www.youtube.com/watch?v=xcsbQHdtI2k) were used for code assistance and app setup.

- For additional code assistance, [the restaurant booking system](https://github.com/andreagrandi/booking-example/tree/master/booking/restaurants) found in github was used for a guide and reference as to different ways to set up the reservation system.

- [Open AI Chatbot](https://chat.openai.com/) was used for tutorial help, code help, trouble shooting, assistance, support and code development through the building process of this project. The AI bot was crucial getting help with: JS onclick listeners, reservation modal, confirmation views, creating modals, connecting urls, running tests, manipulating the DOM, inserting JS, using bootstrap features, inserting bootstrap code, using JS code, and much more.

- [Github Date-Picker](https://github.com/monim67/django-bootstrap-datepicker-plus) was used for as a reference for the date/time picker used in the reservation app, template and view.

- [Stackoverflow jquery](https://stackoverflow.com/questions/68482695/how-to-use-jquery-on-django-media-form) was used for help setting the widgets in to the reservation system.

- [Stackoverflow date-time](https://stackoverflow.com/questions/8474670/pythonic-way-to-combine-datetime-date-and-datetime-time-objects) was used for help with setting up the date and time widget on the reservation system. 

- [Stackoverflow date-range-overlap](https://stackoverflow.com/questions/9044084/efficient-date-range-overlap-calculation) was used for code help and as a reference for creating code that prevents an overlapping booking at the same time and date.

- [Stackoverflow time-period-overlap](https://stackoverflow.com/questions/69015339/how-to-check-two-time-period-for-overlap-in-django) was used for code help and as a reference for creating code that prevents an overlapping booking at the same time and date.

- [StackoverFlow JS manipulating the DOM/SCript conversion](https://stackoverflow.com/questions/3103962/converting-html-string-into-dom-elements) This page was used extensively for help writing the JavaScript code used in the reservation system modal linking the 'submit' button with the first confirmation pop up modal.

- [StackoverFlow Preventing Submission to the database](https://stackoverflow.com/questions/8664486/javascript-code-to-stop-form-submission) This page was used extensively for help writing the JavaScript code used in the reservation system modal preventing the 'submit' button fron linking with the first confirmation pop up modal.

- [StackoverFlow creating choicefeilds in forms](https://stackoverflow.com/questions/22255759/django-forms-dynamic-choices-for-choicefield) This page was used as guidance and code for creating an available times choice field in the reservation forms.

- [StackoverFlow many to many models validaiton](https://stackoverflow.com/questions/7986510/django-manytomany-model-validation/7986937#7986937) This page was used for guidance in developing a method for preventing overlapping bookings

- [StackoverFlow many to many models validaiton](https://stackoverflow.com/questions/7986510/django-manytomany-model-validation)This page was used for guidance in developing a method for preventing overlapping bookings.

- [StackoverFlow many to many filters](https://stackoverflow.com/questions/2218327/django-manytomany-filter) This page was used for guidance in developing a method for preventing overlapping bookings.

- [StackoverFlow zime zone settings](https://stackoverflow.com/questions/15980302/django-set-datetime-in-views-to-utc1) This page was used for guidance on resetting the current time for the current location time zone

- [W3C validator html/css](https://validator.w3.org/#validate_by_input) these pages were used for the validation and error degubbing processes to finalize the code throughout the project to ensure that all pages met the current standards for accessability and readability.

- [Django primary keys/foreign keys](https://docs.djangoproject.com/en/4.1/topics/db/models/?fbclid=IwAR1DeUwd0LjO066e5O74Ry6UyJGuK6HlQdNt6R7l-3QI8vuay_0MgyGp3XA#field-options) The Django Documentation was read and re-read nearly every day for assistance in making correct code for this project.

- [Django testing processes](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)

- [Bootstrap flex columns and grid help](https://getbootstrap.com/docs/5.2/layout/columns/)

- [Bootstrap modal information](https://getbootstrap.com/docs/5.0/components/modal/)

- 


## Media:
********************

- [Background image/video loop](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.millerandcarter.co.uk%2Frestaurants%2Fscotland-and-northern-ireland%2Fmillerandcarteredinburghcitycentre&psig=AOvVaw0BcdhbWh6sSdGkmrm9zBoj&ust=1669377418830000&source=images&cd=vfe&ved=0CA8QjhxqFwoTCPjNg9LhxvsCFQAAAAAdAAAAABAE) was used for a background video loop.

- [Backround image of a bartender](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.sfgate.com%2Fwine%2Fspirits%2Farticle%2FFive-drinks-that-bartenders-just-hate-to-make-2500138.php&psig=AOvVaw15YutI6WYRkbXBZzARNYCh&ust=1669299861155000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCMip5O_hxvsCFQAAAAAdAAAAABAD)  used in this project

- [Image of people at a bar](https://www.google.com/url?sa=i&url=https%3A%2F%2Fthenounproject.com%2Fphoto%2Fgroup-of-young-people-having-drinks-at-bar-41d2N5%2F&psig=AOvVaw0LUIQY1-saAq8t39rksS0g&ust=1669299224807000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCKCvrJXixvsCFQAAAAAdAAAAABAb) that was used for this project

- [Harbor image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flickr.com%2Fphotos%2Fventeco%2F671328968&psig=AOvVaw0iiN8iburCgWVi5TFiDYJw&ust=1670863908840000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCPi_t7mT8vsCFQAAAAAdAAAAABAE) that was used for this project.

- [A second harbor image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dstrandvagen&psig=AOvVaw0iiN8iburCgWVi5TFiDYJw&ust=1670863908840000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCODx6feT8vsCFQAAAAAdAAAAABAD) that was used for  background in this project.


