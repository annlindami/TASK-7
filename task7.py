import sqlite3

# Connect and create sales_data.db
conn = sqlite3.connect("sales_data.db") #If the file already exists, it connects to it.
#If not, SQLite will automatically create a new file named sales_data.db.
cursor = conn.cursor() #cursor is a control handle used to execute SQL commands.

# Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')
#creates a table called sales — if it doesn't already exist.
# Inside the parentheses:the columns and their data types.


# Insert sample data
sample_data = [
    ('Apples', 10, 0.5),
    ('Bananas', 5, 0.3),
    ('Oranges', 8, 0.6),
    ('Apples', 7, 0.5),
    ('Bananas', 12, 0.3),
    ('Oranges', 4, 0.6),
    ('Grapes',12,0.4),
    ('Strawberry',10,0.2)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
#executemany():runs the same SQL statement multiple times with different values.
#"INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)"
#The question marks (?) are placeholders that get filled with actual data from the list we pass in.


conn.commit() #saves all the changes made in the database.
conn.close() #closes the connection to the database.

import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect("sales_data.db")
# Run SQL query
query = '''
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
''' #string containing a valid SQL SELECT statement.
df = pd.read_sql_query(query, conn) #pandas function that: *Executes the SQL *Fetches the result Converts it into a DataFrame
conn.close()

# Print results
print("Sales Summary:")
print(df)

# Plot bar chart for revenue
df.plot(kind='bar', x='product', y='revenue', legend=False, color='pink')
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")  # To Save chart as image
plt.show()
