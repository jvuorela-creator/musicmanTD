from midiutil import MIDIFile
from pathlib import Path  # Tämä kirjasto auttaa kansioiden hallinnassa

def luo_midi():
    # Luodaan MIDI-objekti (2 raitaa)
    midi = MIDIFile(2)
    midi.addTempo(0, 0, 60)

    # Raita 0: Basso-syke
    for i in range(32):
        midi.addNote(0, 0, 36, i * 0.5, 0.5, 60)

    # Raita 1: Melodia
    notes = [48, 44, 43, 39, 48, 41, 39, 38]
    for i, note in enumerate(notes):
        midi.addNote(1, 0, note, i * 4, 4, 75)

    # MÄÄRITETÄÄN TALLENNUSPAIKKA:
    # Path.home() hakee käyttäjäkansion (esim. C:\Users\Matti)
    # ja lisää siihen "Downloads"-kansion.
    lataukset_kansio = Path.home() / "Downloads"
    
    # Luodaan lopullinen tiedostopolku
    tiedoston_nimi = lataukset_kansio / "tangerine_dream.mid"
    
    try:
        with open(tiedoston_nimi, "wb") as f:
            midi.writeFile(f)
        
        print(f"--- VALMIS! ---")
        print(f"Tiedosto tallennettiin onnistuneesti Lataukset-kansioon.")
        print(f"Tarkka sijainti: {tiedoston_nimi}")
        
    except FileNotFoundError:
        # Varmuuskopio: jos "Downloads" kansiota ei löydy (harvinaista),
        # tallennetaan nykyiseen kansioon.
        print("Huom: Downloads-kansiota ei löytynyt automaattisesti.")
        with open("tangerine_dream.mid", "wb") as f:
            midi.writeFile(f)
        print("Tiedosto tallennettiin samaan kansioon, jossa koodi on.")

if __name__ == "__main__":
    luo_midi()
