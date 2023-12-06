#!/usr/bin/env python3
"""Fabric script to generate a .tgz archive from the contents of web_static"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of web_static"""
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Create the archive name with the specified format
        time_format = "%Y%m%d%H%M%S"
        archive_name = "web_static_{}.tgz".format(datetime.utcnow().strftime(time_format))

        # Compress the web_static folder and store in versions
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if successful
        return os.path.join("versions", archive_name)
    except Exception:
        return None
