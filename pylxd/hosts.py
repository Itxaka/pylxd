# Copyright (c) 2015 Canonical Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json

from . import connection

from . import utils


class LXDHost(object):
    def __init__(self):
        self.connection = connection.LXDConnection()

    def host_ping(self):
        try:
            return self.connection.get_status('GET', '/1.0')
        except Exception as e:
            msg = 'LXD service is unavailable. %s' % e
            raise Exception(msg)

    def host_info(self):
        (state, data) = self.connection.get_object('GET', '/1.0')

        return {
            'lxd_api_compat_level': self.get_lxd_api_compat(data.get('metadata')),
            'lxd_trusted_host': self.get_lxd_host_trust(data.get('metadata')),
            'lxd_backing_fs': self.get_lxd_backing_fs(data.get('metadata')),
            'lxd_driver': self.get_lxd_driver(data.get('metadata')),
            'lxc_version': self.get_lxc_version(data.get('metadata')),
            'kernel_version': self.get_kernel_version(data.get('metadata'))
        }

    def get_lxd_api_compat(self, data):
        try:
            if data is None:
                (state, data) = self.connection.get_object('GET', '/1.0')
                data = data.get('metadata')
            return data['api_compat']
        except Exception as e:
             print 'Handling run-time error:', e

    def get_lxd_host_trust(self, data):
        try:
            if data is None:
                (state, data) = self.connection.get_object('GET', '/1.0')
                data = data.get('metadata')
            return True if data['auth'] == 'trusted' else False
        except Exception as e:
            print 'Handling run-time error:', e

    def get_lxd_backing_fs(self, data):
        try:
            if data is None:
                (state, data) = self.connection.get_object('GET', '/1.0')
                data = data.get('metadata')
            return data['environment']['backing_fs']
        except Exception as e:
            print 'Handling run-time error:', e

    def get_lxd_driver(self, data):
        try:
            if data is None:
                (state, data) = self.connection.get_object('GET', '/1.0')
                data = data.get('metadata')
            return data['environment']['driver']
        except Exception as e:
            print 'Handling run-time error:', e

    def get_lxc_version(self, data):
        try:
            if data is None:
                (state, data) = self.connection.get_object('GET', '/1.0')
                data = data.get('metadata')
            return data['environment']['lxc_version']
        except Exception as e:
            print 'Handling run-time error:', e

    def get_kernel_version(self, data):
        try:
            if data is None:
                (state, data) = self.connection.get_object('GET', '/1.0')
                data = data.get('metadata')
            return data['environment']['kernel_version']
        except Exception as e:
            print 'Handling run-time error:', e


