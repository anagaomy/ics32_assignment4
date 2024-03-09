# a4.py

# Ana Gao
# gaomy@uci.edu
# 26384258

import profile
import ui as run
from pathlib import Path
import pathlib
from Profile import Profile as profile
from Profile import Post as post
from ds_client import send


def input_error_check(data: str, journal):
    if len(data.strip().split()) != 1:
        print("Do NOT contain whitespace!")
        Path(journal).unlink()
        return False
        # exit()


def user_bio_error_check(data: str, journal):
    if len(data) == 0:
        print("Error! Invalid bio!")
        Path(journal).unlink()
        return False
        # exit()
    else:
        if data.isspace():
            print("Error! Invalid bio!")
            Path(journal).unlink()
            return False
            # exit()


def list_contents(directory):
    myPath = Path(directory)
    paths = myPath.iterdir()
    pathsList = []
    for currentPath in sorted(paths, key=lambda p: (p.is_dir(), p.name)):
        pathsList.append(currentPath)
    return pathsList


def list_recursively(directory):
    myPath = Path(directory)
    paths = myPath.iterdir()
    pathsList = []
    for currentPath in sorted(paths, key=lambda p: (p.is_dir(), p.name)):
        if currentPath.is_file():
            pathsList.append(currentPath)
        elif currentPath.is_dir():
            pathsList.append(currentPath)
            for path in list_recursively(currentPath):
                pathsList.append(path)
    return pathsList


def list_file(directory):
    myPath = Path(directory)
    paths = myPath.iterdir()
    pathsList = []
    for currentPath in sorted(paths, key=lambda p: (p.is_dir(), p.name)):
        if currentPath.is_file():
            pathsList.append(currentPath)
    return pathsList


def command_len2(directory):
    for path in list_contents(directory):
        print(path)


def command_len3(command, directory):
    option = command[2]
    if option == '-r':
        for path in list_recursively(directory):
            print(path)
    elif option == '-f':
        for path in list_file(directory):
            print(path)
    else:
        print("Error! Invalid command!")


def list_matching_name(command, directory):
    name = command[3:]
    name = ' '.join(name)
    for currentPath in list_contents(directory):
        if currentPath == Path(directory)/name:
            if Path(currentPath).is_file():
                print(currentPath)


def list_extension(command, directory):
    extension = command[-1]
    for path in list_contents(directory):
        if pathlib.Path(path).suffix == ('.' + extension):
            print(path)
        else:
            return False


def recursion_options(command, directory):
    myPath = Path(directory)
    paths = myPath.iterdir()

    if command[3] == '-f':
        for path in sorted(paths, key=lambda p: (p.is_dir(), p.name)):
            if path.is_file():
                print(path)
            elif path.is_dir():
                for i in list_file(path):
                    print(i)

    elif command[3] == '-s':
        name = command[4:]
        name = ' '.join(name)
        for currentPath in list_recursively(directory):
            if name in str(currentPath):
                if Path(currentPath).is_file():
                    print(currentPath)
                else:
                    return False

    elif command[3] == '-e':
        extension = command[-1]
        for path in list_recursively(directory):
            if pathlib.Path(path).suffix == ('.' + extension):
                print(path)


def command_E(journal: str, command: list):
    if len(command) > 1:
        for i in command:
            if i == '-usr':
                index = command.index(i) + 1
                username = str(command[index]).replace("'", "")
                username = username.replace('"', '')
                if input_error_check(username, journal) is False:
                    print("ERROR")
                    return False

                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                PROFILE.username = username
                PROFILE.save_profile(str(journal))

            elif i == '-pwd':
                index = command.index(i) + 1
                password = str(command[index]).replace("'", "")
                password = password.replace('"', '')
                if input_error_check(password, journal) is False:
                    print("ERROR")
                    return False

                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                PROFILE.password = password
                PROFILE.save_profile(str(journal))

            elif i == '-bio':
                index = command.index(i) + 1
                bio = command[index:]
                bio = ' '.join(bio)
                bio = bio.replace("'", "")
                bio = bio.replace('"', '')
                if user_bio_error_check(bio, journal) is False:
                    print("ERROR")

                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                PROFILE.bio = bio
                PROFILE.save_profile(str(journal))

            elif i == '-addpost':
                index = command.index(i) + 1
                entry = command[index:]
                entry = ' '.join(entry)
                entry = entry.replace("'", "")
                entry = entry.replace('"', '')

                POST = post(entry=entry)
                POST.set_entry
                POST.get_entry
                POST.set_time
                POST.get_time
                POST.entry
                POST.timestamp

                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                PROFILE.add_post(POST)
                PROFILE.save_profile(str(journal))

            elif i == '-delpost':
                index = command.index(i) + 1
                ID = int(command[index]) - 1
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                PROFILE.get_posts
                PROFILE.del_post(ID)
                PROFILE.save_profile(str(journal))

            elif i == '-publish':
                ID = -1
                publish_from_file(journal, ID)

            elif i == 'Q':
                quit()

            else:
                continue

    elif len(command) == 1:
        print("ERROR")

    elif len(command) == 0:
        print("ERROR")

    else:
        print("ERROR")
        # exit()


def command_P(journal: str, command: list):
    if len(command) >= 1:
        for j in command:
            if j == '-usr':
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                print(f"Username: {PROFILE.username}")

            elif j == '-pwd':
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                print(f"Password: {PROFILE.password}")

            elif j == '-bio':
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                print(f"Bio: {PROFILE.bio}")

            elif j == '-posts':
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                count = len(PROFILE._posts)
                print("Posts:")
                for post in range(count):
                    print(f"Post {post+1}: {PROFILE._posts[post]["entry"]}")

            elif j == '-post':
                if len(command) == 1:
                    print("ERROR")
                    return False

                index = command.index(j) + 1
                ID = int(command[index]) - 1
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                post = PROFILE._posts[ID]
                print(f"Post{ID + 1}: {post["entry"]}")

            elif j == '-all':
                PROFILE = profile()
                PROFILE.load_profile(str(journal))
                # print("Here is all the contents in the profile: ")
                print(f"DSU Server: {PROFILE.dsuserver}")
                print(f"Username: {PROFILE.username}")
                print(f"Password: {PROFILE.password}")
                print(f"Bio: {PROFILE.bio}")
                print("Posts: ")
                count = len(PROFILE._posts)
                for post in range(count):
                    print(f"Post {post+1}: {PROFILE._posts[post]["entry"]}")

            elif j == '-publish':
                index = command.index(j) + 1
                ID = int(command[index]) - 1
                publish_from_file(journal, ID)

            elif j == 'Q':
                quit()

            else:
                continue

    elif len(command) == 0:
        print("ERROR")
        return False

    else:
        print("ERROR")
        return False
        # exit()


def command_O(journal: str):
    try:
        if str(journal).endswith('.dsu'):
            if Path(journal).exists():
                run.profile_loading(str(journal))
            else:
                raise profile.DsuFileError(Exception)
        else:
            if Path(journal).suffix == '':
                journal = str(journal) + '.dsu'
                if Path(journal).exists():
                    run.profile_loading(str(journal))
            else:
                raise profile.DsuFileError(Exception)
    except Exception:
        print("Error! DSU could not be found!")
    else:
        return journal


def new_file(command, directory):
    name = command[3:]
    name = " ".join(name)
    if command[2] == '-n':
        filePath = Path(directory)/name
        try:
            if str(filePath).endswith('.dsu'):
                if filePath in list_contents(directory):
                    run.profile_loading(str(filePath))
                else:
                    Path(filePath).touch()
                    print("New journal successfully created!")
                    run.data_collection(str(filePath))
            else:
                if Path(filePath).suffix != '':
                    Path(filePath).touch()
                else:
                    filePath = str(filePath) + '.dsu'
                    if Path(filePath).exists():
                        run.profile_loading(str(filePath))
                    else:
                        Path(filePath).touch()
                        print("New journal successfully created!")
                        run.data_collection(str(filePath))
        except Exception:
            print("Error occured when saving user data!")
        else:
            return filePath
    else:
        print("ERROR")


def delete_file(command):
    filePath = command[-1]
    if Path(filePath).suffix != ('.dsu'):
        print("ERROR")
    else:
        if Path(filePath).exists():
            Path(filePath).unlink()
            print(str(filePath) + " DELETED")
        else:
            print("ERROR")


def read_file(command):
    filePath = Path(command[-1])
    if filePath.suffix != ('.dsu'):
        print("ERROR")
    else:
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()
                if len(lines) == 0:
                    print("EMPTY")
                else:
                    for line in lines:
                        line = line.strip()
                        print(line)
        except FileNotFoundError:
            print("ERROR")


def admin_new_file(command, directory):
    name = command[3:]
    name = " ".join(name)
    if command[2] == '-n':
        filePath = Path(directory)/name
        try:
            if str(filePath).endswith('.dsu'):
                if filePath in list_contents(directory):
                    run.profile_loading(str(filePath))
                else:
                    Path(filePath).touch()
                    PROFILE = profile()
                    PROFILE.save_profile(str(filePath))
                    filePath = str(filePath)
            else:
                if Path(filePath).suffix != '':
                    Path(filePath).touch()
                else:
                    filePath = str(filePath) + '.dsu'
                    if Path(filePath).exists():
                        run.profile_loading(str(filePath))
                    else:
                        Path(filePath).touch()
                        PROFILE = profile()
                        PROFILE.save_profile(str(filePath))
                        filePath = str(filePath)
        except Exception:
            print("Error occured when saving user data!")
        else:
            return filePath
    else:
        print("ERROR")


def publish_from_file(journal, post_ID):
    PROFILE = profile()
    PROFILE.load_profile(str(journal))
    port = 3021
    server = str(PROFILE.dsuserver)
    username = str(PROFILE.username)
    password = str(PROFILE.password)
    bio = str(PROFILE.bio)
    message = str(PROFILE._posts[post_ID]['entry'])

    if send(server, port, username, password, message, bio):
        print("Operation completed successfully!")
        ## exit()
    else:
        print("Oops! Operation failed!")
        ## exit()


def main():
    run.ui_main()


if __name__ == "__main__":
    main()
