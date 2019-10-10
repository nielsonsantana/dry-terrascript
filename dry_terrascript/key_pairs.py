from terrascript import Terrascript
from terrascript.digitalocean.r import digitalocean_ssh_key


ts = Terrascript()


def do_ssh_key(name, **kwargs):
    """
    Example of public_key:
        public_key='${file("/tmp/ssh_keys/soar-staging-keypair.pub")}'
    """

    default_params = dict(
        name=name
    )
    default_params.update(kwargs)
    return digitalocean_ssh_key(
        name,
        **default_params
    )


ts_key_pairs = ts

__all__ = [
    'ts_key_pairs', 'do_ssh_key'
]
