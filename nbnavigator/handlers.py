import json
# import psutil
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

# def rss():
#     cur_process = psutil.Process()
#     all_processes = [cur_process] + cur_process.children(recursive=True)
#     return sum([p.memory_info().rss for p in all_processes])

# def cgroup_memory_limit():
#     m = open('/sys/fs/cgroup/memory/memory.limit_in_bytes').read().strip()
#     return int(m)

# def get_metrics():
#     return {
#         'rss': rss(),
#         'cgroup_memory_limit': cgroup_memory_limit(),
#     }


class MetricsHandler(IPythonHandler):
    def get(self):
        self.finish(json.dumps(get_metrics()))


def setup_handlers(web_app):
    #route_pattern = url_path_join(web_app.settings['base_url'], '/metrics')
    # web_app.add_handlers('.*', [(route_pattern, MetricsHandler)])
    return
