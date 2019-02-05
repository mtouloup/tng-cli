# Copyright (c) 2015 SONATA-NFV, 2017 5GTANGO
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the SONATA-NFV, 5GTANGO
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the SONATA project,
# funded by the European Commission under Grant number 671517 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.sonata-nfv.eu).
#
# This work has been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the 5GTANGO
# partner consortium (www.5gtango.eu).

# Building all paths for global use
sp_path = ''
pkg_api = ''
pkg_status_api = ''
request_api = ''
service_api = ''
function_api = ''
sl_templates_api = ''
sl_agreements_api = ''
sl_violations_api = ''
sl_guarantees_api = ''

def get_sp_path():

	return sp_path

def set_sp_path(new_base_path):

	global sp_path
	sp_path = new_base_path
	build_paths()

def build_paths():

	global pkg_api
	global pkg_status_api
	global request_api
	global service_api
	global function_api
	global sl_templates_api
	global sl_agreements_api
	global sl_violations_api
	global sl_guarantees_api

	gtk_api = ":32002/api/v3"
	pkg_api = sp_path + gtk_api + "/packages"
	pkg_status_api = pkg_api + "/status"
	request_api = sp_path + gtk_api + "/requests"
	service_api = sp_path + gtk_api + "/services"
	function_api = sp_path + gtk_api + "/functions"
	sl_templates_api = sp_path + gtk_api + "/slas/templates"
	sl_agreements_api = sp_path + gtk_api + "/slas/agreements"
	sl_violations_api = sp_path + gtk_api + "/slas/violations"
	sl_guarantees_api = sp_path + gtk_api + "/slas/configurations/guaranteesList"
