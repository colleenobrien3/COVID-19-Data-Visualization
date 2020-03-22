# Python Flask SQL API

## Description and Features

I created an API that contains data about COVID-19 cases. I found a dataset online and downloaded it into my directory. Using Peewee and Postgresql, I defined a model for a table and seeded the data from the CSV file into a local database. I then used Flask to connect the database to a local browser and define the API's routes. The paths are defined below. I did all of this in the app.py file of the project.
Then, I decided I wanted data about specific US states, so I decided to refactor things. I found information on worldometers.com and decided I wanted to use web scraping to obtain the data. The data was updated every day, and therefore I could rerun my program each day to get the most up-to-date data. I downloaded BeautifulSoup, UrlLib, and requests, and used them in main.py to pull data from the website. I manipulated the data returned from the web scraping and placed it into json objects in data.txt using json.dump(). Once the data was in the right format, I refactored app.py in a new file, newApp.py, to create the tables in Postgresql.
Next, I wanted to create a user friendly visualization of the data. I installed Anaconda, Seaborn, Pandas, and MatPlotLib and created the file sea_otter.py. In this file, I used these libraries to create a simple table visualization of my data. I also installed Jupyter Notebook and played with some visualizations there. Unfortunately, since my data is actually all strings, I was unable to create certain tables.

![Jupyter Notebook]('./Screen Shot 2020-03-22 at 6.03.19 PM.png')

## Paths

| Method |     Path     | Description                                    |
| ------ | :----------: | ---------------------------------------------- |
| GET    |   /state/    | Retrieves all states and their information     |
| GET    |  /state/:id  | Retrieves the state with matching id parameter |
| POST   |   /state/    | Adds a new state to the table                  |
| PUT    |     /:id     | Updates a recipe using its id as a parameter   |
| DELETE | /delete/<id> | Deletes a state using its id as a parameter    |

## Technologies Used

- Python
- Postgresql
- PeeWee
- Flask
- BeautifulSoup
- UrlLib
- Requests
- Json
- Anaconda
- Seaborn
- Pandas
- MatPlotLib

## Getting Started

## Goals

Next, I plan on refactoring my data so that I can create better visualizations using Jupyter Notebook.
