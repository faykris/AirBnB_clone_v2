#!/usr/bin/python3
"""1. Compress before sending - module"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """do_pack - function"""

    try:
        local("mkdir -p versions")
        n_time = datetime.now()
        s_time = str(n_time.year).zfill(4) + str(n_time.month).zfill(2) +\
            str(n_time.day).zfill(2) + str(n_time.hour).zfill(2) +\
            str(n_time.minute).zfill(2) + str(n_time.second).zfill(2)
        tgz_path_file = "versions/web_static_{}.tgz".format(s_time)
        local("tar -czvf {} web_static".format(tgz_path_file))
        return tgz_path_file
    except:
        return None


def do_deploy(archive_path):
    """do_deploy - function"""
    try:
        local("stat {}".format(archive_path))
    except:
        return False
    return False
