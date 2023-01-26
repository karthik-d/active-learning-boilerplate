import os

config = dict(
    ROOT_PATH = os.path.abspath(os.path.join(os.path.split(__file__)[0], *((os.path.pardir,)*0)))
)

print("[INFO] Configurations set.")