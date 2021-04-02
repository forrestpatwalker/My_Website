# Purpose
The purpose for this app is to serve as a portfolio for myself. Currently I have an about me section, a skills section that focuses on which programming languages I like to use, a work section where my past and future projects will be displayed, a contact form so anyone who wants to reach out me can, and a way to download my resume incase any potential recruiters/hiring managers are looking.

# Major Functions
[Here](https://github.com/foorast/My_Website/tree/main/my_website/templates/my_website) you will find all of the html files that make up the site. They all inherit from [base.html](https://github.com/foorast/My_Website/blob/main/my_website/templates/my_website/base.html) keeping the other files condensed to just the html code that differentiates the pages. 

All of the templates are individual pages with the [details.html](https://github.com/foorast/My_Website/blob/main/my_website/templates/my_website/details.html) being the only exception. By using a database filled with information about my past projects the details.html file is able to loop through each object within the database and display their content within this file. This allows the site to only need one details.html page that will cover all of my current and future projects. This is the primary reason for having a backend to the site.

[models.py](https://github.com/foorast/My_Website/blob/main/my_website/models.py) this file is used to set up the database.

[views.py](https://github.com/foorast/My_Website/blob/main/my_website/views.py) is where web requests are taken in and returns the proper web response in the case for this app the response are always the HTML contents of a web page found in the [templates folder](https://github.com/foorast/My_Website/tree/main/my_website/templates/my_website).

[urls.py](https://github.com/foorast/My_Website/blob/main/my_website/urls.py) is where the URL dispatcher is utilized to give the different pages their URL.

The only PHP file utilized is [ContactForm](https://github.com/foorast/My_Website/blob/main/my_website/static/my_website/contactForm.php) that handles the contact form page and sends the contents of the form to my email.

The rest of the files are standard Django files that may become more relevant down the line.

# Dependencies
All of the dependencies are found within the [static folder](https://github.com/foorast/My_Website/tree/main/my_website/static/my_website) here you will find the [css stylesheet](https://github.com/foorast/My_Website/blob/main/my_website/static/my_website/styles.css) which handles all the websites styling. 

You will also find the [folder img](https://github.com/foorast/My_Website/tree/main/my_website/static/my_website/img) that stores the images used throughout the site.

Last you have the jQuery dependencies found within the [JS Folder](https://github.com/foorast/My_Website/tree/main/my_website/static/my_website/JS) These are primarily used with the nav bar on the site and is how the dropdown contact portion of the navbar works.

# Build/Deply Instructions
1. In order to build an app like this one or modify the contents of this you are going to need the latest version of python found [here](https://www.python.org/downloads/).
2. Look up the different IDE's used for python and determine which you would like to use and download it. I used Pycharm you can find them [here](https://www.jetbrains.com/pycharm/)
3. Next it is time to set up your [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). Open up a terminal and create a new directory (name it whatever you want), once created move into that folder. Then run the command ```python3 -m venv .env``` then run ```source .env/bin/activate``` this should start up your virtual environment (if you see (.env) to the left you are in a virutal environment).
4. Now that you are here use the ```pip install django``` command to download the latest version of django.
5. Go ahead and open up that folder in your IDE now and you are set to start building/modifying a django project.
6. If you are looking for further instructions Django has a lot it can do and I can't list them all here but check out [Real Pyhton's learning path](https://realpython.com/learning-paths/django-web-development/) they are extremly good tutorials on Django and can help get you started with whatever you are doing.
