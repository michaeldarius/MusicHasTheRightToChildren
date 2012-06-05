# -*- coding: UTF-8 -*-

from musichastherighttochildren.configuration import Configuration

class Globals(Configuration):
    EXTENSION_MP3 = 'mp3'
    EXTENSION_M4A = 'm4a'
    EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
    
    KEY_MUSICBRAINZ = 'TXXX:MusicBrainz'
    KEY_MUSICBRAINZ_ALBUMID = KEY_MUSICBRAINZ + ' ' + 'Album Id'