from bs4 import BeautifulSoup

# Read the HTML code from file.html
with open('file.html', 'r') as file:
    html_code = file.read()

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Open a new text file for writing the extracted text
with open('output.txt', 'w') as output_file:
    # Extract and write the text from each caption to the text file
    for caption in soup.find_all(class_="caption-content"):
        extracted_text = caption.get_text()
        output_file.write(extracted_text + '\n')  # Write the text with a newline
