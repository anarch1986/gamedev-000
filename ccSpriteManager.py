class ccSpriteManager:

    textures = {}
    sprites = {}

    def __init__(self):
        stop_being_a_noob = "You cannot instantiate this class. Now go cry in the corner."
        raise Exception(stop_being_a_noob)

    @classmethod
    def add_texture(cls, texture_name, texture):
        # add the ccTexture to the textures dictionary, but only if it's not
        # already there (texture_name is the key). If it is there, don't add and
        # print a warning msg that says that we wanted to load it twice
        if texture_name in ccSpriteManager.textures:
            print("Warning: ccTexture is already loaded.")
        else:
            ccSpriteManager.textures[texture_name] = texture

    @classmethod
    def get_texture(cls, texture_name):
        # give back the ccTexture. If it can't be found, write an error msg and return with None
        texture = ccSpriteManager.textures.get(texture_name)
        if texture:
            return texture
        else:
            print("Error: ccTexture not found.")

    @classmethod
    def add_sprite(cls, sprite_name, sprite):
        # add ccSprite to sprites dictionary but only if it is not there
        # (sprite_name is the key). If it is there, print a warning msg and don't
        # overwrite the previous one
        if sprite_name in ccSpriteManager.sprites:
            print("Warning: ccSprite is already loaded. It will not be overwritten.")
        else:
            ccSpriteManager.sprites[sprite_name] = sprite

    @classmethod
    def get_sprite(cls, sprite_name):
        # give back the ccSprite. If it can't be found, write an error msg and return with None
        sprite = ccSpriteManager.sprites.get(sprite_name)
        if sprite:
            return sprite
        else:
            print("Error: ccSprite not found.")
