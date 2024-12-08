class RPCBase(object):
    config = {
        "tikcast.game.task_center": {
            "idl_version": "master",
            'zone': 'SGALI',
            'idc': 'sg1',
            'cluster': 'default',
            'online': True,
        }
    }

    def __init__(self, psm, env, idl_version=None, zone=None, idc=None, cluster=None, online=None):
        idl_version = self.config[psm]["idl_version"]
        zone = self.config[psm]["zone"]
        idc = self.config[psm]["idc"]
        cluster = self.config[psm]["cluster"]
        online = self.config[psm]["online"]

        self.json_data = {
            'serialization': 'json',
            'psm': psm,
            'func_name': '',
            'idl_source': 1,
            'idl_version': idl_version,
            'env': env,
            'test_plane': 1,
            'zone': zone,
            'idc': idc,
            'cluster': cluster,
            'http_req_headers': [],
            'http_cookies': [],
            'http_query': [],
            'req_body': '',
            'form_req_body': [],
            'rpc_context': [],
            'request_timeout': 60000,
            'connect_timeout': 60000,
            'source': 1,
            'protocol': 'thrift',
            'online': online,
        }
