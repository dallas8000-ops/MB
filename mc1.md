Mini Challenge 3 - Create project from scratch

Create the basic structure for a django project
Create a virtual environment and activate it
Install django and create the config folder (django-admin startproject config .)

Run the pip freeze > requirements.txt to create the txt file


Set up the configurations on settings.py
Add the folders for statics and templates
Create two new apps called pages and posts

# Mini Challenge 4 - Create a home page and about page with a blueprint
1. Create a base.html inside of the templates folder and add the following:
   - A block for the title
   - A block for extra css
   - A block for the content
   - A block for extra js
   - Add bootstrap link and script
   - Include a navbar
2. Create a home.html and about.html inside of templates/pages and add the following to each one:
   - a title
   - an h1 title
   - a paragraph (if you want to add more stuff feel free to do it!)
3. Create the urls for the home and about page.
4. Create the views to link the htmls
5. Make sure to link the children urls inside of the parent one (config.urls)
