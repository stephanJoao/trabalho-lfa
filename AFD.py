import xml.etree.ElementTree as XMLElementTree

class AFDState:
    def __init__(self, label: str, is_final = False):
        self._label = label
        self._transitions = {}
        self._is_final = is_final

    def label(self):
        return self._label

    def is_final(self) -> bool:
        return self._is_final

    def set_final(self, is_final):
        self._is_final = is_final

    def add_transtion(self, symbol: str, dst):
        self._transitions[symbol] = dst
        
    def transition(self, symbol: str):
        return self._transitions.get(symbol)

class AFD:
    def __init__(self):
        self._initial_state = None
        self._states = {}

    def _get_or_create_state(self, label: str):
        state = self._states.get(label)
        if state is None:
            state = AFDState(label)
            self._states[label] = state
        return state

    def set_initial_state(self, label: str):
        self._initial_state = self._get_or_create_state(label)

    def add_final_state(self, label: str):
        state = self._get_or_create_state(label)
        state.set_final(True)

    def add_transition(self, origin, symbol: str, dst):
        origin = self._get_or_create_state(origin)
        dst    = self._get_or_create_state(dst)
        origin.add_transtion(symbol, dst)

    def parse(self, input: str):
        if self._initial_state is None:
            return False
        
        state = self._initial_state
        for symbol in input:
            state = state.transition(symbol)
            if state is None:
                return False
            
        return state.is_final()

    @staticmethod
    def from_xml(xml_file_path: str):
        tree = XMLElementTree.parse(xml_file_path)
        root = tree.getroot()

        afd = AFD();

        transition_function = root.find('funcaoPrograma')
        if transition_function is not None:
            for elem in transition_function.findall('elemento'):
                origin = elem.get('origem')
                dst    = elem.get('destino')
                symbol = elem.get('simbolo')

                if origin is not None and dst is not None and symbol is not None:
                    afd.add_transition(origin, symbol, dst)

        final_states = root.find('estadosFinais')
        if final_states is not None:
            for elem in final_states.findall('elemento'):
                state_label = elem.get('valor')
                if state_label is not None:
                    afd.add_final_state(state_label)

        initial_state = root.find('estadoInicial')
        if initial_state is not None:
            initial_state = initial_state.get('valor')
            if initial_state is not None:
                afd.set_initial_state(initial_state)
        return afd
