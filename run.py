"""
Wrapper around `toupee` binaries to ease further development of native code,
and to simplify global configuration set up.
"""

import os

from config import config

# TODO: Switch to CLI args.
# TODO: Move CLI handling from base_model to here.
# TODO: Use level-logging.
# TODO: Parameter supply needs major fixing for non-required fields

## base_model.py configurations (SET HERE; "" to OMIT)

def run_base_model():
    root_path = config.get('ROOT_PATH')
    params_file = os.path.join(config.get('ROOT_PATH'), "tests", "mnist_test", "parameters.yml")   # REQUIRED
    save_file = ""
    num_epochs = "1" 
    tensorboard = ""
    adv_testing = ""
    wandb_store = ""
    wandb_project = ""
    wandb_group = ""

    # help text for arguments (reproduced, in part, from toupee)
    '''
    root_path: base path from where all relative paths will be referenced
    parser.add_argument('params_file', help='the parameters file')
    parser.add_argument('save_file', nargs='?',
                        help='the file where the trained MLP is to be saved')
    parser.add_argument('--epochs', type=int, nargs='?',
                        help='number of epochs to run')
    parser.add_argument('--tensorboard', action="store_true",
                        help="Save training graphs to TensorBoard")
    parser.add_argument('--adversarial-testing', action="store_true",
                        help="Test for adversarial robustness")
    parser.add_argument('--wandb', action="store_true",
                        help="Send results to Weights and Biases")
    parser.add_argument('--wandb-project', type=str, help="Weights and Biases project name")
    parser.add_argument('--wandb-group', type=str, help="Weights and Biases group name")
    '''

    print("[INFO] Parameter file: ", params_file)
    _cmd = 'python toupee/bin/base_model.py {root_path} {params} {save} {epochs} {tboard} {adv_testing} {wandb_store} {wandb_project} {wandb_group}'.format(
        root_path = root_path,
        params = params_file,
        save = save_file,
        epochs = num_epochs,
        tboard = tensorboard,
        adv_testing = adv_testing,
        wandb_store = wandb_store,
        wandb_project = wandb_project,
        wandb_group = wandb_group
    )
    print("[DEBUG]", _cmd)
    os.system(_cmd)


def run_ensemble_model():
    root_path = config.get('ROOT_PATH')
    params_file = os.path.join(config.get('ROOT_PATH'), "tests", "mnist_test", "parameters.yml")   # REQUIRED
    save_file = ""
    num_epochs = "1" 
    ensemble_size = ""
    tensorboard = ""
    adv_testing = ""
    wandb_store = ""
    wandb_project = ""
    wandb_group = ""
    distil = ""

    # help text for arguments (reproduced, in part, from toupee)
    '''
    root_path: base path from where all relative paths will be referenced
    parser.add_argument('params_file', help='the parameters file')
    parser.add_argument('save_file', nargs='?',
                        help='the file where the trained MLP is to be saved')
    parser.add_argument('--epochs', type=int, nargs='?',
                        help='Override number of epochs to run')
    parser.add_argument('--size', type=int, nargs='?',
                        help='Override Ensemble size')
    parser.add_argument('--adversarial-testing', action="store_true",
                        help="Test for adversarial robustness")
    parser.add_argument('--tensorboard', action="store_true",
                        help="Save training graphs to TensorBoard")
    parser.add_argument('--wandb', action="store_true",
                        help="Send results to Weights and Biases")
    parser.add_argument('--wandb-project', type=str, help="Weights and Biases project name")
    parser.add_argument('--wandb-group', type=str, help="Weights and Biases group name")
    parser.add_argument('--distil', action="store_true",
                        help="Create a distilled network from the Ensemble")
    '''

    print("[INFO] Parameter file: ", params_file)
    _cmd = 'python toupee/bin/ensemble.py {root_path} {params} {save} {epochs} {size} {tboard} {adv_testing} {wandb_store} {wandb_project} {wandb_group} {distil}'.format(
        root_path = root_path,
        params = params_file,
        save = save_file,
        epochs = num_epochs,
        size = ensemble_size,
        tboard = tensorboard,
        adv_testing = adv_testing,
        wandb_store = wandb_store,
        wandb_project = wandb_project,
        wandb_group = wandb_group,
        distil = distil
    )
    print("[DEBUG]", _cmd)
    os.system(_cmd)


if __name__=='__main__':
    # run_base_model()
    run_ensemble_model()