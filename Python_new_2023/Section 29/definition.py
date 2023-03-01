import requests
import json

# Enter your Dictionary.com API key here
api_key = "ddd4507d-803f-4389-8a0a-1c9b91d33723"


def get_word_definition(word):
    # Define the endpoint and parameters for the API request
    endpoint = "https://www.dictionaryapi.com/api/v3/references/collegiate/" \
               "json/" + word.lower() + "?key=" + api_key

    # Make the API request and get the response
    response = requests.get(endpoint)

    # Parse the JSON response and extract the definition
    definition = None
    try:
        data = json.loads(response.text)
        definition = data[0]["shortdef"][0]
    except:
        definition = "Sorry, no definition found for " + word

    # Return the definition as a string
    return definition
