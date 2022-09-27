import pretty_midi


class midiObj:
    def __init__(self, path: str):
        self.midi = pretty_midi.PrettyMIDI(path)
        self.midi.remove_invalid_notes()


