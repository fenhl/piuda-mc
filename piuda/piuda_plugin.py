from spockbot.plugins.base import PluginBase, pl_announce

@pl_announce('PiudaPlugin')
class PiudaPlugin(PluginBase):
    requires = ()
    events = {}
