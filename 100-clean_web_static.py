#!/usr/bin/python3
'''Module to delete outdated archives'''
from fabric.api import *
env.hosts = ['54.144.144.194', '100.25.140.47']


def do_clean(number=0):
    '''Function to delete outdated archives'''
    number = int(number) if int(number) != 0 else 1

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number + 1))
