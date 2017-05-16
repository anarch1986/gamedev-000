from cc_basic_object import ccBasicObject
from cc_anim_frame import ccAnimFrame
from cc_anim_sprite import ccAnimSprite
from cc_logger import ccLogger
from cc_sprite_manager import ccSpriteManager
from cc_anims_file_loader import ccAnimsFileLoader
from copy import deepcopy


class ccAnimObject(ccBasicObject):

    def __init__(self):
        super().__init__()
        self.type = 'ccAnimObject'
        self.time = 0
        self.anims = []
        self.current_anim = None
        self.current_frame = None
        self.active_sprite = None

    def load(self, anim_data):
        try:
            super().load(anim_data)
            if 'animations' in anim_data:
                for anim_name in anim_data['animations']:
                    anim = ccSpriteManager.get_sprite(anim_name)
                    self.anims.append(anim)
            if 'start_anim' in anim_data:
                self.current_anim = ccSpriteManager.get_sprite(anim_data['start_anim'])
                self.current_frame = self.current_anim.get_frame(0)
                self.active_sprite = self.current_frame.get_sprite()

        except:
            ccLogger.error('Sprite could not be loaded.: ')
            raise RuntimeError('Sprite could not be loaded.')

    def add_anim(self, anim):
        if type(anim) == 'ccAnimSprite':
            self.anims.append(anim)
        else:
            ccLogger.error('Not Anim sprite' + type(anim))

    def draw(self, renderer):
        ccBasicObject.draw(self, renderer)

    def step(self, time_passed):  # time passed = frame's time
        super().step(time_passed)
        self.time += time_passed
        if self.current_frame.time <= self.time:
            self.time -= self.current_frame.time
            self.current_frame = self.current_anim.get_frame(self.current_frame.get_next_frame())
            if self.current_frame is None:
                self.current_frame = self.current_anim.get_frame(0)
                ccLogger.warning("Animation change should be implemented")
                # WARNING
            self.active_sprite = self.current_frame.get_sprite()

    def play(self, anim_name=None):
        # set and start playing an anim. anim_name is optional,
        # it should play the current animation if the anim_name is not set
        # if an anim was paused, resume from that point where it was
        pass

    def pause(self):
        # pause the current animation
        pass

    def reset(self):
        # don't change the animation but reset it to start
        # pause the animation
        pass

    def copy(self):
        new_object = ccAnimObject()
        self.__fill(new_object)
        return new_object

    def __fill(self, source):
        source.position = deepcopy(self.position)
        source.velocity = deepcopy(self.velocity)
        source.active_sprite = self.active_sprite
        source.type = self.type
        source.id = deepcopy(self.id)
        source.object_props = deepcopy(self.object_props)
        source.time = 0
        source.anims = self.anims
        source.current_anim = deepcopy(self.current_anim)
        source.current_frame = deepcopy(self.current_frame)
