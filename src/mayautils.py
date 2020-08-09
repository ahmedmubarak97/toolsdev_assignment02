import logging

import pymel.core as pmc
from pymel.core.system import Path

log = logging.getLogger(__name__)


class SceneFile(object):

    def __init__(self, dir='', descriptor='main', version=1, ext="ma"):
        self._dir = Path(dir)
        self.descriptor = descriptor
        self.version = version
        self.ext = ext
        scene = pmc.system.sceneName()
        if scene:
            self._init_properties_from_path(scene)

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, val):
        self._dir = Path(val)

    def basename(self):
        name_pattern = "{descriptor}_{version:03d}.{ext}"
        name = name_pattern.format(descriptor=self.descriptor,
                            version=self.version,
                            ext=self.ext)
        return name

    def path(self):
        return Path(self.dir) /  self.basename()

    def _init_properties_from_path(self, path):
        # TODO: convert this to a regex
        self._dir = path.dirname()
        self.ext = path.ext[1:]
        self.descriptor, version = path.name.split("_")
        self.version = int(version.split(".")[0][1:])

    def save(self):

        try:
            return pmc.system.saveAs(self.path())
        except RuntimeError:
            log.warning("Missing directories. Creating directories")
            self.dir.makedirs_p()
            return pmc.system.saveAs(self.path())

    def next_avail_version(self):
        pattern = "{descriptor}_v*.{ext}".format(descriptor=self.descriptor,ext=self.ext)
        self.dir.files()
        matched_scenes = [file for file in self.dir.files()
                          if file.fnmatch(pattern)]
        versions = [int(scene.name.split("_v")[1].split(".")[0])
                    for scene in matched_scenes]
        versions = list(set(versions))
        versions.sort()
        return versions[-1] + 1

    def increment_and_save(self):
        self.version = self.next_avail_version()
        self.save()
