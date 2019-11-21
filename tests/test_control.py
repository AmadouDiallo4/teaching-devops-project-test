
"""Test Control machine"""

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
