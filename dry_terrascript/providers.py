from terrascript import Terrascript

from terrascript import provider
from terrascript import variable
from terrascript.aws.d import aws_vpc

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

def ts_amazon_aws(version='=< 2.30', AWS_REGION_LIST=['us-east-1'], **kwargs):
    ts_local = Terrascript()

    aws_access_key = ts_local.add(variable('aws_access_key'))
    aws_secret_key = ts_local.add(variable('aws_secret_key'))
    aws_region = ts_local.add(variable('aws_region', default='us-east-1'))

    default_params = dict(
        version=version,
        access_key=aws_access_key,
        secret_key=aws_secret_key,
    )
    default_params.update(kwargs)

    # Providers
    aws_providers_map = {}
    for region in AWS_REGION_LIST:
        _provider = provider(
            'aws',
            region=region,
            alias=region,
            **default_params
        )
        aws_providers_map[region] = ts_local.add(_provider)

    ts_local.add(provider(
        'aws',
        region=aws_region,
        **default_params
    ))

    # VPC
    aws_vpc_map = {}
    for region in AWS_REGION_LIST:
        aws_provider = 'aws.{0}'.format(region)
        vpc_name = 'vpc-{}'.format(region)
        aws_vpc_map[region] = ts_local.add(aws_vpc(
            vpc_name, provider=aws_provider
        ))

    return ts_local


ts.update(ts_digitalocean())
ts.update(ts_cloudflare())
ts_providers = ts


__all__ = [
    'ts_cloudflare', 'ts_digitalocean', 'ts_providers'
]
