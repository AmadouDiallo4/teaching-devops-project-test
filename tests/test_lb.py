
# verify that ansible is NOT installed here

def test_dnsmasq_is_installed(host):
    """Verify that dnsmasq is installed"""
    assert host.package("dnsmasq").is_installed

# VERIFY that dnsmasq does not provide a gateway
# VERIFY that dnsmasq host has a static IP adress
# VERIFY that dnsmasq uses 1.1.1.1 for dns relay

# For other hosts
# VERIFY that dnsmasq provides a dynamic IP adress to this host
# Verify that current host resolv.conf uses s0.infra (somewhere in 192.168.50.x/24) for DNS requests

def test_haproxy_is_installed(host):
    """Verify that haproxy is installed"""
    assert host.package("haproxy").is_installed

# Verify that haproxy backend include s1.infra & s2.infra

