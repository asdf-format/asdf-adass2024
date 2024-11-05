import os
import shutil
from pathlib import Path

from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/ADASS2024/"
REMOTE_PATHS = [
    "jwst.asdf",
    "grism.asdf",
    "catalog.asdf"]

LOCAL_DIRECTORY = Path("./data")


def download_data():
    for remote_path in REMOTE_PATHS:
        filename = download_file(REMOTE_URL + remote_path)
        local_path = LOCAL_DIRECTORY / Path(remote_path)
        shutil.move(filename, local_path)


if __name__ == "__main__":
    download_data()
