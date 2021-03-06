from cc_file_loader import *
from cc_logger import *
from cc_sprite_manager import *
from cc_texture import *
from cc_sprite import *
from pygame import *
from cc_resource_paths import *


class ccSpritesFileLoader(ccFileLoader):

    def __init__(self):
        pass

    def process_file(self, filename):
        try:
            self.load_file(ccResourcePaths.get_sprites() + filename)

        except:
            ccLogger.error(str(filename) + ' file could not be loaded.')
            raise RuntimeError('File could not be loaded.')
        self.__configure()
        self.__process_sprites()

    def __configure(self):
        self.file_name = self.current_dict['Config']['filename']
        self.cc_texture = ccTexture()
        self.cc_texture.load_image(self.file_name)
        ccSpriteManager.add_texture(self.file_name, self.cc_texture)

    def __process_sprites(self):
        self.set_first_section()
        while self.next_section():
            if 'num_of_sprites' in self.current_section:
                self.__create_multiple_sprites()
            else:
                self.__create_one_sprite()

    def __create_one_sprite(self):
        self.name = list(self.current_dict)[self.current_section_id]
        section = self.current_section
        hitbox = self.create_hitbox(section)
        rect = pygame.Rect(section['offset_x'], section['offset_y'], section['width'], section['height'])
        ccSpriteManager.add_sprite(self.name, ccSprite(ccSpriteManager.get_texture(self.file_name), rect, hitbox))

    def __create_multiple_sprites(self):
        offset_x = int(self.get_field("offset_x"))
        offset_y = int(self.get_field("offset_y"))
        num = 0

        for i in range(self.current_section['num_of_sprites']):
            if offset_x >= self.cc_texture.get_width():
                offset_y += int(self.get_field("height"))
                offset_x = 0
            self.name = list(self.current_dict)[self.current_section_id] + "%03d" % num
            section = self.current_section
            hitbox = self.create_hitbox(section)
            rect = pygame.Rect(offset_x, offset_y, section['width'], section['height'])
            ccSpriteManager.add_sprite(self.name, ccSprite(ccSpriteManager.get_texture(self.file_name), rect, hitbox))
            offset_x += section['width']
            num += 1

    def create_hitbox(self,section):
        if 'hitbox_width' in section:
            hitbox_offset_x = self.get_field('hitbox_offset_x')
            hitbox_offset_y = self.get_field('hitbox_offset_y')
            if hitbox_offset_x is None:
                hitbox_offset_x = 0
            if hitbox_offset_y is None:
                hitbox_offset_y = 0
            return pygame.Rect(hitbox_offset_x, hitbox_offset_y,
                                section['hitbox_width'], section['hitbox_height'])       
        return None
        
        