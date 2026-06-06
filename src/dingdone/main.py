import subprocess
import argparse
import os
import threading



def main():
    arg = argparse.ArgumentParser(description="get a sound notification when your process is done,try `dingdone -h` for more information")
    arg.add_argument("-p","--process",help="your command",required=True)
    arg.add_argument("-s","--sound-address",default=os.path.join(os.path.dirname(__file__),"default_sound.mp3"),help="play your sound/music file, write the file address")
    arg.add_argument("-l","--loop",action="store_true",help="when you use this flag ,the sound will not stop until you press Enter or any key")
    args = arg.parse_args()
    p = subprocess.Popen(args.process,shell=True,stderr=subprocess.STDOUT,stdout=subprocess.PIPE,text=True)

    for i in p.stdout :
        print(i,end='')

    p.wait()
    stop = False
    import playsound as pl
    if args.loop :
        def key():
            nonlocal stop 
            input()
            stop = True
        t = threading.Thread(target=key)
        t.daemon = True
        t.start()
        while not stop:
            pl.playsound(args.sound_address)
    else :
        pl.playsound(args.sound_address)
if __name__ == "__main__":
    main()
