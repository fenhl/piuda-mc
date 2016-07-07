from spockbot.plugins.base import PluginBase, pl_announce

@pl_announce('PiudaPlugin')
class PiudaPlugin(PluginBase):
    requires = ('Chat', 'ClientInfo', 'Movement')
    events = {
        'client_join_game': 'perform_initial_actions',
        'client_position_update': 'start_bot'
    }

    def __init__(self, ploader, settings):
        super(PiudaPlugin, self).__init__(ploader, settings)

        self.started = False

    def perform_initial_actions(self, name, data):
        # Say hello
        self.chat.chat('Eana!')

    def start_bot(self, _, __):
        if self.started:
            return
        else:
            self.started = True
        pass #TODO bot actions
