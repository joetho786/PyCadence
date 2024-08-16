from version import __version__ as VERSION

def update_version(version:str):
    version = version.split(".")
    # increment the last digit if it is less than 9 else update the second last digit and so on
    for i in range(len(version)-1,-1,-1):
        if int(version[i]) < 9:
            version[i] = str(int(version[i])+1)
            break
        else:
            version[i] = "0"
    return ".".join(version)
    

if __name__ == "__main__":
    new_version = update_version(VERSION)
    print(f"New version: {new_version}")
    with open("version.py", "w") as f:
        f.write(f'__version__ = "{new_version}"')
  
