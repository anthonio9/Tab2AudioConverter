import argparse
import guitarpro
from pathlib import Path
import splitter_toolset as split


def main(source, dest):
    gp_path = Path(source)
    dst_path = gp_path.parent

    if dest is not None:
        dst_path = Path(dest)

    try:
        tab = guitarpro.parse(gp_path)
    except guitarpro.GPException as exception:
        print(f"###This is not a supported GuitarPro file: \
                {gp_path}: {exception}")

    else:
        # format stem
        gp_path_stem = gp_path.stem \
            .replace(' ', '_').replace('.', '_')

        # create a directory for all new tabs
        gp_tab_dir = Path(dst_path, gp_path_stem)
        gp_tab_dir.mkdir(parents=True, exist_ok=True)

        for track in tab.tracks:
            # percussive tracks to garbage
            if track.isPercussionTrack:
                continue

            # accept only 6-guitar string tracks
            if len(track.strings) != 6:
                continue

            # only real tracks left
            songs = split.split_track_into6_songs(track)
            track_name = track.name.replace('.', '_') \
                .replace(' ', '_').lower()

            # create a dir for each track
            gp_path_track_dir = Path(gp_tab_dir, track_name)
            gp_path_track_dir.mkdir(parents=True, exist_ok=True)

            for s, song in enumerate(songs):
                # create a new file for new string
                new_string_name = \
                    f"{gp_path_stem}_{track_name}_{s}{gp_path.suffix}"
                gp_path_track_string = Path(
                        gp_path_track_dir, new_string_name)
                guitarpro.write(song, gp_path_track_string)

    print("\nDone!")


if __name__ == '__main__':
    description = """Split guitar tracks into single-string tracks
     from a given guitar pro file."""

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--src',
                        metavar='SOURCE',
                        dest='source',
                        help='path to the source tabs folder')
    parser.add_argument('--dst',
                        metavar='DESTINATION',
                        dest='dest',
                        help='path to the destination tabs folder')
    args = parser.parse_args()

    kwargs = dict(args._get_kwargs())
    main(**kwargs)
