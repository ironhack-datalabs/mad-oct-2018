import os

#https://github.com/theskumar/python-dotenv
from dotenv import load_dotenv

def loadCredentials(loadVars):
    load_dotenv()
    obj = dict()
    for v in loadVars:
        obj[v] = os.getenv(v)
        if not obj[v]:
            raise ValueError("env var '%s' does not exist. Please create a .env file containing it" % (v))
    return obj

if __name__ == "__main__":
    requestKeys = ["GITHUB_TOKEN"]
    d = loadCredentials(requestKeys)
