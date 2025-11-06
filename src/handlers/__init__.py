import torch
from pathlib import Path
from transformers.utils import logging as transformers_logging

transformers_logging.set_verbosity_error()

_orig_read_text = Path.read_text
def _read_text_utf8(self, encoding=None, errors=None):
    if encoding is None:
        encoding = 'utf-8'
    return _orig_read_text(self, encoding=encoding, errors=errors)
Path.read_text = _read_text_utf8

_original_torch_load = torch.load
def patched_torch_load(*args, **kwargs):
    if 'weights_only' not in kwargs or kwargs['weights_only'] != True:
        kwargs['weights_only'] = False
    return _original_torch_load(*args, **kwargs)
torch.load = patched_torch_load
