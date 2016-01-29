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
comment|'# from nova.conf import availability_zone'
nl|'\n'
comment|'# from nova.conf import aws'
nl|'\n'
comment|'# from nova.conf import barbican'
nl|'\n'
comment|'# from nova.conf import base'
nl|'\n'
comment|'# from nova.conf import cells'
nl|'\n'
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
comment|'# from nova.conf import floating_ip'
nl|'\n'
comment|'# from nova.conf import glance'
nl|'\n'
comment|'# from nova.conf import guestfs'
nl|'\n'
comment|'# from nova.conf import host'
nl|'\n'
comment|'# from nova.conf import hyperv'
nl|'\n'
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
comment|'# from nova.conf import keymgr'
nl|'\n'
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
comment|'# from nova.conf import network'
nl|'\n'
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
comment|'# from nova.conf import rdp'
nl|'\n'
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
comment|'# from nova.conf import vnc'
nl|'\n'
comment|'# from nova.conf import volume'
nl|'\n'
comment|'# from nova.conf import workarounds'
nl|'\n'
comment|'# from nova.conf import wsgi'
nl|'\n'
comment|'# from nova.conf import xenserver'
nl|'\n'
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
comment|'# availability_zone.register_opts(CONF)'
nl|'\n'
comment|'# aws.register_opts(CONF)'
nl|'\n'
comment|'# barbican.register_opts(CONF)'
nl|'\n'
comment|'# base.register_opts(CONF)'
nl|'\n'
comment|'# cells.register_opts(CONF)'
nl|'\n'
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
comment|'# floating_ip.register_opts(CONF)'
nl|'\n'
comment|'# glance.register_opts(CONF)'
nl|'\n'
comment|'# guestfs.register_opts(CONF)'
nl|'\n'
comment|'# host.register_opts(CONF)'
nl|'\n'
comment|'# hyperv.register_opts(CONF)'
nl|'\n'
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
comment|'# keymgr.register_opts(CONF)'
nl|'\n'
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
comment|'# network.register_opts(CONF)'
nl|'\n'
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
comment|'# rdp.register_opts(CONF)'
nl|'\n'
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
comment|'# vnc.register_opts(CONF)'
nl|'\n'
comment|'# volume.register_opts(CONF)'
nl|'\n'
comment|'# workarounds.register_opts(CONF)'
nl|'\n'
comment|'# wsgi.register_opts(CONF)'
nl|'\n'
comment|'# xenserver.register_opts(CONF)'
nl|'\n'
comment|'# xvp.register_opts(CONF)'
nl|'\n'
comment|'# zookeeper.register_opts(CONF)'
nl|'\n'
endmarker|''
end_unit
