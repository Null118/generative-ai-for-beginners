from openai import AzureOpenAI

client = AzureOpenAI(api_key='3154ab1d3a6a4abfba45b336c8781fa5',
api_version='2023-05-15',
azure_endpoint='https://null118.openai.azure.com/')
import os
import dotenv


# import dotenv
dotenv.load_dotenv()


deployment = 'gpt-3.5'

# add your completion code
prompt = "Complete the following: Once upon a time there was a"


completion = client.completions.create(model=deployment, prompt=prompt)

# print response
print(completion.choices[0].message.content)
