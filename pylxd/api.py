
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


from . import container
from . import certificate
from . import hosts
from . import image
from . import network
from . import operation
from . import profiles

class API(object):
    def __init__(self):
        self.hosts = hosts.LXDHost()
        self.image = image.LXDImage()
        self.alias = image.LXDAlias()
        self.network = network.LXDNetwork()
        self.operation = operation.LXDOperation()
        self.profiles = profiles.LXDProfile()
        self.certificate = certificate.LXDCertificate()
        self.container = container.LXDContainer()

    # host
    def host_ping(self):
        return self.hosts.host_ping()

    def host_info(self):
        return self.hosts.host_info()

    def get_lxd_api_compat(self, data=None):
        return self.hosts.get_lxd_api_compat(data)

    def get_lxd_host_trust(self, data=None):
        return self.hosts.get_lxd_host_trust(data)

    def get_lxd_backing_fs(self, data=None):
        return self.hosts.get_lxd_backing_fs(data)

    def get_lxd_driver(self, data=None):
        return self.hosts.get_lxd_driver(data)

    def get_lxc_version(self, data=None):
        return self.get_lxc_version(data)

    def get_kernel_version(self, data=None):
        return self.get_kernel_version(data)

    # images
    def image_list(self):
        return self.image.image_list()

    def image_search(self, params):
        return self.image.image_list_by_key(params)

    def image_info(self, image):
        return self.image.image_info(image)

    def image_upload_date(self, image, data=None):
        return self.image.get_image_date(image, data, 'uploaded_at')

    def image_create_date(self, image, data=None):
        return self.image.get_image_date(image, data, 'created_at')

    def image_expire_date(self, image, data=None):
        return self.image.get_image_date(image, data, 'expires_at')

    def image_upload(self, path, filename):
        return self.image.image_upload(path, filename)

    def image_delete(self, image):
        return self.image.image_delete(image)

    def image_export(self, image):
        return self.image.image_export(image)

    def image_update(self, image):
        return self.image.image_update(image)

    def image_rename(self, image):
        return self.image.image_rename(image)

    # alias
    def alias_list(self):
        return self.alias.alias_list()

    def alias_create(self, alias):
        return self.alias.alias_create(alias)

    def alias_update(self, alias):
        return self.alias.alias_update(alias)

    def alias_show(self, alias):
        return self.alias.alias_show(alias)

    def alias_rename(self, alias):
        return self.alias.alias_rename(alias)

    def alias_delete(self, alias):
        return self.alias.alias_delete(alias)

    # containers:
    def container_list(self):
        return self.container.container_list()

    def container_defined(self, container):
        return self.container.container_defined(container)

    def container_init(self, container):
        return self.container.container_init(container)

    def container_state(self, container):
        return self.container.container_state(container)

    def container_start(self, container):
        return self.container.container_start(container)

    def container_stop(self, container):
        return self.container.container_stop(container)

    def container_suspend(self, container):
        return self.container.container_suspend(container)

    def container_resume(self, container):
        return self.container.container_resume(container)

    def container_reboot(self, container):
        return self.container.container_reboot(container)

    def container_destroy(self, container):
        return self.container.container_destroy(container)

    def get_container_log(self, container):
        return self.container.get_container_log(container)

    # file operations
    def get_container_file(self, container, filename):
        return self.container.get_container_file(container, filename)

    def put_container_file(self):
        raise NotImplemented()

    # snapshots
    def container_snapshot_list(self):
        raise NotImplemented()

    def container_snapshot_create(self):
        raise NotImplemented()

    def container_snapshot_info(self):
        raise NotImplemented()

    def container_snaphsot_delete(self):
        raise NotImplemented()

    # misc container
    def container_run_command(self):
        raise NotImplemented()

    # certificates
    def certificate_list(self):
        return self.certificate.certificate_list()

    def certificate_show(self, fingerprint):
        return self.certificate.certificate_show(fingerprint)

    def certificate_delete(self, fingerprint):
        return self.certificate.certificate_delete(fingerprint)

    def certificate_create(self, fingerprint):
        return self.certificate.certificate_create(fingerprint)

    # profiles
    def profile_create(self, profile):
        return self.profiles.profile_create(profile)

    def profile_show(self, profile):
        return self.profiles.profile_show(profile)

    def profile_list(self):
        return self.profiles.profile_list()

    def profile_update(self, profile):
        return self.profiles.profile_update(profile)

    def profile_rename(self, profile):
        return self.profiles.profile_rename(profile)

    def profile_delete(self, profile):
        return self.profiles.profile_delete(profile)

    # lxd operations
    def list_operations(self):
        return self.operation.operation_list()

    def wait_container_operatoin(self, operation, status_code, timeout):
        return self.operation.operation_wait(operation, status_code, timeout)

    def operation_delete(self, operation):
        return self.operation.operation_delete(operation)

    def operation_info(self, operation):
        return self.operation.operation_show(operation)

    def operation_show_create_time(self, operation, data=None):
        return self.operation.operation_create_time(operation, data)

    def operation_show_update_time(self, operation, data=None):
        return self.operation.operation_update_time(operation, data)

    def operation_show_status(self, operation, data=None):
        return self.operation.operation_status_code(operation, data)

    # networks
    def network_list(self):
        return self.network.network_list()

    def network_show(self, network):
        return self.network.network_show(network)

    def network_show_name(self, network, data=None):
        return self.network.show_network_name(network, data)

    def network_show_type(self, network, data=None):
        return self.network.show_network_type(network, data)

    def network_show_members(self, network, data=None):
        return self.network.show_network_members(network, data)
