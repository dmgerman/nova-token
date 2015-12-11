begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
nl|'\n'
comment|'# This package got introduced during the Mitaka cycle in 2015 to'
nl|'\n'
comment|'# have a central place where the config options of Nova can be maintained.'
nl|'\n'
comment|'# For more background see the blueprint "centralize-config-options"'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
comment|'# from nova.conf import api'
nl|'\n'
comment|'# from nova.conf import api_database'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'availability_zone'
newline|'\n'
comment|'# from nova.conf import aws'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'barbican'
newline|'\n'
comment|'# from nova.conf import base'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'cells'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'cert'
newline|'\n'
comment|'# from nova.conf import cinder'
nl|'\n'
comment|'# from nova.conf import cloudpipe'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'conductor'
newline|'\n'
comment|'# from nova.conf import configdrive'
nl|'\n'
comment|'# from nova.conf import console'
nl|'\n'
comment|'# from nova.conf import cors'
nl|'\n'
comment|'# from nova.conf import cors.subdomain'
nl|'\n'
comment|'# from nova.conf import crypto'
nl|'\n'
comment|'# from nova.conf import database'
nl|'\n'
comment|'# from nova.conf import disk'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'ephemeral_storage'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'floating_ips'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'glance'
newline|'\n'
comment|'# from nova.conf import guestfs'
nl|'\n'
comment|'# from nova.conf import host'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'hyperv'
newline|'\n'
comment|'# from nova.conf import image'
nl|'\n'
comment|'# from nova.conf import imagecache'
nl|'\n'
comment|'# from nova.conf import image_file_url'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'ironic'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'keymgr'
newline|'\n'
comment|'# from nova.conf import keystone_authtoken'
nl|'\n'
comment|'# from nova.conf import libvirt'
nl|'\n'
comment|'# from nova.conf import matchmaker_redis'
nl|'\n'
comment|'# from nova.conf import metadata'
nl|'\n'
comment|'# from nova.conf import metrics'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'network'
newline|'\n'
comment|'# from nova.conf import neutron'
nl|'\n'
comment|'# from nova.conf import notification'
nl|'\n'
comment|'# from nova.conf import osapi_v21'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'pci'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'rdp'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'remote_debug'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'scheduler'
newline|'\n'
comment|'# from nova.conf import security'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'serial_console'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'service'
newline|'\n'
comment|'# from nova.conf import spice'
nl|'\n'
comment|'# from nova.conf import ssl'
nl|'\n'
comment|'# from nova.conf import trusted_computing'
nl|'\n'
comment|'# from nova.conf import upgrade_levels'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'virt'
newline|'\n'
comment|'# from nova.conf import vmware'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'vnc'
newline|'\n'
comment|'# from nova.conf import volume'
nl|'\n'
comment|'# from nova.conf import workarounds'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'xenserver'
newline|'\n'
comment|'# from nova.conf import xvp'
nl|'\n'
comment|'# from nova.conf import zookeeper'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
comment|'# api.register_opts(CONF)'
nl|'\n'
comment|'# api_database.register_opts(CONF)'
nl|'\n'
name|'availability_zone'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# aws.register_opts(CONF)'
nl|'\n'
name|'barbican'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# base.register_opts(CONF)'
nl|'\n'
name|'cells'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# cinder.register_opts(CONF)'
nl|'\n'
comment|'# cloudpipe.register_opts(CONF)'
nl|'\n'
name|'compute'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'conductor'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# configdrive.register_opts(CONF)'
nl|'\n'
comment|'# console.register_opts(CONF)'
nl|'\n'
comment|'# cors.register_opts(CONF)'
nl|'\n'
comment|'# cors.subdomain.register_opts(CONF)'
nl|'\n'
comment|'# crypto.register_opts(CONF)'
nl|'\n'
comment|'# database.register_opts(CONF)'
nl|'\n'
comment|'# disk.register_opts(CONF)'
nl|'\n'
name|'ephemeral_storage'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'floating_ips'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'glance'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# guestfs.register_opts(CONF)'
nl|'\n'
comment|'# host.register_opts(CONF)'
nl|'\n'
name|'hyperv'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# image.register_opts(CONF)'
nl|'\n'
comment|'# imagecache.register_opts(CONF)'
nl|'\n'
comment|'# image_file_url.register_opts(CONF)'
nl|'\n'
name|'ironic'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'keymgr'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# keystone_authtoken.register_opts(CONF)'
nl|'\n'
comment|'# libvirt.register_opts(CONF)'
nl|'\n'
comment|'# matchmaker_redis.register_opts(CONF)'
nl|'\n'
comment|'# metadata.register_opts(CONF)'
nl|'\n'
comment|'# metrics.register_opts(CONF)'
nl|'\n'
name|'network'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# neutron.register_opts(CONF)'
nl|'\n'
comment|'# notification.register_opts(CONF)'
nl|'\n'
comment|'# osapi_v21.register_opts(CONF)'
nl|'\n'
name|'pci'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'rdp'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'scheduler'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# security.register_opts(CONF)'
nl|'\n'
name|'serial_console'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# spice.register_opts(CONF)'
nl|'\n'
comment|'# ssl.register_opts(CONF)'
nl|'\n'
comment|'# trusted_computing.register_opts(CONF)'
nl|'\n'
comment|'# upgrade_levels.register_opts(CONF)'
nl|'\n'
name|'virt'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# vmware.register_opts(CONF)'
nl|'\n'
name|'vnc'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# volume.register_opts(CONF)'
nl|'\n'
comment|'# workarounds.register_opts(CONF)'
nl|'\n'
name|'wsgi'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'xenserver'
op|'.'
name|'register_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# xvp.register_opts(CONF)'
nl|'\n'
comment|'# zookeeper.register_opts(CONF)'
nl|'\n'
nl|'\n'
name|'remote_debug'
op|'.'
name|'register_cli_opts'
op|'('
name|'CONF'
op|')'
newline|'\n'
endmarker|''
end_unit
