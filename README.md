# The Advanced Scientific Data Format Tutorial
## ADASS 2024
### Valletta, Malta

To run all the workshop notebooks on your own computer, be sure your machine is configured with the packages in
the
[installation check file](https://github.com/asdf-format/asdf-adass2024/blob/main/tutorial/install/verify_install.py). These packages
are the ones we use to verify that the notebooks are working as expected.

These instructions assume the installation is done on a *nix type of operating system and describe setup using `git` and `Miniconda`. It is not strictly necessary to use either of these.There are pointers for setting this up on Windows, however Windows is not fully supported.

## 1. Install Miniconda (if needed)

> *Miniconda is a free minimal installer for `conda`. It is a small, bootstrap version of Anaconda that includes
only `conda`, Python, the packages they depend on, and a small number of other useful packages like `pip`, `zlib` etc.
If you have already installed Miniconda or Anaconda, you can skip to the next step.*

In a terminal window, check if Miniconda is already installed:

```shell
conda info
```

If Miniconda is not already installed, follow these instructions for your operating system:

https://conda.io/projects/conda/en/latest/user-guide/install/index.html

> Please be sure to install a **64-bit version** of Miniconda to ensure that all packages work correctly.


## 2. Open the conda command prompt

> *Miniconda includes an environment manager called `conda`. An environment manager allows you to have multiple
installations of Python, including packages and versions, installed on your computer. You can create, export, list,
remove, and update environments that have different versions of Python and / or packages installed in them. For this
workshop, we will configure an environment using the `conda` command line utility.*

Open a terminal window and verify that conda is working:

```shell
conda info
```

If you are having trouble, check your shell in a terminal window:

```shell
echo $SHELL
```

then run the initialization, if needed, in that same terminal window:

```shell
conda init $SHELL
```

> *(An alternative to using conda is [mamba](https://github.com/mamba-org/mamba) which is a reimplementation of the
conda package manager in C++.)*

> Note: you will need `conda` version `4.6` or later. You can update your `conda` installation with `conda update conda`

## 3. Install Git (if needed)

At the prompt, check whether Git is already installed:

```shell
git --version
```

If the output shows a Git version, skip to the next step. Otherwise, install Git:

```shell
conda install git
```

## 4. Clone this repository, or download and extract a ZIP file, from GitHub

If using `git`, clone the workshop repository using
[git](https://help.github.com/articles/set-up-git/):

```shell
git clone https://github.com/asdf-format/asdf-adass2024.git
```

If you elect not to use `git`, you can download the ZIP file by opening the green `Code` button at
https://github.com/asdf-format/asdf-adass2024.git and selecting `Download ZIP`.

## 5. Create a `conda` environment for the workshop

> *Miniconda includes an environment manager called conda. Environments allow you to have multiple sets of Python
packages installed at the same time, making reproducibility and upgrades easier. You can create, export, list, remove,
and update environments that have different versions of Python and/or packages installed in them.*

[Create a conda environment for this workshop using a yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
. The python version and all needed packages are listed in
[`environment.yml`](https://github.com/asdf-format/asdf-adass2024/blob/main/tutorial/install/environment.yml).

Open a terminal window using the appropriate one for your operating system.

Now navigate to this directory in the terminal:

```shell
cd asdf-adass2024
```

And finally, on any platform, to install and activate the `roman-data-workshop-env` environment, type:

```shell
conda env create --file install/environment.yml
conda activate adass-asdf
```

The name of the new conda environment created above should now be displayed next to the terminal
prompt: `(adass-asdf)`

Now navigate to this directory in the terminal:

```shell
cd asdf-adass2024
```

If the package was installed with `pip`, the `Build` and `Channel` columns will include `pypi`:

```
# packages in environment at /opt/miniconda3/envs/test:
#
# Name                    Version                   Build  Channel
numpy                     1.22.4                   pypi_0    pypi
```

and then you can upgrade with `pip install --upgrade <package>`:

```shell
pip install --upgrade numpy
```

## 6. Download Data

Making sure to activate the `conda` environment (`conda activate adass-asdf`), run the following to
download the data files used by these notebooks:

```shell
python data/download.py
```

## 7. Starting Jupyter Notebook

Making sure your terminal is in the `roman-data-workshop` directory (you can use `pwd` to check), you can then start the
Jupyter server on your local computer, with which you can view the Jupyter notebooks:

```shell
jupyter notebook
```

If successful, your browser will open a new page / tab pointing to `localhost`, showing a listing of the current
directory (including subdirectories).

Click into one of the notebook directories, double-click on a notebook, and wait for it to launch. In the top right
corner, if you see a blue `Kernel Ready` message appear and disappear, then all is well.

If you see a red `Kernel Error` in the top right corner, click on it and scroll down to see the error message. If it
says `FileNotFoundError`, shut down the notebook server on your terminal and run this command:

```shell
python -m ipykernel install --user
```

Now, try running `jupyter notebook` again as above, and the `Kernel Error`
should be fixed. You can try running the first cell (usually an `import`) to check.
