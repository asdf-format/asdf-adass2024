import os
import shutil
from pathlib import Path

from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/ExampleData/Build14"
remote_path = "r0000101001001001001_01101_0001_WFI01_cal.asdf"

LOCAL_DIRECTORY = Path(os.curdir)
local_path = LOCAL_DIRECTORY / Path(remote_path)



def download_data():
    filename = download_file(REMOTE_URL + remote_path)
    shutil.move(filename, local_path)


if __name__ == "__main__":
    download_data()
