# Boilerplate-for-Active-Learning

Templated boilerplate to perform active learning.


## Clone the repository to your local environment

- Use the following command to create a local copy by executing,   
`git clone https://github.com/karthik-d/Boilerplate-for-Active-Learning`

- Use the option `--recurse-submodules` to set up *toupee* as a submodule here itself. This can, however, be done at a later stage.

## Install dependencies

### **(Recommended)** Using an Anaconda environment
- Use `dep-file-conda.yml` file to create an environment with all dependencies by running,   
`conda env create -f dep-file-conda.yml`

- **Then**, switch to the created/modified environment by running   
`conda activate <env-name>`

### **(Not preferred)** Using pip
- Use `dep-file-pip.txt` file Install all dependencies by running,      
  `pip install -r dep-file-pip.txt`
  
### Setup `toupee` as a submodule
- If you did not use `--recurse-submodules` while cloning the repository, set up *toupee* now.
- Run the following commands to do so,
  ```
  git submodule init     
  git submodule update   
  ```
  to detect the submodule, and to fetch and set it up, respectively.

## Download data
- Use **toupee**'s setup to install the dataset.
- For `tests/mnist_test`, get the MNIST dataset into `data/mnist` by running,   
  `python bin/load_data.py mnist <destination-location>`
- **Note**: The path to destination should preferrably be an **absolute path**, but it could also be **relative** to the current working context.


## General Notes

- Use `python3` in place of `python` to execute Python scripts if you experience problems with Python version resolution between 2.x and 3.x.
