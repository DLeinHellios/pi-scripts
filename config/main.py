import json, os

def read_config(appName=None):
    '''
    Returns the config object for the specified app, or all apps 
    if appName is undefined
    '''
    with open('./config/config.json', 'r') as configFile:
        fullConfig = json.load(configFile)

    if appName:
        config = fullConfig.get(appName)
        if config:
            return config
        else:
            raise KeyError(f'ERROR: missing configuration for app "{appName}"')

    return fullConfig
        

if __name__ == "__main__":
    os.chdir("../")
    print("Full Configuration:")
    print(read_config())
    print("-----")
    print("Partial Configuration:")
    print(read_config('net-monitor'))
    print("-----")
    print("Missing Configuration:")
    print(read_config("nope"))