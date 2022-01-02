# Patient Tracker

Desciption here

The website can be seen [here](https://vaccination-patient-manager.herokuapp.com/).

![Mockup](https://github.com/neil314159/portfolio-project-2/blob/main/docs/screenshot.png) <br>

## Table of Contents
* [Overview](#wireframes)
* [How to Use](#wireframes)
* [Planning](#wireframes)
* [Data Model](#wireframes)
* [OOP Principles and Data Model](#)
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

# Features

## Possible Future Features
* Full name search of users would be useful for larger databases and the project could be extended to handle it.
* The email addresses of users could be collected and they could be emailed reminder notices either via the Heroku server or Zapier automation integrations.

## Third Party Libraries Used

After looking at a number of projects of this type, there are a few factors that seem to contribute to extra code and clutter. The first is storing large strings of ASCII graphics to be printed out in the terminal. The second is validating user input for any interaction through the terminal. For this reason I have used the following libraries as part of my project.

* [Pyfiglet](https://github.com/pwaller/pyfiglet) - This library allows you to generate ASCII titles and text on the fly. You call the library on any piece of text and a string is returned which generates text effects when printed out to the terminal. For example, the word 'Dashboard' is rendered like this: <br>
![dashboardtitle](https://github.com/neil314159/portfolio-project-3/blob/main/docs/dashboardtitle.png)
* [PyInputPlus](https://pypi.org/project/PyInputPlus/) - Designed to handle user input validation, this library lets you offer a number of different prompts for menus, yes/no questions, integers etc. You can restrict the range of acceptable data and make sure that user data is sanitised before processing it in your program.

Other libraries used include:
* [PrettyTable] (https://github.com/jazzband/prettytable) - printing lists of names can be difficult to format correctly. This library handles constructing the table and printing it in a pleasing layout, while also letting you set maximum widths for certain columns which is important when outputting to a terminal.
* [Termcolor](https://pypi.org/project/termcolor/) allows the use of colours in text output on the terminal. This was used to highlight menu options and make the interface more visually appealing.
* [Plotext] (https://github.com/piccolomo/plotext) is a library that generates charts and plotting graphics. This was implemented on the dashboard page of the project, takng overall data on patient vaccination rates and shoing it as a bar chart.
* Gspread / Google Auth - these were used to set up the connection to Google Sheets. The spreadsheet was used to store the user records, and these APIs were used to read, edit and delete data.

## Technologies Used
* Python 
    * The entirety of this project was written in the Python language.
* [Github](https://github.com) 
    * GitHub is used to host the source code of the project.
* [Gitpod](https://gitpod.io) 
    * Gitpod was the development environment for this site and linked to Github for storage and deployment.
* [MacOS Preview](https://support.apple.com/guide/preview/welcome/mac)
    * This prpgram was used to capture and edit screenshots of the site.
* [Heroku](https://dashboard.heroku.com/)
    * Used as a server for the project once deployed.
* [LucidChart](https://www.lucidchart.com/)
    * For creating charts and flow diagrams.
* [PEP8](http://pep8online.com/)
    * Python code validation service.

## Validation Tsting
* Python: All code was tested using the [PEP8 Validator](http://pep8online.com/). The code shows no errors and no warnings. Most of the inital warnings that required fixing were about keepinng all code within the 80 character limit.


# Deployment

## Creating the Project
1. A new repository was created for the project on GitHUb by clicking 'New Repository' on the GitHUb user page, giving a name to the project.
1. The GitPod link created by the Chrome extension was clicked on the Code Institute Python template found [here](https://github.com/Code-Institute-Org/python-essentials-template).
1. This created a virtual workspace which was linked to my GitHUb account.
1. After writing code for the project, I used git commands add, commit and push which sent all the project files from GitPod to my GitHub repository.

## Deploying to Heroku
The project was deployed on the Heroku site by using these steps:
1. Log into Heroku after creating a user account if necessary.
1. Select the 'New' button and click 'Create New App'.
1. Choose a unique name for your app.
1. Add the buildpacks for Python and NodeJS from the settings page for your project. They must be added in this order.
1. Add the configuration variables for your app on the settings page. These incluse PORT=8000 and the credentials used for your API access.
1. On the settings page, click the 'Deploy' tab.
1. Select GitHub as the method for deplyments.
1. Sign in when prompted with your GitHub login and search for the repository for your project.
1. Click the correct repository and click 'Connect'.
1. Under the deployment type section, you can choose between automatic deployment whenever you push updated code to GitHub, or manual deployment where you must confirm that you want the site updated.

## Local Deployment

#### Forking the repo on GitHub
1. Log into your GitHub account.
1. Navigate to the project page found [here](https://github.com/neil314159/portfolio-project-3).
1. Click the 'Fork' icon on the upper right hand side of the screen.
1. This action copies the code into yoru own repo so you can examine and edit it in the development environment of your choice.

#### Cloning to Gitpod
1. Install the Google Chrome Gitpod plugin found [here](https://github.com/neil314159/portfolio-project-3).
1. Navigate to the project repository page [here](https://github.com/neil314159/portfolio-project-3).
1. Click the green GitPod button on the top right of the screen.
1. This will open the project in a virtual GitPod workspace.
1. Install the required libraries by executing the command 'pip3 install -r requirements.txt' in your GitPod terminal.


#### Download a zip file of the source code
1. Click this [link](https://github.com/neil314159/portfolio-project-3) to the project home page.
1. Click the 'Code' button on the right hand side.
1. Select "Download Zip'
1. Decompress the files on your own machine.
1. Open them in your local IDE such as VSCode.


### Project Set-up
The Code Institute Python template found [here](https://github.com/Code-Institute-Org/python-essentials-template) was used for this project. This template was pre-configured with useful extensions and allowed me to get the project up and running quickly. I selected a repository name and used Gitpod to start editing my project files.

The Remote/Guide website was deployed to GitHub Pages by following these steps:
1. Navigate to the [Project 1 portfolio](https://github.com/neil314159/portfolio-project-1) on GitHub.
1. Click on the 'Settings' tab.
1. Select 'Pages' from the menu on the left. 
1. Select the 'main' branch in the source selector drop-down.
1. Click 'Save'.
1. After a few moments the website was deployed, and can be accessed here: https://neil314159.github.io/portfolio-project-1/

# Credits
* Fake user data including names and dates of birth were generated on the website [Mockaroo](https://www.mockaroo.com).
* The techniques for connecting to the Google Sheets spreadsheets via API were taken from the Code Institite training materials.
* The table view required some code to iterate over a slice of a list while maintaining a proper index, this was inspired by [this question](https://stackoverflow.com/questions/23159254/python-slices-of-enumerate) on StackOverflow.
* The [documentation](https://github.com/piccolomo/plotext/blob/master/readme/bar.md) for the Plotext library was used to construct the bar chart on the dashboard page.
* The idea of counting Boolean values by simply adding them to quickly sort a list was shown in [this answer](https://stackoverflow.com/questions/16455777/python-count-elements-in-a-list-of-objects-with-matching-attributes#comment23606447_16455812) on StackOverflow.
* The [documentation](https://github.com/jazzband/prettytable) for the PrettyTable library showed how to construct and print properly formatted data.

## Acknowledgements
Thanks to Daisy McGirr for her advice and guidance.