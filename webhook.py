import cherrypy
from controller.map import Map

config = {'/static': {'tools.staticdir.on': True,
    'tools.staticdir.dir': "/home/gaurav/dnt_maps/static_files/",
}}

cherrypy.tree.mount(Map(),config=config)

cherrypy.config.update({'server.socket_host': 'localhost', })
cherrypy.config.update({'server.socket_port': 8004, })

cherrypy.engine.start()
cherrypy.engine.block()
