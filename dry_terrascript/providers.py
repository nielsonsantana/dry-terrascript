from terrascript import Terrascript

from terrascript import provider
from terrascript import variable

ts = Terrascript()

#########################################
# DigitalOcean


def ts_digitalocean(version='>= 1.7, < 1.9', **kwargs):
    ts_local = Terrascript()

    do_token = ts_local.add(variable('do_token'))

    default_parms = dict(token=do_token)
    default_parms.update(kwargs)

    ts_local.add(provider(
        'digitalocean',
        version=version,
        **default_parms
    ))

    return ts_local


#########################################
# Cloudflare

def ts_cloudflare(version='< 1.9.0', **kwargs):
    ts_local = Terrascript()

    cloudflare_email = ts_local.add(variable('cloudflare_email'))
    cloudflare_token = ts_local.add(variable('cloudflare_token', default=''))

    default_parms = dict(
        email=cloudflare_email,
        token=cloudflare_token,
    )
    default_parms.update(kwargs)

    ts_local.add(provider(
        'cloudflare',
        version=version,
        **default_parms
    ))
    return ts_local


#########################################
# Amazon Aws

def ts_AmazonAWS(version='< 1.9.0', **kwargs):
    pass


ts.update(ts_digitalocean())
ts.update(ts_cloudflare())
ts_providers = ts


__all__ = [
    'ts_cloudflare', 'ts_digitalocean', 'ts_providers'
]
