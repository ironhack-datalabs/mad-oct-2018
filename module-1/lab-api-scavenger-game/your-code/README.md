### Problemas
1. identificar el usuario de ironhack

 curl -u albertogcmr: TOKEN https://api.github.com/ironhack-datalabs > outpout.json


primero el espacio

y luego hay que poner user

curl -u albertogcmr:TOKEN https://api.github.com/user > output.json

2. A la hora de trabajar con 

### Generamos archivos
.env -> GITHUB_TOKEN = "asdlfnasfnaskdfs"
.gitignore -> 
    ipynb_checkpoints
    .env
    __pycache__
    .DS_Store
loadCredentials.py
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
        #d = loadCredentials(requestKeys)
        d = loadCredentials(requestKeys)
        print(d)

