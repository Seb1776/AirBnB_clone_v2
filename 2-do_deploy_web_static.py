#!/usr/bin/python3
from os import path
from fabric.api import env
from fabric.api import put
from fabric.api import hosts
from fabric.api import run
from fabric.api import local

env.hosts = ["34.75.52.228", "18.212.233.99"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not path.exists(archive_path):
        return False
    
    splitter = archive_path.split('/')[1]
    destination = "/data/web_static/releases/{}/".format(splitter.split('.')[0])

    try:
        print("Executing task 'do_deploy'")
        put(archive_path, "/tmp/")
        run('mkdir -p {}'.format(destination))
        run('tar -xzf /tmp/{} -C {}'.format(splitter, destination))
        run('rm /tmp/{}'.format(splitter))
        run('mv {}web_static/* {}'.format(destination, destination))
        run('rm -rf {}web_static'.format(destination))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(destination))
        print("New version deployed!")
        return True

    except:
        return False
