from midiutil import MIDIFile
import os

def luo_midi():
    # Luodaan MIDI-objekti (2 raitaa)
    midi = MIDIFile(2)
    midi.addTempo(0, 0, 60)

    # Raita 0: Basso-syke
    # 32 kpl 1/8-nuotteja (C1 = 36)
    for i in range(32):
        midi.addNote(0, 0, 36, i * 0.5, 0.5, 60)

    # Raita 1: Synkkä melodia
    # C, Ab, G, Eb, C, F, Eb, D (C-molli asteikkoa)
    notes = [48, 44, 43, 39, 48, 41, 39, 38]
    for i, note in enumerate(notes):
        midi.addNote(1, 0, note, i * 4, 4, 75)

    tiedoston_nimi = "tangerine_dream.mid"
    
    with open(tiedoston_nimi, "wb") as f:
        midi.writeFile(f)
    
    print(f"--- VALMIS! ---")
    print(f"Tiedosto '{tiedoston_nimi}' on luotu onnistuneesti.")
    print(f"Löydät sen täältä: {os.getcwd()}")

if __name__ == "__main__":
    luo_midi()
