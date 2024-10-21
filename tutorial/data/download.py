import os
import shutil
from pathlib import Path

from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/ADASS2024/"
remote_path = "jwst.asdf"

LOCAL_DIRECTORY = Path(os.curdir)
local_path = LOCAL_DIRECTORY / Path(remote_path)



def download_data():
    filename = download_file(REMOTE_URL + remote_path)
    shutil.move(filename, local_path)


if __name__ == "__main__":
    download_data()
