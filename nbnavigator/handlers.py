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
    token = "FBbpbjZ3DfLKgbWzysQU5atui8tAYR"
    course_api = "https://okpy.org/api/v3/enrollment/{}".format(jpy_user)
    api_params = {'access_token': token}
    course_request = requests.get(course_api, params = api_params)
    return course_request.json()

def get_assignments():
    offering = self.get_arguments
    assignment_api = "https://okpy.org/api/v3/course/{}/assignments".format(offering)
    assignment_request = request.get(assignment_api)
    return assignment_request.json()

class AssignmentsHandler(IPythonHandler):
    def get(self):
        self.finish(json.dumps(get_assignments()))

class CourseHandler(IPythonHandler):
    def get(self):
        self.finish(json.dumps(get_courses()))

def setup_handlers(web_app):
    web_app.log.info("Hello, world")
    web_app.log.info(os.environ.get('$JPY_USER'))
    assignment_route_pattern = url_path_join(web_app.settings['base_url'], '/assignments')
    course_route_pattern = url_path_join(web_app.settings['base_url'], '/courses')
    web_app.add_handlers('.*', [(route_pattern, AssignmentsHandler), (route_pattern, CourseHandler)])ß
    return
