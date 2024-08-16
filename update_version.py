

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

    with open("setup.py","r") as fp:
        data = fp.readlines()
    for i in range(len(data)):
        if "VERSION" in data[i]:
            old_version = data[i].split("\"")[1]
            new_version = update_version(old_version)
            print(f"Old version: {old_version}")
            print(f"New version: {new_version}")
            data[i] = f"VERSION = \"{new_version}\"\n"
            break
    with open("setup.py","w") as fp:
        fp.writelines(data)
    print(f"Version updated to {new_version}")
