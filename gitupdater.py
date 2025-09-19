import os
import subprocess

# Helper to check if a folder is a Git repository
def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))

# Main menu of the app
def menu():
    print('Menu')
    print('1. Commit changes')
    print('2. Pull repository')
    print('3. Clone repository')
    print('4. Exit')

    while True:
        choice = input("Choose an option to continue >> ")
        if not choice:
            print('Error, try again!')
        elif choice == '1':
            commit_changes()
        elif choice == '2':
            pull_repo()
        elif choice == '3':
            clone_repo()
        elif choice == '4':
            exit()
        else:
            print('Error, try again!')

# Commit changes to the desired repository
def commit_changes():
    repo_location = input("Where is your repository located? >> ")
    repo_path = os.path.abspath(os.path.join(os.getcwd(), "..", repo_location))

    if not os.path.isdir(repo_path):
        print("Error: folder not found!", repo_path)
        return
    if not is_git_repo(repo_path):
        print("Error: folder is not a Git repository!", repo_path)
        return

    file_selector = input("What files would you like to add? (e.g., script.js) or '.' for all >> ")
    commit_comment = input("What's your commit comment? >> ")

    subprocess.run(["git", "add", file_selector], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", commit_comment], cwd=repo_path)
    subprocess.run(["git", "push"], cwd=repo_path)
    print("Commit and push completed.")

# Pull the content of an updated repository
def pull_repo():
    repo_location = input("Where is your repository located? >> ")
    repo_path = os.path.abspath(os.path.join(os.getcwd(), "..", repo_location))

    if not os.path.isdir(repo_path):
        print("Error: folder not found!", repo_path)
        return
    if not is_git_repo(repo_path):
        print("Error: folder is not a Git repository!", repo_path)
        return

    subprocess.run(["git", "pull"], cwd=repo_path)
    print("Pull completed.")

# Clone a repository easily
def clone_repo():
    url = input("Enter your repository URL >> ")
    target_folder = input('Enter a folder name to clone into >> ')

    # Use the current working directory as default
    clone_path = os.path.abspath(os.path.join(os.getcwd(), target_folder))

    if os.path.exists(clone_path):
        print(f"Error: folder '{clone_path}' already exists.")
        return

    subprocess.run(["git", "clone", url, clone_path])
    print(f"Repository cloned into: {clone_path}")

# Run the menu
menu()
