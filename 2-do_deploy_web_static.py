#!/usr/bin/env python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run, sudo
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', 'IP web-02']
env.user = '<your_ssh_username>'
env.key_filename = '<path_to_your_ssh_private_key>'

def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/<archive_filename>
        archive_filename = archive_path.split("/")[-1]
        release_path = '/data/web_static/releases/{}'.format(archive_filename[:-4])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        run('rm -f {}'.format(current_link))

        # Create a new symbolic link /data/web_static/current
        run('ln -s {} {}'.format(release_path, current_link))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(str(e)))
        return False

if __name__ == "__main__":
    archive_path = "path/to/your/archive.tgz"  # Replace with the actual path to your archive
    do_deploy(archive_path)
