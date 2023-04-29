#!/usr/bin/python3
"""
This Fabric script distributes an archive to web servers
"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ["34.232.70.146", "54.160.120.62"]
env.user = "ubuntu"


def do_pack():
    """
    Compresses the web_static folder into a timestamped archive.

    Usage:
        'fab do_pack' command.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
    Deploys web_static to the remote servers.

    Usage:
        'fab do_deploy:/path/to/archive' command,
        where '/path/to/archive' is the path to the archive file.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        # Delete the archive from the web server
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on the web server
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
