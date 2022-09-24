from midi_process import MidiPedal

test = MidiPedal("test.mid")
test.debug(print_all=True, witch=lambda x: 'control' in x.type, form=lambda x: x.control)
test.filter(witch=lambda x: 'control_change' != x.type or x.control == 64)
print()
test.debug(print_all=True, witch=lambda x: 'control' in x.type, form=lambda x: x.control)
test.export()
