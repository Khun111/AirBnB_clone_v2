#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

if __name__ == '__main__':
    def do_pack():
        try:
            local('mkdir versions')

            time = datetime.now().strftime('%Y%m%d%H%M%S')
            archive_name = f'web_static_{time}.tgz'
            local(f'tar -cvsf versions/{archive_name} web_static')
            if os.path.exists(f'versions/{archive_name}')
                return f'versions/{archive_name}'
            else:
                return None
        except:
                return None
