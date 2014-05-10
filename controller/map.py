import cherrypy
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('static_files'))

class Map:
    @cherrypy.expose
    def map(self):
        tmp = env.get_template("map.html")
        return tmp.render(type="map")
    map.exposed = True
