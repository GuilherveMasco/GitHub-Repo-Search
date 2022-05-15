# GitHub-Repo-Search
## A simple GitHub repository search by topic tool using GH API


### Before running
Before running, you'll need a Access Token from GitHub. If you don't have a token yet, you can get yours on:
> - https://github.com/settings/tokens

This code runs on Python 3.

### Running the tool
The code for the tool is on the src folder, by the file main.py.

To run your repositories search by topic, first you'll have to fill your authentication information (Username and Access Token) in the headers{ } array.

    headers = {
        'User': '###USERNAME###',
        'Authorization': '###TOKEN###'
    }


Save the file and run it with the command

> - python3 main.py ###TOPIC###

Where the ###TOPIC### argument is the desired topic.

The outuput will be generated on the output.json file in the src folder.

By nature, GitHub API will show only the information for the first 30 repositories found by the search.