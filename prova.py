from openstack import connection

conn = connection.Connection(
    auth_url="http://172.20.10.11:5000/v3",
    project_name="admin",
    username="admin",
    password="tuapassword",
    user_domain_id="default",
    project_domain_id="default"
)

for server in conn.compute.servers():
    print(server.name, server.status)
