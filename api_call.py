import requests
import pandas as pd
import webbrowser
import os

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    # Convert the JSON data to a pandas DataFrame
    df = pd.DataFrame(data)
    # Store the DataFrame in a CSV file
    df.to_csv("posts_data.csv", index=False)
    print("Data fetched successfully:")
    # Print the first few rows of the DataFrame
    print(df.head())
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# show only specific columns
df = df[["userId", "title", "body"]]
# Convert DataFrame to HTML table and open in browser
data_html = df.to_html(index=False)

html_file = "posts_data.html"

# === For better looking HTML file with Bootstrap CSS

html_template = f"""
<html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
          <style>   
            th {{
                text-align: center;
            }}
            td {{
                text-align: center;
            }}
             /* Left align only title and body columns */
            td:nth-child(2), 
            td:nth-child(3) {{
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Post List</h2>                    
            {df.to_html(classes="table table-striped table-bordered", index=False)}
        </div>
    </body>
</html>
"""

# Write the HTML content to a file
with open(html_file, "w") as f:
    f.write(html_template)

# Open the HTML file in the default web browser
webbrowser.open(f"file://{os.path.abspath(html_file)}")
