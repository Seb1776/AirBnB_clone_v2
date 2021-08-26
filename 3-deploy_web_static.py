#!/usr/bin/python3
from fabric.api import env, local, put, run
from datetime import datetime
import os.path
from os import path
from os.path import exists, isdir

env.hosts = ["34.75.52.228", "18.212.233.99"]


def do_pack():
    """Generate .tgz file"""

    today = datetime.today()

    ftgz = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        today.year, today.month, today.day, today.hour, today.minute,
        today.second)

    if os.path.isdir("versions") is False:
        if local("sudo mkdir -p versions").failed is True:
            return None

    if local("tar -czvf {} web_static".format(ftgz)).failed is True:
        return None

    return ftgz


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file = archive_path.split('/')[-1]
        filedir = file.split('.')[0]
        pathf = "/data/web_static/releases/" + filedir
        run("mkdir -p " + pathf)
        run("tar -xzf /tmp/" + file + " -C " + pathf)
        run("rm /tmp/" + file)
        run("mv " + pathf + "/web_static/* " + pathf)
        run("rm -rf " + pathf + "/web_static/")
        run("rm -rf /data/web_static/current")
        run("ln -sf " + pathf + "/" + " /data/web_static/current")

        return True

    except:
        return False


def deploy():
    """Fabric script creates + distributes files to your web servers"""

    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
