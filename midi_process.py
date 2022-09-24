import mido


class MidiPedal:
    def __init__(self, path: str):
        self.midi = mido.MidiFile(path)

    def debug(self,
              row=0,
              witch=lambda x: True,
              form=lambda x: x,
              print_all=False):
        collected = self.collect(witch)
        if print_all:
            for i, track in enumerate(collected):
                print(f"\nTrack #{i}\t: ", end=' ')
                for j in track:
                    print(form(j), end=' ')
        else:
            for i in collected[row]:
                print(form(i))

    def collect(self,
                witch=lambda x: True) -> mido.MidiTrack[mido.MidiTrack]:
        ret = mido.MidiTrack()
        for i in self.midi.tracks:
            back_track = mido.MidiTrack()
            for j in i:
                if witch(j):
                    back_track.append(j)
            ret.append(back_track)
        return ret

    def filter(self,
               witch=lambda x: True):
        for i, track in enumerate(self.midi.tracks):
            self.midi.tracks[i] = list(filter(witch, track))

    def export(self, path: str = 'output/test.mid'):
        self.midi.save(path)
