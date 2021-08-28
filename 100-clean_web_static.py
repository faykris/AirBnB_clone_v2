#!/usr/bin/python3
"""4. Keep it clean!"""

from subprocess import check_output
from os import path, system
from datetime import datetime
from fabric.api import local, env, put, run, sudo

env.hosts = ['ubuntu@34.138.47.45', 'ubuntu@35.237.57.6']


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
    if not path.exists(archive_path):
        return False
    try:
        ext_nam_file = archive_path.split("/")[1]
        nam_file = ext_nam_file.split(".")[0]
        put(archive_path, "/tmp/")
        tmp_ext_nam_file = "/tmp/{}".format(ext_nam_file)
        path_name_file = "/data/web_static/releases/{}/".format(nam_file)
        run("mkdir -p {}".format(path_name_file))
        run("tar -xzf {} -C {}".format(tmp_ext_nam_file, path_name_file))
        run("rm " + tmp_ext_nam_file)
        run("mv " + path_name_file + "web_static/* " + path_name_file)
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_name_file))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """deply - function"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """do_clean - function"""

    # remove tgz files from local storage
    l_files = check_output(
        "ls -ltr versions | grep web_static | cut -d ' ' -f 9", shell=True
    )
    i = 1
    lf_list = l_files.splitlines()
    for file in lf_list:
        if i != len(lf_list) and i <= len(lf_list) - int(number):
            local("rm -rf versions/{}".format(file.decode("utf-8")))
            i += 1

    # remove directories from remote storage
    r_files = run(
        "ls -ltr /data/web_static/releases | grep web_static | cut -d ' ' -f 9"
    )
    j = 1
    rf_list = r_files.splitlines()
    for file in rf_list:
        if j != len(rf_list) and j <= len(rf_list) - int(number):
            run("rm -rf /data/web_static/releases/{}".format(file))
            j += 1
