# Canvas-Webscraper
Built a super simple to use web scraper using Python, Homebrew and BeautifulSoup. Helpful for ASU student who want to transcribe any lecture

## Installation
Installation Guide for BeautifulSoup Script
This guide will help you set up and run the BeautifulSoup script to extract text from HTML elements with the class "caption-content".
Prerequisites
Before you begin, ensure you have the following installed on your computer:
Python 3
pip (Python package installer)
Installation Steps
Install BeautifulSoup4:
BeautifulSoup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files. You can install it using pip:

bash
Copy code
pip install beautifulsoup4
Install lxml (Optional):
lxml is a Python library that provides a way to work with XML and HTML documents. It is optional but recommended for faster parsing with BeautifulSoup. Install it using pip:

bash
Copy code
pip install lxml
Prepare Your HTML File:
Ensure you have an HTML file named file.html in the same directory as your script. This file should contain the HTML code you want to scrape.

Running the Script:
To run the script, navigate to the directory containing your script and HTML file in the terminal or command prompt, and execute the following command:

bash
Copy code
python extract.py
Replace extract.py with the name of your file if have updated it.

Output
The script will print the extracted text from elements with the class "caption-content" to the console. If you want to save the output to a text file, you can modify the script to write the output to a file. However the output for the above code is setup to where it outputs in the file directory of your choosing.

## Questions
if you have any questions or issues reach out to me on discord: dee_16452
