# Dingdone

Get a sound notification when your long-running task finishes.

Dingdone is a lightweight Python CLI tool that plays a sound when a command completes.
You can use a custom sound or the default beep.loop stops after current playback finishes

## Features
- Run any command and get sound when it's done
- Use custom sound files
- Optional looping until user stops it

## Usage
`dingdone -p "sleep 3" -s "music.mp3"`

Plays music.mp3 after the command finishes.

`dingdone -p "sleep 2" -s "music.mp3" -l`

Plays the sound in a loop until you press Enter.

`dingdone -p "sleep 1"`

Uses the default beep sound.

## CLI
You can run it using:
- `dingdone`
- `ddone`
- `ding`(my favorite)
- `python -m dingdone`

## Help
If anything is unclear, feel free to ask or run:

`dingdone -h`

I’m open to feedback, ideas, and questions 🙂
