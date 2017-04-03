import os
import cc_logger

class ccResourcePaths:

    base_path = os.path.dirname(os.path.realpath(__file__))
    resource_path = base_path + "/resources/"

    def __init__(self):
        ccLogger.error("ccResourcePath can not be instanted")
        raise NotImplementedError

    @classmethod
    def get_resources(cls):
        return cls.resource_path

    @classmethod
    def get_objects(cls):
        return cls.resource_path  + "objects/"

    @classmethod
    def get_sprites(cls):
        return cls.resource_path + "sprites/"

    @classmethod
    def get_anims(cls):
        return cls.resource_path + "anims/"

    @classmethod
    def get_object_scenes(cls):
        return cls.resource_path + "object_scenes/"

    @classmethod
    def get_acts(cls):
        return cls.resource_path + "acts/"


