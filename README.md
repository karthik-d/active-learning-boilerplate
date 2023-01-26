# Boilerplate-for-Active-Learning

Templated boilerplate to perform Active Learning.


## Clone the repository to your local environment

- Use the following command to create a local copy by executing,   
`git clone https://github.com/karthik-d/Boilerplate-for-Active-Learning`

- Use the option `--recurse-submodules` to set up *toupee* as a submodule here itself. This can, however, be done at a later stage.

## Install dependencies

### **(Recommended)** Using an Anaconda environment
- [Quick Reference](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
- **Either**, use `dependencies/dep-file-conda.yml` file to create an environment with all dependencies by running,   
`conda env create -f dep-file-conda.yml`   
The default environment name is **al_boilerplate**. Edit the .yml file to change it.

- **Or, for \*nix systems**, use `dependencies/dep-file-conda-nix.txt` file to create an environment by running,   
`conda create --name <env-name> --file dep-file-conda-nix.txt`  

- **Then**, switch to the created/modified environment by running   
`conda activate <env-name>`

### **(Not preferred)** Using pip
- Use `dpendencies/dep-file-pip.txt` file Install all dependencies by running,      
  `pip install -r dep-file-pip.txt`

#### Potential caveats
- The requirements file for `pip` was generated on a *nix system. Hence, it will install without hiccups only on this platform.
- For other platoforms, the task may simply decompose to a manual dep-by-dep install! In this case, refer to the versions of dependencies in the dependency files when installing them.
  
### **In either case**, Install other dependencies currently not packaged in conda
- Use the standard `pip install <lib-name>` syntax to install the following additional dependencies that are currently not available in any of the anaconda repositories,
  - [pyyaml-include](https://pypi.org/project/pyyaml-include/)
  
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
  `python toupee/bin/load_data.py mnist <destination-location>`
- This prepares the data in the [**NPZ**](https://imageio.readthedocs.io/en/v2.6.1/format_npz.html) format, into the destination directory.
- **Note**: The path to destination should preferrably be an **absolute path**, but it could also be **relative** to the current working context.
- **Note**: The `load_data.py` script file, of course, must be traced to its location appropriately, depending on the current working context.

## Run Model Tests
- Model tests are scripted in `tests/`
  - Each subdirectory is a test.
  - Each test contains three files: A tensorflow model defined as a *yml* configuration (**.model** extension); a training experiment configuration file (**.yml** extension); and a Python script to define evaluation metrics and the testing workflow (**.py** extension). 
- Use `run.py` in the root of the repository to run models; this is a wrapper for *toupee* model executors in `toupee/bin/`.
- Edit `run.py` to set the parameters to be defined for model training and choose the underlying *toupee* script to run; one additiona parameter - `root_dir` - is required, and is already configured to the repository root.
- To execute the script, after setting the parameters and calling the appropriate driver function, simply use,
  ```
  python run.py
  ```

## General Notes

- Use `python3` in place of `python` to execute Python scripts if you experience problems with Python version resolution between 2.x and 3.x.
- Prefer the use of *abolute* paths over *relative* ones. In the latter case, adjust the values relative to the current context.
- Prefeably, use `ROOT_DIR` defined in `config.py` to reference the root of the codebase and construct the path from thereon.


# Development Notes

## Major changes to `toupee` (*!Incomplete List*)
- Model definitions changed, in-pipeline, from YAML to JSON to adapt to newer versions of tensorflow and keras. No input-output changes.
- Environment dependencies and version changes fixed. Environment sandboxes included as dependency files for easy reproduction.
- File paths configured to be referenced from codebase root.
- Wrapper developed for training experiments to integrate toupee as a "submodule" of the working codebase.
