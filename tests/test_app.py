# Utility

import requests

def apache_is_responding_for_vhost(host):
    """Test if apache is responding for given vhost"""
    response = requests.get("http://" + host)
    return response.status_code == 200

# Tests

def test_apache_is_installed(host):
    """Verify that apache is installed"""
    assert host.package("apache2").is_installed

# verify that PHP is installed
# verify that PHP version is 7

def test_apache_is_running(host):
    """Verify that apache has at least one running process"""
    apaches = host.process.filter(user="www-data", comm="apache2")
    assert apaches

def test_apache_is_listening_on_80(host):
    """Verify that apache is listening on port 80"""
    assert host.socket("tcp://80").is_listening

def test_apache_is_responding_for_all_vhosts(host):
    """Verify that apache if responding for requested vhosts"""
    vhosts = ['localhost', 'devops.com', 'devsecops.com']
    for vhost in vhosts:
        apache_is_responding_for_vhost(vhost)

# verify that nfs is mounted for on /mnt/nfs
# verify that apache allows directory /mnt/nfs

