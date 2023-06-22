import xml.etree.ElementTree as XMLElementTree

class AFNState:
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
        self._initial_state = None
        self._states = {}

    def _get_or_create_state(self, label: str):
        state = self._states.get(label)
        if state is None:
            state = AFNState(label)
            self._states[label] = state
        return state

    def set_initial_state(self, label: str):
        self._initial_state = self._get_or_create_state(label)

    def add_final_state(self, label: str):
        state = self._get_or_create_state(label)
        state.set_final(True)

    def add_transition(self, origin, symbol, dest):
        origin = self._get_or_create_state(origin)
        dest   = self._get_or_create_state(dest)
        origin.add_transition(symbol, dest)

    def parse(self, input: str) -> bool:
        if self._initial_state is None:
            return False
        
        states = [self._initial_state]
        for symbol in input:
            new_states = []
            for state in states:
                new_states += state.transition(symbol)
            if len(new_states) == 0:
                return False
            states = new_states

        for state in states:
            if state.is_final():
                return True;
        return False

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
    
    def quintuple(self):
        print("M = (A, Q, P, q0, F)")
        print("A = {" + ", ".join(set([symbol for state in self._states.values() for symbol in state._transitions.keys()])) + "}")
        print("Q = {" + ", ".join(self._states.keys()) + "}")
        for state in self._states.values():
            for symbol, dst in state._transitions.items():
                print("P(" + state._label + ", " + symbol + ") = " + ", ".join([d._label for d in dst]))
        print("q0 = " + self._initial_state._label)
        print("F = {" + ", ".join([state._label for state in self._states.values() if state._is_final]) + "}")