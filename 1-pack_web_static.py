#!/usr/bin/python3
from fabric.api import local
from fabric.decorators import runs_once
from datetime import datetime
import os

@runs_once
def do_pack():
    try:
        local('mkdir -p versions')

        time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = 'web_static_{}.tgz'.format(time)
        local('tar -cvsf versions/{} web_static'.format(archive_name))
        if os.path.exists('versions/{}'.format(archive_name)):
            return 'versions/{}'.format(archive_name)
        else:
            return None
    except Exception as no:
            return None
