
import sys
import pytest
import testinfra
import requests

# sys.path.append('.')
# from server import create_app # <<=== CHANGER CA / AJOUTER DES LIGNES

# HOSTS = [
#     's0.infra'
#     's1.infra'
#     's2.infra'
#     's3.infra'
#     's4.infra'
# ]
# 
# # scope='function' uses a new container per test function.
# @pytest.fixture(scope='session')
# def host(request):
#     """Yield machine names"""
#     for machine in HOSTS:
#         # return a testinfra connection to the container
#         yield testinfra.get_host("ssh://root@" + machine)
