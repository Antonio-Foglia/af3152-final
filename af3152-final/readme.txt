Antonio Foglia
af3152
Final

First commit:
The first commit ensured that git was working and was just a test.

Main page:
In this commit I created the main page with the pictures and links to the departments of my majors.

Sport page:
In this commit I create a sport page with my favorite sports to watch. Each of them has a link to a surprise article on the sport

Picture link:
In this commit I added a picture link on the cat picture so that when you press on the picture the cat names are shown.

Formula 1 edit:
In this commit I created a page which allows the user to search formula 1 for any year. This required me to create an HTML form. Trough the file F1_standings.py I use requests, beautiful soup and pandas to extract data from the formula 1 website for the given year and turn it in a pd dataframe. This dataframe is then converted to html and then written to a file. I also had to use Try Except so that the code did not fail if the inputted year did not return a table.  