from os import mkdir, path

_INITIALIZED_ = False
_CREATED_ = False


def init() -> None:
    global _INITIALIZED_

    try:
        mkdir('./.dtg')
        print("Initializing dtg models repository...")
        _INITIALIZED_ = True
    except FileExistsError:
        print("Repository folder already exists")
        exit(1)
    except PermissionError:
        print("Apparently you don't have permission, try with sudo")
        exit(1)

    try:
        if path.exists('./.dtg/'):
            with open("./.dtg/models.dat", "w"):
                print("Done.")
                _INITIALIZED_ = True
    except IOError:
        print("Something went wrong, ups 🤦🏽")
        exit(1)
