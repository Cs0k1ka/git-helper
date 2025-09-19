import os
import subprocess

# Helper to check if a folder is a Git repository
def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))

# Utility to get the repository path from the user
def get_repo_path():
    repo_location = input("Where is your repository located? (Press Enter for current folder) >> ").strip()
    if not repo_location:
        repo_location = "."

    # Handle absolute vs relative paths
    repo_path = repo_location if os.path.isabs(repo_location) else os.path.abspath(os.path.join(os.getcwd(), repo_location))
    
    print("DEBUG: Using repository path:", repo_path)

    if not os.path.isdir(repo_path):
        print("Error: folder not found!", repo_path)
        return None
    if not is_git_repo(repo_path):
        print("Error: folder is not a Git repository!", repo_path)
        return None

    return repo_path

# Commit changes to a repository
def commit_changes():
    repo_path = get_repo_path()
    if not repo_path:
        return

    file_selector = input("Which files to add? (e.g., script.js) or '.' for all >> ").strip()
    if not file_selector:
        file_selector = "."

    commit_comment = input("Commit message >> ").strip()
    if not commit_comment:
        print("Error: commit message cannot be empty.")
        return

    subprocess.run(["git", "add", file_selector], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", commit_comment], cwd=repo_path)
    subprocess.run(["git", "push"], cwd=repo_path)
    print("Commit and push completed.")

# Pull updates from a repository
def pull_repo():
    repo_path = get_repo_path()
    if not repo_path:
        return

    subprocess.run(["git", "pull"], cwd=repo_path)
    print("Pull completed.")

# Clone a repository
def clone_repo():
    url = input("Enter your repository URL >> ").strip()
    if not url:
        print("Error: repository URL cannot be empty.")
        return

    target_folder = input("Enter folder name to clone into (Press Enter for current folder) >> ").strip()
    target_folder = target_folder or "."

    clone_path = os.path.abspath(os.path.join(os.getcwd(), target_folder))
    if os.path.exists(clone_path):
        print(f"Error: folder '{clone_path}' already exists.")
        return

    subprocess.run(["git", "clone", url, clone_path])
    print(f"Repository cloned into: {clone_path}")

# Main menu of the app
def menu():
    while True:
        print("\n─── Git Helper Menu ───")
        print("1. Commit changes")
        print("2. Pull repository")
        print("3. Clone repository")
        print("4. Exit")

        choice = input("Choose an option >> ").strip()
        if choice == '1':
            commit_changes()
        elif choice == '2':
            pull_repo()
        elif choice == '3':
            clone_repo()
        elif choice == '4':
            exit()
        else:
            print("Error: invalid choice, try again.")

# Run the menu
if __name__ == "__main__":
    menu()
