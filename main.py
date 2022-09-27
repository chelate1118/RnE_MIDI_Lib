from MIDI_Pedal import _midiObj

midi = _midiObj("be_ps_14.mid")

for note in midi.midi.instruments[0].notes:
    print(note)

print("=" * 30)

for i in midi.pedalRange:
    print(i)
