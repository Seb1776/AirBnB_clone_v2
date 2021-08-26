#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os.path


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
