from os import environ as env
import keystoneclient.v3.client as ksclient
import cinderclient
import novaclient
from keystoneauth1 import loading
from keystoneauth1 import session

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           project_name=env['OS_PROJECT_NAME'],
                           project_domain_name=env['OS_USER_DOMAIN_NAME'],
                           project_id=env['OS_PROJECT_ID'],
                           version=env['OS_IDENTITY_API_VERSION'],
                           user_domain_name=env['OS_USER_DOMAIN_NAME'],
                           region_name=env['OS_REGION_NAME'])

endpoints = keystone.service_catalog.get_endpoints()
print(endpoints)
for endpoint in endpoints:
    for edp in endpoints[endpoint]:
        #if edp['interface'] == 'public':
        print ('service: ', endpoint, ', region: ', edp['region'], ', public endpoint: ', edp['url'])

loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                project_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_id=env['OS_PROJECT_ID'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'])
sess = session.Session(auth=auth)
nova = novaclient.client.Client('2.1', session=sess)
nova.servers.list()
cinder = cinderclient.v3.client.Client('3', session=sess)
cinder.volumes.list()
testvol = cinder.volumes.create(size=1, name="li-ju-test")