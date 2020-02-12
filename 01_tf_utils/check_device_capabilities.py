import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.python.client import device_lib

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

version = tf.__version__
executing_eagerly = tf.executing_eagerly()
hub_version = hub.__version__
available = tf.config.experimental.list_physical_devices("GPU")

print("Version: ", version)
print("Eager mode: ", executing_eagerly)
print("Hub Version: ", hub_version)
print("GPU is", "available" if available else "NOT AVAILABLE")
if available:
    print(get_available_gpus())