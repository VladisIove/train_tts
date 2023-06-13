import torch

loaded_options = None

def checkpoint(fn, *args):
    if loaded_options is None:
        enabled = False
    else:
        enabled = loaded_options['checkpointing_enabled'] if 'checkpointing_enabled' in loaded_options.keys() else True
    if enabled:
        return torch.utils.checkpoint.checkpoint(fn, *args)
    else:
        return fn(*args)