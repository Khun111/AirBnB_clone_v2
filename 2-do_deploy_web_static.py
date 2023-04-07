#!/usr/bin/python3
'''Module Fabric script that distributes an archive to your web server'''
import os
from fabric.api import *
from datetime import datetime
env.hosts = ['54.144.144.194', '100.25.140.47']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
def do_deploy(archive_path):
    '''Function to distribute to webservers'''
    if not os.path.exists(archive_path):
        return False
    try:
        archive_f = os.path.basename(archive_path)
        archive_d = os.path.splitext(archive_f)
        put(archive_path, '/tmp/{}'.format(archive_f))
        sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_f, archive_d))
        sudo('rm /tmp/{}'.format(archive_f))
        sudo('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(archive_d, archive_d))
        sudo('rm -rf /data/web_static/releases/{}/web_static/'.format(archive_d))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_d))
        return True
    except Exception as e:
        return False
