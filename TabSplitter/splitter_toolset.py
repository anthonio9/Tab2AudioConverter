import guitarpro


def prepare_split_song(track, no_track):
    split_song = guitarpro.models.Song(
        versionTuple=track.song.versionTuple,
        title=track.song.title.replace(' ', '_') + f"_string_{no_track + 1}",
        artist=track.song.artist,
        pageSetup=track.song.pageSetup,
        tempoName=track.song.tempoName,
        tempo=track.song.tempo,
        key=track.song.key,
        measureHeaders=track.song.measureHeaders
        )

    print(split_song.title)
    return split_song


def create_empty_beat(base_beat, voice):
    beat_new = guitarpro.models.Beat(
            voice=voice,
            duration=base_beat.duration,
            text=base_beat.text,
            start=base_beat.start,
            effect=base_beat.effect,
            octave=base_beat.octave,
            display=base_beat.display,
            status=base_beat.status
            )

    voice.beats.append(beat_new)
    return beat_new


def copy_note(note, beat):
    note_new = guitarpro.models.Note(
            beat=beat,
            value=note.value,
            velocity=note.velocity,
            string=note.string,
            effect=note.effect,
            durationPercent=note.durationPercent,
            swapAccidentals=note.swapAccidentals,
            type=note.type
            )
    return note_new


def split_track_into6_songs(track):
    split_songs = [prepare_split_song(track, i) for i in range(6)]

    for m, measure in enumerate(track.measures):
        # print(measure.number)
        tracks_remote = [song.tracks[0] for song in split_songs]

        def compensate_voice_amount(track, m, measure):
            # add more voices if its number isn't matching
            no_voices_remote = len(track.measures[m].voices)
            no_voices_local = len(measure.voices)

            for i in range(no_voices_local - no_voices_remote):
                track.measures[m].voices.append(
                        guitarpro.models.Voice(track.measures[m]))

        # compensate_voice_amount(track_remote, m, measure)
        for track in tracks_remote:
            compensate_voice_amount(track, m, measure)

        # add beats and notes to the track_remote
        for v, voice in enumerate(measure.voices):
            voices_remote = [track.measures[m].voices[v]
                             for track in tracks_remote]

            for b, beat in enumerate(voice.beats):
                # firts, add an empty beat
                beats_remote = [create_empty_beat(beat, voice)
                                for voice in voices_remote]

                for note in beat.notes:
                    # not sure what the string indexing is in the Note Class?
                    if note.string > 0 and note.string <= 6:
                        beats_remote[note.string - 1].notes.append(
                                copy_note(note, beats_remote[note.string - 1]))

    return split_songs
