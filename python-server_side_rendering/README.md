## Tasks

### 1.

In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.

### Objective

*   Understand how to use string templating in Python.
*   Implement file operations for reading templates and writing output files.
*   Handle various edge cases and errors gracefully.

* * *

### Instructions

1.  **Create the Template:**
    
    *   Use the provided template with placeholders for `name`, `event_title`, `event_date`, and `event_location`.
2.  **Define the Data:**
    
    *   Use the provided list of objects as your data source.
3.  **Write the Templating Function:**
    
    *   Define a function named `generate_invitations` that takes two parameters: `template` and `attendees`.

*   **Check Input Types:**
    
    *   Verify that `template` is a string and `attendees` is a list of dictionaries.
    *   If `template` is not a string or `attendees` is not a list of dictionaries, log an error message and terminate the function.
*   **Handle Empty Inputs:**
    
    *   Check if the template is empty and log an error message if it is.
    *   Check if the attendees list is empty and log an error message if it is.
*   **Process Each Attendee:**
    
    *   Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
    *   If a value is missing, replace it with “N/A”.
*   **Generate Output Files:**
    
    *   Write the processed template to output files named `output_X.txt`, where `X` is the index of the attendee starting from 1.

1.  **Specific Error Handling Behaviors:**
    *   **Empty Template:** If the template is empty, log an error message, “Template is empty, no output files generated.” and terminate without creating any files.
    *   **Empty List of Objects:** If the list of objects is empty, log a message, “No data provided, no output files generated.” and terminate without creating any files.
    *   **Missing Data in Object:** If an object is missing data for any of the placeholders, replace the missing data with the text “N/A” in the output file. For example, if `event_date` is missing, it should appear as “event\_date: N/A” in the output.
    *   **Invalid Input Types:** If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.

* * *

### Template **File:** ``template.txt``
```
Hello {name},

You are invited to the {event\_title} on {event\_date} at {event\_location}.

We look forward to your presence.

Best regards,
Event Team
```
### Example Data for Testing:
```
attendees = \[
    {"name": "Alice", "event\_title": "Python Conference", "event\_date": "2023-07-15", "event\_location": "New York"},
    {"name": "Bob", "event\_title": "Data Science Workshop", "event\_date": "2023-08-20", "event\_location": "San Francisco"},
    {"name": "Charlie", "event\_title": "AI Summit", "event\_date": None, "event\_location": "Boston"}
\]
```
### Example Main File to Test the Program:
```
\# Main file content
from task\_00\_intro import generate\_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template\_content = file.read()

# List of attendees
attendees = \[
    {"name": "Alice", "event\_title": "Python Conference", "event\_date": "2023-07-15", "event\_location": "New York"},
    {"name": "Bob", "event\_title": "Data Science Workshop", "event\_date": "2023-08-20", "event\_location": "San Francisco"},
    {"name": "Charlie", "event\_title": "AI Summit", "event\_date": None, "event\_location": "Boston"}
\]

# Call the function with the template and attendees list
generate\_invitations(template\_content, attendees)
```
* * *

### Hints:

*   Use Python’s string `replace` method to substitute placeholders with actual values.
*   Use `os.path.exists` to check if a file already exists before writing.
*   Use `try` and `except` blocks to handle potential errors gracefully.

* * *

### Resources:

*   **Python String Methods**: [Python Official Documentation](/rltoken/W6bJdwDnBI2Ei0brfUqCJw "Python Official Documentation")
*   **File Handling in Python**: [Python Official Documentation](/rltoken/1T4vhH1weF8SheeeZYeeLA "Python Official Documentation")

  

### 2.

In this task, you will build a basic Flask application that serves a web page using a Jinja template. You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.

### Objective

*   Set up a Flask environment and create a basic Flask application.
*   Design HTML templates using Jinja for dynamic content rendering.
*   Implement reusable components in templates to maintain consistent layout across pages.

* * *

### Instructions

1.  **Set Up Your Flask Environment:**
    
    *   Ensure Python is installed on your system.
    *   Install Flask using pip: `sh pip install Flask`
2.  **Create a Basic Flask Application:**
    
    *   In your project directory, create a Python file named `task_01_jinja.py`.
    *   Write a basic Flask application with a route that renders an HTML template.
```
from flask import Flask, render\_template

   app = Flask(\_\_name\_\_)

   @app.route('/')
   def home():
       return render\_template('index.html')

   if \_\_name\_\_ == '\_\_main\_\_':
       app.run(debug=True, port=5000)
```
1.  **Design Your HTML Template:**
    *   In a `templates` folder within your project directory, create an HTML file named `index.html`.
    *   Design a simple HTML page with a heading (`<h1>`), a paragraph (`<p>`), and an unordered list (`<ul>` with `<li>` items).

Content for `index.html`:
```
<!doctype html>
   <html lang="en">
   <head>
       <title>My Flask App</title>
   </head>
   <body>
       <h1>Welcome to My Flask App</h1>
       <p>This is a simple Flask application.</p>
       <ul>
           <li>Flask</li>
           <li>HTML</li>
           <li>Templates</li>
       </ul>
   </body>
   </html>
```
1.  **Render the Template in Flask:**
    
    *   Use Flask’s `render_template` function to render the HTML template when the corresponding route is accessed.
2.  **Create Reusable Header and Footer Templates:**
    
    *   In the `templates` folder, create two new HTML files: `header.html` and `footer.html`.
    *   Design simple but distinct layouts for the header and footer, and include navigation links (Home, About, Contact) to all pages into header file.

Content for `header.html`:
```
<header>
       <h1>My Flask App</h1>
   </header>
```
Content for `footer.html`: `html <footer> <p>&copy; 2024 My Flask App</p> </footer>`

1.  **Design Multiple Pages with Shared Header and Footer:**
    *   Create additional HTML pages `about.html` and `contact.html`.
    *   In each of these pages (`index.html`, `about.html` and `contact.html`), include the header and footer templates without duplicating their code.
```
- Add specific tags for each page:
     - In \`about.html\`, include an   \`<h1>\` tag with the text "About Us" and a paragraph (\`<p> \`) with content describing the page.
     - In \`contact.html\`, include an  \`<h1> \`  tag with the text "Contact Us" and a paragraph (\`<p>\`) with content for the contact page.
```
1.  **Modify Flask Routes:**
    *   Add new routes in your Flask application corresponding to the additional pages you created.
```
@app.route('/about')
   def about():
       return render\_template('about.html')

   @app.route('/contact')
   def contact():
       return render\_template('contact.html')
```
* * *

### Hints:

*   Ensure your Flask application runs on port 5000.
*   Use the `render_template` function from Flask to render HTML templates.
*   Utilize Jinja’s `{% include %}` statement to include reusable components like headers and footers.

* * *

### Resources:

*   **Flask Quickstart:** [Flask Quickstart](/rltoken/xLnef6coA0Lgt71gTcnS5Q "Flask Quickstart")
*   **HTML Basics:** [HTML Tutorial on W3Schools](/rltoken/3s9aM9mrDsmWx6I-V7zokw "HTML Tutorial on W3Schools")
*   **Flask Templating with Jinja:** [Flask Templating](/rltoken/RWlt7-FqgostaP1MpAJnXg "Flask Templating")
*   **Jinja Template Inheritance:** [Jinja Template Inheritance](/rltoken/oT7L0anPHrZ-Q42K1Lp8ig "Jinja Template Inheritance")

  

### 3.

In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.

### Objective

*   Use Jinja’s loop and conditional constructs to dynamically render content in HTML templates.
*   Read and parse JSON data in Python.
*   Integrate dynamic content into your Flask application.

* * *

### Instructions

1.  **Prepare Your Flask Application:**
    
    *   Continue using the Flask application you created in the previous exercises.
    *   Ensure you have a basic understanding of Jinja’s templating syntax.
2.  **Create a Dynamic Template:**
    
    *   In your `templates` folder, create a new HTML template named `items.html` with “Items List” for the title.
    *   This template should include a loop to iterate over a list of items and display each item.
    *   Items must be displayed as an **unordered list**.
    *   Add a conditional statement to display a message “**No items found**” if the list is empty.
3.  **Define the Data for the Template:**
    
    *   In your project directory, create a file named `items.json`.
    *   Populate `items.json` with a list of items:
    
     {
         "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
     }
    

*   Experiment with different lists, including an empty list, to see how your template responds.

1.  **Add a Route in Flask:**
    *   Create a new route `/items` in your Flask application to render the `items.html` template with the list of items.
    *   Use Python’s `json` module to read the data from `items.json`.
    *   Pass the list of items to the template for rendering.

* * *

### Data for Testing:
```
{
    "items": \["Python Book", "Flask Mug", "Jinja Sticker"\]
}
```
* * *

### Hints:

*   Use Python’s `json` module to read data from the JSON file.
*   Utilize Jinja’s `{% for %}` loop to iterate over the list of items in the template.
*   Use the `{% if %}` statement to conditionally display the message when the list is empty.
*   Define the new route `/items` in your Flask application and use the `render_template` function to pass the list of items to `items.html`.

* * *

### Resources:

*   **Jinja Template Designer Documentation:** [Jinja Template Designer Documentation](/rltoken/8JdOhBd-JaExBWwtyVJuew "Jinja Template Designer Documentation")
*   **Flask Templating with Jinja:** [Flask Templating](/rltoken/RWlt7-FqgostaP1MpAJnXg "Flask Templating")

* * *

### Testing Your Application:

After setting up the dynamic template and route, run your Flask application and navigate to the new route. Verify that the list of items is correctly displayed on the page. Test with different lists, including an empty list, to ensure that the conditional statement works as expected.

  

### 4.

In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional `id` query parameter. Additionally, you will handle edge cases such as invalid `source` parameter values or when the specified `id` is not found in the data.

### Objective

*   Read and parse data from JSON and CSV files.
*   Use query parameters in Flask to determine data sources and filter criteria.
*   Implement error handling for invalid inputs and missing data.
*   Render dynamic data in HTML templates using Jinja.

* * *

### Instructions

1.  **Prepare Data Files:**
    
    *   Create a JSON file (`products.json`) containing a list of products, each with an `id`, `name`, `category`, and `price`.
        
        Example JSON content format: `json [ {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99}, {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99} ]`
        

*   Create a CSV file (`products.csv`) with similar data, using columns for `id`, `name`, `category`, and `price`.
    
     Example CSV content:
     id,name,category,price
     1,Laptop,Electronics,799.99
     2,Coffee Mug,Home Goods,15.99
    

1.  **Create a Dynamic Template:**
    
    *   In your `templates` folder, create an HTML template `product_display.html` for displaying the product data.
    *   Design the template to display the data in a table format with headings for Name, Category, and Price.
2.  **Modify Flask Application:**
    
    *   In `task_03_files.py`, create a route in your Flask application that accepts a `source` query parameter (values `json` or `csv`) and an optional `id`.
    *   Depending on the `source` parameter, read and parse data from the corresponding file.
    *   Implement logic to filter data by the specified `id` if provided. If `id` is not provided, display all products.
    *   Pass the parsed data to the `product_display.html` template for rendering.
3.  **Implement File Reading Logic:**
    
    *   Write functions to read and parse data from both JSON and CSV files.
    *   Ensure the data is converted into a format that can be easily displayed by the template.
4.  **Handle Edge Cases:**
    
    *   If `source` is neither `json` nor `csv`, return a “Wrong source” error message in the template.
    *   If `id` is provided but not found in the file, display a “Product not found” error message in the template.
    *   Modify the `product_display.html` template to handle and display error messages if necessary.

* * *

### Hints:

*   Use Python’s `json` module to read data from the JSON file.
*   Use Python’s `csv` module to read data from the CSV file.
*   Utilize Flask’s `request.args` to get query parameters.
*   Use Jinja’s templating features to conditionally display error messages and dynamic data.

* * *

### Resources:

*   **Reading JSON and CSV in Python:**
    *   JSON: [JSON in Python](/rltoken/lC6m9GFhAWqgqvmSlA3y5g "JSON in Python")
    *   CSV: [CSV File Reading and Writing](/rltoken/FwAYKq-BrdtZlNodGDxsag "CSV File Reading and Writing")
*   **Flask Request Object:** [Flask Request Object](/rltoken/eQhOfyVFkLC5gR3NhPoVsA "Flask Request Object")
*   **Query Parameters in Flask:** [Flask Request Object](/rltoken/eQhOfyVFkLC5gR3NhPoVsA "Flask Request Object")
*   **Error Handling in Flask:** [Flask Error Handling](/rltoken/c3p6vS48JY-Dvimfj3NPbw "Flask Error Handling")

* * *

### Testing Your Application:

Test your application with various scenarios:

*   Access URLs like `http://localhost:5000/products?source=json`, `http://localhost:5000/products?source=csv`, and `http://localhost:5000/products?source=xml` (invalid source).
*   Test with and without the `id` parameter, and with both valid and invalid `id` values.
*   Verify that the application correctly filters data, displays all products when no `id` is provided, and shows appropriate error messages for edge cases.

  

### 5.

Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the `source` query parameter.

### Objective

*   Set up and interact with a SQLite database in a Flask application.
*   Extend existing functionality to handle multiple data sources.
*   Implement error handling for database-related issues.

* * *

### Instructions

1.  **Database Setup:**
    *   **SQLite Database **File:** `**`
        *   Name your SQLite database file `products.db`.

*   **Table Structure:**
    
    *   Create a `Products` table with columns: `id` (primary key), `name`, `price`, `category`.
*   **Example Data:**
    
    *   Insert the following data into the `Products` table:
        *   `id`: 1, `name`: “Laptop”, `price`: 799.99, `category`: “Electronics”
        *   `id`: 2, `name`: “Coffee Mug”, `price`: 15.99, `category`: “Home Goods”

Use the following script to create and populate the database:
```
import sqlite3

   def create\_database():
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

   if \_\_name\_\_ == '\_\_main\_\_':
       create\_database()
```
1.  **Modify the Existing Dynamic Template:**
    
    *   Use the same HTML template (`product_display.html`) created in Task 3 for displaying product data.
2.  **Implement SQLite Data Source:**
    
    *   Extend the existing Flask route to handle `source=sql` as a query parameter.
    *   Implement logic to fetch data from the SQLite database when this parameter is used.
    *   Ensure that the same template is used to display data regardless of the source.
3.  **Handle Error Cases:**
    
    *   As in Task 3, display a “Wrong source” error message if an invalid `source` is provided.
    *   Implement appropriate error handling for database-related errors.

* * *

### Hints:

*   Use Python’s `sqlite3` module to interact with the SQLite database.
*   Define a function to read data from the SQLite database and convert it into a format suitable for rendering in the template.
*   Use Flask’s `request.args` to get the `source` query parameter and determine the data source.

* * *

### Resources:

*   **Flask-SQLAlchemy:** [Flask-SQLAlchemy](/rltoken/JBmvcrjCCGZGlWw1M-OI3A "Flask-SQLAlchemy")
*   **SQLite in Python:** [SQLite3 Module](/rltoken/wPc6yZmq5N00DfY5cfWRYQ "SQLite3 Module")

* * *

### Testing Your Application:

Test your application with the URL query parameter set to `json`, `csv`, and `sql` to ensure that the correct data is displayed for each source. Verify that the application can handle and display errors appropriately for invalid sources or database issues.