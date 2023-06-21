import xml.etree.ElementTree as XMLElementTree

class AFNState:
    def __init__(self, label: str, is_final = True):
        self._label = label
        self._is_final = is_final
        self._transitions = {}

    def label(self):
        return self._label

    def is_final(self) -> bool:
        return self._is_final

    def set_is_final(self, is_final):
        self._is_final = is_final

    def add_transition(self, symbol: str, state):
        transitions = self._transitions.get(symbol)

        if transitions is None:
            transitions = []
            self._transitions[symbol] = transitions
        transitions.append(state)

    def transition(self, symbol: str):
        dest_list = self._transitions.get(symbol)
        return dest_list if dest_list is not None else []

class AFN:
    def __init__(self):
        self._initital_state = None
        self._states = {}

    @staticmethod
    def from_xml(xml_file_path: str):
        tree = XMLElementTree.parse(xml_file_path)
        root = tree.getroot()

        afn = AFN();

        transition_function = root.find('funcaoPrograma')
        if transition_function is not None:
            for elem in transition_function.findall('elemento'):
                origin = elem.get('origem')
                dst    = elem.get('destino')
                symbol = elem.get('simbolo')

                if origin is not None and dst is not None and symbol is not None:
                    afn.add_transition(origin, symbol, dst)

        final_states = root.find('estadosFinais')
        if final_states is not None:
            for elem in final_states.findall('elemento'):
                state_label = elem.get('valor')
                if state_label is not None:
                    afn.add_final_state(state_label)

        initial_state = root.find('estadoInicial')
        if initial_state is not None:
            initial_state = initial_state.get('valor')
            if initial_state is not None:
                afn.set_initial_state(initial_state)
        return afn 

    def _get_or_create_state(self, label: str):
        state = self._states.get(label)
        if state is None:
            state = AFNState(label)
            self._states[label] = state
        return state

    def set_initial_state(self, state_label: str):
        state = self._get_or_create_state(state_label)
        self._initital_state = state

    def add_final_state(self, state_label: str):
        state = self._get_or_create_state(state_label)
        state.set_is_final(True)

    def add_transition(self, origin, symbol, dest):
        origin = self._get_or_create_state(origin)
        dest   = self._get_or_create_state(dest)
        origin.add_transition(symbol, dest)

    def parse(self, input: str) -> bool:
        if self._initital_state is None:
            return False
        states = [self._initital_state]
        for symbol in input:
            new_states = []
            for state in states:
                # NOTE(igolt): eu sei que eu vou esquecer então: o operador
                # "+" concatena duas listas
                new_states += state.transition(symbol)
            if len(new_states) == 0:
                return False
            states = new_states

        for state in states:
            if state.is_final():
                return True;
        return False
