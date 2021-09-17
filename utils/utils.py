import os
from zipfile import ZipFile

ENV = "ENV"

STATIC_DIR = "../static"
ARTICLES_FILE = "../static/articles1-%s.csv"
ARTICLES_FILE_ZIP = "../static/articles1-%s.csv.zip"


def get_file_path(file_name):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)


def get_articles_file():
    env = "local" if not os.getenv(ENV) else os.getenv(ENV)
    static_dir = get_file_path(STATIC_DIR)
    file_zip = ARTICLES_FILE_ZIP % env
    unzip_file(get_file_path(file_zip), static_dir)
    file = ARTICLES_FILE % env
    return get_file_path(file)


def unzip_file(archive, path):
    with ZipFile(archive, "r") as zip_object:
        zip_object.extractall(path)
