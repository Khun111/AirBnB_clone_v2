#!/usr/bin/python3
'''Create and distribute archive'''
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['54.144.144.194', '100.25.140.47']


def do_pack():
    '''Fabric that generates a .tgz archive from the contents of web_static'''
    try:
        local('mkdir -p versions')

        time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = 'web_static_{}.tgz'.format(time)
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        if os.path.exists('versions/{}'.format(archive_name)):
            return 'versions/{}'.format(archive_name)
        else:
            return None
    except Exception as no:
        return None


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


def deploy():
    '''Function that creates and distributes archive_d'''
    my_archive = do_pack()
    return False if not my_archive else do_deploy(my_archive)
