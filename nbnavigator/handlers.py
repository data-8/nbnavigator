import json
# import psutil
import requests
import os
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

def get_token():
    # To implement once authenticator stuff is done
    return

def parse_offering(offering):
    return offering.replace("_", "/")

def get_courses():
    jpy_user = "alinxie@berkeley.edu"
    #token = "FBbpbjZ3DfLKgbWzysQU5atui8tAYR"
    token = os.environ.get('OKPY_ACCESS_TOKEN')
    course_api = "https://okpy.org/api/v3/enrollment/{}".format(jpy_user)
    api_params = {'access_token': token}
    course_request = requests.get(course_api, params = api_params)
    response = course_request.json()
    return {'courses': response['data']['courses'], 'code': response['code']}

def get_assignments(offering):
    assignment_api = "https://okpy.org/api/v3/course/{}/assignments".format(offering)
    assignment_request = requests.get(assignment_api)
    response = assignment_request.json()
    return {'assignments': response['data']['assignments'], 'code':response['code']}

class AssignmentsHandler(IPythonHandler):
    def get(self):
        self.finish(json.dumps(get_assignments(self.get_argument('offering'))))
        #self.finish(json.dumps({'offering': self.get_argument('offering')}))

class CourseHandler(IPythonHandler):
    def get(self):
        self.finish(json.dumps(get_courses()))

def setup_handlers(nb_app):
    nb_app.log.info("Hello, world")
    nb_app.log.info(os.environ.get('USER'))
    nb_app.log.info(os.environ.get('OKPY_ACCESS_TOKEN'))
    web_app = nb_app.web_app
    nb_app.log.info(dir(web_app))
    assignment_route_pattern = url_path_join(web_app.settings['base_url'], '/assignments')
    course_route_pattern = url_path_join(web_app.settings['base_url'], '/courses')
    web_app.add_handlers('.*',
        [(assignment_route_pattern, AssignmentsHandler),
        (course_route_pattern, CourseHandler)
        ])
    return
