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


class LXDProfile(object):
    def __init__(self):
        self.connection = connection.LXDConnection()

    def profile_list(self):
        (state, data) = self.connection.get_object('GET', '/1.0/profiles')
        return [profiles.split('/1.0/profiles/')[-1] for profiles in data['metadata']]

    def profile_create(self, profile):
        return self.connection.get_status('POST', '/1.0/profiles',
                                          json.dumps(profile))

    def profile_show(self, profile):
        return self.connection.get_object('GET', '/1.0/profile/%s'
                                          % profile)

    def profile_update(self, profile):
        return self.connection.get_status('PUT', '/1.0/profiles',
                                          json.dumps(profile))

    def profile_rename(self, profile):
        return self.connection.get_status('POST', '/1.0/profiles',
                                          json.dumps(profile))

    def profile_delete(self, profile):
        return self.connection.get_status('DELETE', '/1.0/profiles/%s'
                                          % profile)
