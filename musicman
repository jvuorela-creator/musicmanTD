# Asenna ensin kirjasto komennolla: pip install midiutil
from midiutil import MIDIFile

midi = MIDIFile(2)
midi.addTempo(0, 0, 60)

# Basso-syke (C-molli)
for i in range(32):
    midi.addNote(0, 0, 36, i * 0.5, 0.5, 60) # C1 nuotti

# Synkkä melodia
notes = [48, 44, 43, 39, 48, 51, 50, 46] # C, Ab, G, Eb...
for i, note in enumerate(notes):
    midi.addNote(1, 0, note, i * 4, 4, 70)

with open("tangerine_dream.mid", "wb") as f:
    midi.writeFile(f)
