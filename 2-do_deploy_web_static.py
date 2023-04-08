#!/usr/bin/python3
'''Module Fabric script that distributes an archive to your web server'''
import os
from fabric.api import env, sudo
from datetime import datetime
env.hosts = ['54.144.144.194', '100.25.140.47']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    '''Function to distribute to webservers'''
    if not os.path.exists(archive_path):
        return False
    try:
        archive_f = os.path.basename(archive_path)
        archive_d = os.path.splitext(archive_f)[0][:]
        put(archive_path, '/tmp/{}'.format(archive_f))
        run('sudo mkdir -p /data/web_static/releases/{}'.format(archive_d))
        run('sudo tar -xzf /tmp/{} -C /data/web_static\
/releases/{}'.format(archive_f, archive_d))
        run('sudo rm /tmp/{}'.format(archive_f))
        run('sudo mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}'.format(archive_d, archive_d))
        run('sudo rm -rf \
/data/web_static/releases/{}/web_static/'.format(archive_d))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{} \
/data/web_static/current'.format(archive_d))
        return True
    except Exception as e:
        return False
