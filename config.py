import os

config = dict(
    ROOT_PATH = os.path.join(os.path.abspath(__file__), *((os.path.pardir,)*1))
)

print("[INFO] Configurations set.")