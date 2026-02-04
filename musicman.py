import streamlit as st
from midiutil import MIDIFile
from io import BytesIO  # Tarvitaan tiedoston käsittelyyn muistissa

st.title("Tangerine Dream MIDI-generaattori 🎹")
st.write("Tämä sovellus luo MIDI-tiedoston suoraan selaimessa.")

def luo_midi_data():
    # Luodaan MIDI-objekti
    midi = MIDIFile(2)
    midi.addTempo(0, 0, 60)

    # Raita 0: Basso
    for i in range(32):
        midi.addNote(0, 0, 36, i * 0.5, 0.5, 60)

    # Raita 1: Melodia
    notes = [48, 44, 43, 39, 48, 41, 39, 38]
    for i, note in enumerate(notes):
        midi.addNote(1, 0, note, i * 4, 4, 75)

    # TÄRKEÄ MUUTOS:
    # Emme tallenna tiedostoa levylle (open...), vaan muistiin (BytesIO).
    # Tämä on välttämätöntä pilvipalveluissa.
    mem_file = BytesIO()
    midi.writeFile(mem_file)
    
    # Palautetaan tiedoston binääridata
    return mem_file.getvalue()

# Luodaan data valmiiksi
midi_data = luo_midi_data()

# Luodaan latauspainike Streamlitiin
st.download_button(
    label="Lataa MIDI-tiedosto",
    data=midi_data,
    file_name="tangerine_dream.mid",
    mime="audio/midi"
)

st.success("Tiedosto on valmis ladattavaksi yllä olevasta painikkeesta!")
