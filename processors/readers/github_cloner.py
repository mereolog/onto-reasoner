import os

from git import Repo

from processors.readers.helpers.folder_creator import create_folder_if_not_exists


def clone_repo(repo_github_url: str, clone_folder: str):
    clone_folder_path = os.path.join('inputs/', clone_folder)
    create_folder_if_not_exists(folder_path=clone_folder_path)
    git_repo = Repo.clone_from(url=repo_github_url, to_path=clone_folder_path)