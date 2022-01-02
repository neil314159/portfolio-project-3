# Patient Tracker

Desciption here

The website can be seen [here](https://vaccination-patient-manager.herokuapp.com/).

![Mockup](https://github.com/neil314159/portfolio-project-2/blob/main/docs/screenshot.png) <br>

## Table of Contents
* [Overview](#wireframes)
* [How to Use](#wireframes)
* [Planning](#wireframes)
* [Data Model](#wireframes)
* [OOP Principles](#)
* [Flow of Control](#wireframes)
* [Testing](#wireframes)
* [Third Party Libraries](#wireframes)
* [Features](#Features)
* [Future Features](#possible-future-features)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
* [Validation Testing](#validation-testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Features

### Possible Future Features
* Full name search of users would be useful for larger databases and the project could be extended to handle it.
* The email addresses of users could be collected and they could be emailed reminder notices either via the Heroku server or Zapier automation integrations.

## Third Party Libraries Used

After looking at a number of projects of this type, there are a few factors that seem to contribute to extra code and clutter. The first is storing large strings of ASCII graphics to be printed out in the terminal. The second is validating user input for any interaction through the terminal. For this reason I have used the following libraries as part of my project.

* [Pyfiglet](https://github.com/pwaller/pyfiglet) - This library allows you to generate ASCII titles and text on the fly. You call the library on any piece of text and a string is returned which generates text effects when printed out to the terminal. For example, the word 'Dashboard' is rendered like this:
![dashboardtitle](https://github.com/neil314159/portfolio-project-3/blob/main/docs/dashboardtitle.png)
* [PyInputPlus](https://pypi.org/project/PyInputPlus/) - Designed to handle user input validation, this library lets you offer a number of different prompts for menus, yes/no questions, integers etc. You can restrict the range of acceptable data and make sure that user data is sanitsed before processing it in your program.

## Deployment

### Project Set-up
The Code Institute Python template found [here](https://github.com/Code-Institute-Org/python-essentials-template) was used for this project. This template was pre-configured with useful extensions and allowed me to get the project up and running quickly. I selected a repository name and used Gitpod to start editing my project files.

The Remote/Guide website was deployed to GitHub Pages by following these steps:
1. Navigate to the [Project 1 portfolio](https://github.com/neil314159/portfolio-project-1) on GitHub.
1. Click on the 'Settings' tab.
1. Select 'Pages' from the menu on the left. 
1. Select the 'main' branch in the source selector drop-down.
1. Click 'Save'.
1. After a few moments the website was deployed, and can be accessed here: https://neil314159.github.io/portfolio-project-1/

## Credits
* Fake user data including names and dates of birth were generated on the website [Mockaroo](https://www.mockaroo.com).
* The techniques for connecting to the Google Sheets spreadsheets via API were taken from the Code Institite training materials.
* The table view required some code to iterate over a slice of a list while maintaining a proper index, this was inspired by [this question](https://stackoverflow.com/questions/23159254/python-slices-of-enumerate) on StackOverflow.
* The [documentation](https://github.com/piccolomo/plotext/blob/master/readme/bar.md) for the Plotext library was used to construct the bar chart on the dashboard page.
* The idea of counting Boolean values by simply adding them to quickly sort a list was shown in [this answer](https://stackoverflow.com/questions/16455777/python-count-elements-in-a-list-of-objects-with-matching-attributes#comment23606447_16455812) on StackOverflow.
* The [documentation](https://github.com/jazzband/prettytable) for the PrettyTable library showed how to construct and print properly formatted data.

### Acknowledgements
Thanks to Daisy McGirr for her advice and guidance.