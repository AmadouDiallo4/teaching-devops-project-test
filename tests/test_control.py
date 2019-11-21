
import os
import glob

"""Test Control machine"""

def test_rsa_files():
    """
    Verify that there is no dangling RSA key in Vagrant folder :-)
    """
    project_root = os.environ('PROJECT_ROOT')
    # find Vagrantfile directory
    vagrant_root = project_root
    rsa_files = (
        glob.glob(vagrant_root + '*_rsa') +
        glob.glob(vagrant_root + '*_rsa.pub')
    )
    assert not rsa_files

def test_readme_files():
    """
    Verify that there is a README.txt or README.md file
    """
    project_root = os.environ('PROJECT_ROOT')
    assert False

def test_yaml_syntax():
    """
    Verify syntax for ansible files with ansible-lint + yamllint
    """
    assert False

def test_resolution(host):
    """
    Verify that this host resolves hostnames for
    - s*.infra
    - dev*.com

    Verify that sites resolve to the same IP as s1.infra
    """
    servers = [
        's0.infra',
        's1.infra',
        's2.infra',
        's3.infra',
        's4.infra',
    ]
    sites = [
        'devops.com',
        'devsec.com',
        'devsecops.com'
    ]
    for target_name in servers:
        target = host.addr(target_name)
        assert target.is_resolvable

    lb = host.addr(servers[0])
    for target_name in sites:
        target = host.addr(target_name)
        assert target.is_resolvable
        assert target.ip_address.sort() == lb.ip_address.sort()
