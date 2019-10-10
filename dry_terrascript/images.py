from terrascript import Terrascript
from terrascript.aws.d import aws_ami
from terrascript.digitalocean.d import image

do_ubuntu_16_04_x64 = image('ubuntu-16-04', slug='ubuntu-16-04-x64')
do_ubuntu_18_04_x64 = image('ubuntu-18-04', slug='ubuntu-18-04-x64')


def get_aws_ec2_image(name='ubuntu-18-04-minimal',
                      aws_region_list=['us-east-1'], **kwargs):
    ts_local = Terrascript()

    filter_value = 'ubuntu-minimal/images/hvm-ssd/ubuntu-bionic-18.04-amd64-minimal-20190723*'
    filter_value = kwargs.pop('filter_value', '') or filter_value

    default_params = dict(
        owners=['099720109477'],
        most_recent=True,
        filter=[
            dict(
                name='name',
                values=[
                    filter_value
                ]
            ),
            dict(
                name='root-device-type',
                values=[
                    'ebs'
                ]
            )
        ]
    )
    default_params.update(kwargs)

    aws_ami_ubuntu_18_04_minimal_map = {}
    for region in aws_region_list:
        _provider = 'aws.{}'.format(region)
        _aws_ami = ts_local.add(aws_ami(
            '{0}-{1}'.format(name, region),
            provider=_provider,
            **default_params
        ))
        aws_ami_ubuntu_18_04_minimal_map[region] = _aws_ami

    return aws_ami_ubuntu_18_04_minimal_map, ts_local


def get_aws_ec2_ubuntu_image(name='ubuntu-18-04-minimal', **kwargs):
    get_aws_ec2_ubuntu_image(name=name, **kwargs)
