from googlesearch import search

def test_google_search(query, num_results=5):
  """Tests the googlesearch library and prints the results."""
  try:
    results = list(search(query, num_results=num_results))
    print(f"Search results for '{query}':")
    for i, result in enumerate(results):
      print(f"{i+1}. {result}")
  except ImportError:
    print("Error: The 'googlesearch-python' package is not installed. Please install it using 'pip install googlesearch-python'.")
  except Exception as e:
    print(f"An error occurred during the search: {e}")

# Example usage:
test_google_search("Python programming", num_results=3)
test_google_search("Current weather in London", num_results=2)
