#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import os

from mhtrtc import MHTRTC
from retrieval.collection import Collection
from retrieval.itunes import iTunes
from aux.shell import Shell
from settings.settings import Settings

class Backups(MHTRTC):

    MAX = 8
    ITUNES_JSON = 'data/itunes.json'
    COLLECTION_JSON = 'data/collection.json'

    def __init__(self):
        u"""
        """
        super(Backups, self).__init__()
        itunes = self.getITunes()
        collection = self.getCollection()
        self.compareCollection(collection, itunes)

    def compareCollection(self, collection, itunes):
        for artist, albums1 in collection.items():
            artist = self.compareArtists(artist, itunes.keys())

            if not artist is None:
                albums2 = itunes[artist]
                self.compareAlbums(artist, albums1, albums2)

    def compareArtists(self, artist, artists):
        if artist in artists:
            return artist
        else:
            artist = artist.replace('_', '/')
            if artist in artists:
                return artist

        print 'Missing artist %s' % artist

    def compareAlbums(self, artist, albums1, albums2):
        found = False

        for album in albums1:
            if album in albums2:
                found = True
            else:
                slash_album = album.replace('_', '/')
                if slash_album in albums2:
                    found = True

        if not found:
            print 'Missing album %s for artist %s' % (album, artist)

    def getCollection(self):
        if not os.path.exists(self.COLLECTION_JSON):
            collection = Collection(self.settings.BACKUP, verbose=True).asDict()
            self.writeJSON(self.COLLECTION_JSON, collection)
        else:
            collection = self.readJSON(self.COLLECTION_JSON)
        print 'Finished loading %s' % self.COLLECTION_JSON
        return collection

    def getITunes(self):
        if not os.path.exists(self.ITUNES_JSON):
            itunes = iTunes(self.settings.BACKUP_LIBRARY).asDict()
            self.writeJSON(self.ITUNES_JSON, itunes)
        else:
            itunes = self.readJSON(self.ITUNES_JSON)
        print 'Finished loading %s' % self.ITUNES_JSON
        return itunes

if __name__ == '__main__':
    b = Backups()