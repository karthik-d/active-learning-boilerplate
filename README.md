# Boilerplate-for-Active-Learning

Templated boilerplate to perform Active Learning. Uses a fork of [toupee](https://github.com/nitbix/toupee) as a submodule with custom modifications for this particular boilerplate implementation. Fixes compatability issues with `tensorflow >= 2.2`.


## Clone the repository to your local environment

- Use the following command to create a local copy,   
```
git clone https://github.com/karthik-d/Boilerplate-for-Active-Learning
```

- Use the `--recurse-submodules` option to set up the [*toupee* fork](https://github.com/karthik-d/toupee-refbase) as a submodule here itself. This can, however, be done at a later stage.

## Install dependencies

### **(Recommended)** Using an Anaconda environment
- [Quick reference](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) on the basics of conda environments.
- **Either**, use [`dependencies/dep-file-conda.yml`](./dependencies/dep-file-conda.yml) file to create an environment with all dependencies by running,   
```
conda env create -f dep-file-conda.yml
```   
The default environment name is **al_boilerplate**. Edit the *.yml* file to change it.

- **Or, for \*nix systems**, use [`dependencies/dep-file-conda-nix.txt`](./dependencies/dep-file-conda-nix.txt) file to create an environment by running,   
```
conda create --name <env-name> --file dep-file-conda-nix.txt
```  

- **Then**, switch to the created/modified environment by running   
```
conda activate <env-name>
```

### **(Not preferred)** Using pip
- Use [`dependencies/dep-file-pip.txt`](./dependencies/dep-file-pip.txt) file to install all dependencies by running,      
  ```
  pip install -r dep-file-pip.txt
  ```

#### Potential caveats
- The requirements file for `pip` was generated on a *nix system. Hence, it will likely install without hiccups only on this platform.
- For other platforms, the task may simply decompose to a manual dep-by-dep install! In this case, refer to the versions of dependencies in the dependency files when installing them.
  
### **In either case**, install other dependencies currently not packaged in *conda*
- Use the standard `pip install <lib-name>` syntax to install the following additional dependencies that are currently not available in any of the anaconda repositories,
  - [pyyaml-include](https://pypi.org/project/pyyaml-include/)
- **Note**: Newer versions of *conda* may have already completed this for you.
  
### Setup [**toupee**](https://github.com/nitbix/toupee) as a submodule
- If you did not use `--recurse-submodules` when cloning this repository, set up the [*toupee* fork](https://github.com/karthik-d/toupee-refbase) now.
- Run the following commands to do so,
  ```
  git submodule init     
  git submodule update   
  ```
  to detect the submodule, and to fetch and set it up, respectively.

## Download data
- Use [**toupee**](https://github.com/nitbix/toupee)'s setup to install the dataset.
- For [`tests/mnist_test`](./tests/mnist_test), get the MNIST dataset into `data/mnist` by running,   
  `python toupee/bin/load_data.py mnist <destination-location>`
- This prepares the data in the [**NPZ**](https://imageio.readthedocs.io/en/v2.6.1/format_npz.html) format, into the destination directory.
- **Please note that**,
  - The path to destination should preferrably be an **absolute path**, but it could also be **relative** to the current working context.
  - The `bin/load_data.py` script file, of course, must be traced to its location appropriately, depending on the current working context.

## Run Model Tests
- Model test-cases are scripted in [`tests/`](./tests)
  - Each subdirectory is a test-case.
  - Each test-case contains three files: a tensorflow model defined as a *yml* configuration (with **.model** extension); a training experiment configuration file (with **.yml** extension); and a Python script to define evaluation metrics and the testing workflow (with **.py** extension). 
- Use [`run.py`](./run.py) in the root of the repository to run models; this is a wrapper for *toupee*'s model executors in `toupee/bin`.
- Edit [`run.py`](./run.py) to,
  - set the parameters for model training; only two parameters are **required**, and the rest are optional: `root_path` which is already configured to the repository root, and `params_file` which must point to the **.yml** defintion file in the test-case directory.
  - choose the underlying *toupee* script to run, by calling the appropriate `run_*` function in `__main__`. 
    - `run_base_model()` is a wrapper for *toupee*'s `bin/base_model.py`.
    - `run_ensemble_model()` is a wrapper for *toupee*'s `bin/ensemble.py`.
- To execute the script, after setting the parameters and calling the appropriate driver function, simply use,
  ```
  python run.py
  ```
  
### Expected Outputs

Should the driver run without any errors, the following outputs can be expected for training and subsequently evaluating the test workflows.

- [Link to sample outpusts for `mnist_test`](./docs/outputs_mnist-test)
- [Link to sample outputs for `cifar10_dib_test`](./docs/outputs_cifar10_dib_test)

## General Notes

- Use `python3` in place of `python` to execute Python scripts if you experience problems with Python version resolution between 2.x and 3.x.
- Prefer the use of **abolute** paths over **relative** ones. In the latter case, adjust the path relative to the current context.
- Preferably, use `ROOT_DIR` defined in [`config.py`](./config.py) to reference the root of the codebase and construct the path from thereon.
- If you need to make changes to the [*toupee* fork](https://github.com/karthik-d/toupee-refbase),
  - Be sure to do them on the [`dev-main`](https://github.com/karthik-d/toupee-refbase/tree/dev-main) branch, and send a pull request to its [`master`](https://github.com/karthik-d/toupee-refbase/tree/master) to verify. This will require an approval.
  - Note, however, that the changes made on [`dev-main`](https://github.com/karthik-d/toupee-refbase/tree/dev-main) will be immediately mapped to the boilerplate, and you can start using it right away.


# Development Notes

## Key changes made in [toupee](https://github.com/nitbix/toupee) (*!Incomplete List*)
- Model definitions changed, in-pipeline, from YAML to JSON to adapt to newer versions of *tensorflow* and *keras*. No input/output changes.
- Environment dependencies and version-related issues fixed. Sandboxed and included as dependency files for easy reproduction.
- File paths configured to be referenced from codebase root.
- Wrapper developed for training experiments to integrate a fork of toupee as a **submodule** of the working codebase.
