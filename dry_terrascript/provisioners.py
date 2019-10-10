

def secure_ubuntu_provisioner(connection, content=''):
    """
    Parameters connection, content, source

    Example of connection:
    connection = [dict(
        user='root',
        type='ssh',
        private_key='${file("key-path")}',
        timeout='60s',
        agent=False,
    )]
    """
    _provisioner = {
        'file': dict(
            source='/app/images/shell-scripts/create-base-user.sh',
            destination='/tmp/create-base-user.sh',
            connection=connection,
        ),
        'remote-exec': dict(
            inline=[
                'chmod +x /tmp/create-base-user.sh',
                'sh /tmp/create-base-user.sh',
            ],
            connection=connection,
        )
    }

    return _provisioner


__all__ = [
    'secure_ubuntu_provisioner',
]
