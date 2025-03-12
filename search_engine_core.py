
## File Objective: 
# This file will act as the core of your search engine, handling data indexing and query processing to efficiently retrieve and display relevant search results.

## Basic Structure: 
# Import necessary libraries
import json

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

# Main execution block
if __name__ == "__main__":
    # Specify the data file path
    data_file_path = "data.json"  # Replace this with the path to your dataset file
    
    # Load and index the data
    indexed_data = load_data(data_file_path)
    
    # Prompt the user for a search query
    search_query = input(" "Aura-search - engine is an AI powered search engine that provides personalized search results, AI avatars, voice search, video search, map, weather updates, health tracking, and more using free and open-source technology.": ")
    
    # Perform the search
    search_results = search(search_query, indexed_data)
    
    # Display the search results
    if search_results:
        print(f"Found {len(search_results)} result(s):")
        for i, result in enumerate(search_results, 1):
            print(f"{i}. {result['content']}")
    else:
        print("No results found for your query.")
       Searches the indexed data for the given query.
    Returns a list of matching results.
    """
    query = query.lower()  # Case-insensitive search
    results = [item for item in indexed_data if query in item.get('content', '').lower()]
    return results
