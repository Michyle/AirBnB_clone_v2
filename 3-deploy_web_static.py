#!/usr/bin/python3
# a Fabfile to create and distribute an archive to the web server
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["34.207.63.120", "54.165.237.124"]

def do_pack():
    """this function creates a tar gzipped archive f the dictory web_static"""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

def do_deploy(archive_path):
    """This function distributes an archive to the webserver

    Args:
        archive_path (str): The path of the archive to distribute
    Returns:
        if file doesn't exit at archive_path or an error occurs - False.
        else - True
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split("."[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} - C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return False
    return True

def deploy():
    """Create and distribute an archive to a web server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
