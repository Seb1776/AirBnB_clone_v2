#!/usr/bin/python3
from os import path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.75.52.228", "18.212.233.99"]


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
