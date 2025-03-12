
## File Objective: 
# This file will act as the core of your search engine, handling data indexing and query processing to efficiently retrieve and display relevant search results.

## Basic Structure: 
# Import necessary libraries


import json

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Extract details from JSON
name = data.get('name')
age = data.get('age')
city = data.get('city')
search_criteria = data.get('search', '')

# Implement search logic
def search_engine_core(criteria):
    # Example search logic
    if criteria in name:
        return f"Found '{criteria}' in name: {name}"
    elif criteria in city:
        return f"Found '{criteria}' in city: {city}"
    else:
        return f"'{criteria}' not found"
# Perform search
result = search_engine_core(search_criteria)
print(result)
# Function to load and index data
def load_data(file_path):
    """
    Loads data from a JSON file and indexes it.
    Returns the indexed data as a list of records.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("Data successfully loaded and indexed.")
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file content.")
        return []

# Function to search the indexed data
def search(query, indexed_data):
    """
    Searches the indexed data for the given query.
    Returns a list of matching results.
    """
    query = query.lower()  # Case-insensitive search
    results = [item for item in indexed_data if query in item.get('content', '').lower()]
    return results
