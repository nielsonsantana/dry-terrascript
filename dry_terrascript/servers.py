
from terrascript.digitalocean.r import droplet

from .images import do_ubuntu_18_04_x64


class ServerInstance(object):
    server = None
    server_dict = None

    def __init__(self, server, server_dict):
        self.server = server
        self.server_dict = server_dict

    def get_ts_object(self):
        return self.server

    def get(self, key, default=''):
        return self.server_dict.get(key, default)

    @property
    def public_ip(self):
        if 'digitalocean' in str(self.server).lower():
            return self.server.ipv4_address
        return ''


def do_server(name, image=do_ubuntu_18_04_x64,
              size='s-1vcpu-1gb', **kwargs):
    """
    name - Droplet name
    image - Distro image name
    kwargs - Others named parametes

    """
    region = kwargs.get('region', 'nyc3')
    name_region = '{0}-{1}'.format(name, region)

    default_params = dict(
        name=name_region,
        image=image.slug, size=size,
        region='nyc3',
        monitoring=True,
        private_networking=True,
        resize_disk=False,
    )
    default_params.update(kwargs)

    do_droplet_production = droplet(
        name_region,
        **default_params
    )
    return ServerInstance(do_droplet_production, default_params)


def aws_server_lightsail(name, image=do_ubuntu_18_04_x64,
                         size='s-1vcpu-1gb', **kwargs):
    """
    name - Droplet name
    image - Distro image name
    kwargs - Others named parametes

    """
    region = kwargs.get('region', 'nyc3')
    name_region = '{0}-{1}'.format(name, region)

    default_params = dict(
        name=name_region,
        image=image.slug, size=size,
        region='nyc3',
        monitoring=True,
        private_networking=True,
        resize_disk=False,
    )
    default_params.update(kwargs)

    do_droplet_production = droplet(
        name_region,
        **default_params
    )
    return ServerInstance(do_droplet_production, default_params)


def aws_server_ec2(name, image=do_ubuntu_18_04_x64,
                   size='s-1vcpu-1gb', **kwargs):
    """
    name - Droplet name
    image - Distro image name
    kwargs - Others named parametes

    """
    region = kwargs.get('region', 'nyc3')
    name_region = '{0}-{1}'.format(name, region)

    default_params = dict(
        name=name_region,
        image=image.slug, size=size,
        region='nyc3',
        monitoring=True,
        private_networking=True,
        resize_disk=False,
    )
    default_params.update(kwargs)

    do_droplet_production = droplet(
        name_region,
        **default_params
    )
    return ServerInstance(do_droplet_production, default_params)
