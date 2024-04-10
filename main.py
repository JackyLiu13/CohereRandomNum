import os
import re
import cohere
from dotenv import load_dotenv
import json

# Load API keys from .env file
load_dotenv()
api_key = os.getenv("CO_API_KEY")
co = cohere.Client(api_key=api_key)
numbers = dict()

for temp in range(0,11):
    temperature = temp/10
    print(temperature)
    numbers[temperature] = []
    for i in range(1, 101):
        response = co.chat(
            message="Pick a number between 1 - 100",
            temperature=temperature,
        )
        # Extract number from response text
        number = re.search(r'\d+', response.text).group()
        print(number)
        numbers[temperature].append(int(number))
print(numbers)
# save the dictionary to a file as json
with open('numbers.json', 'w') as f:
    json.dump(numbers, f)

