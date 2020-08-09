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

    def save(self):

        try:
            pmc.system.saveAs(self.path())
        except RuntimeError:
            log.warning("Missing directories. Creating directories")
            self.dir.makedirs_p()
            pmc.system.saveAs(self.path())

