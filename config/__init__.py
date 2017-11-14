"""config"""
from . import development
from . import production

CONFIG_FILE = {
    'development': development.__file__,
    'production': production.__file__
}
