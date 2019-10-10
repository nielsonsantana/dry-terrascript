from terrascript import Terrascript
from terrascript.digitalocean.r import digitalocean_ssh_key


# DigitalOcean
def connection_gen(**kwargs):
    """DigitalOcean connection generator"""
    default_params = dict(
        user='root',
        type='ssh',
        private_key='${file("/tmp/ssh_keys/soar-staging-keypair")}',
        timeout='60s',
        agent=False,
    )
    default_params.update(kwargs)
    return default_params


def do_connection_gen(**kwargs):
    return connection_gen(**kwargs)


__all__ = [
    'do_connection_gen'
]
