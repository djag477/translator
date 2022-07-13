
import youtube_dl
from subprocess import getoutput


# we need an input 

video = input("What video you want? ") # insert youtube link of video to download

# store subtitles to know what are our options

command = f"youtube-dl {video} --list-subs"
list_subs = getoutput(command)


with open("sub_list-wsubs.txt", "w+") as f:
    f.write(list_subs)

with open("sub_list-wsubs.txt", "r") as f:
    lines = f.readlines()
    
# evaluate if subs are automatic or uploaded and which English version is submitted

subs = ""
help_list = []

for i in lines:
    if "Available subtitles for" in i:
        print("Available subtitles for ", video)

        for i in lines:
            if "en" in i:
                help_list.append(i[:i.find("  ")])

        subs = "--write-sub"

    elif "Available automatic captions" in i:
        print("Available automatic captions ", video)

        for i in lines:
            if "en" in i:
                help_list.append(i[:i.find("  ")])

        subs = "--write-auto-sub"

# run the command depending on the type of subtitles

keep_vid = input("To keep the video input '-k', to delete, input '-x' ")

if subs == "--write-auto-sub":
    opts = [video, f"{keep_vid}", "--audio-format", "mp3", f"{subs}", "-o", './%(title)s.%(ext)s']
    

else: 
    print(help_list)
    sub_lang = int(input("Index of subs to use: "))
    opts = [video, f"{keep_vid}", "--audio-format", "mp3", f"{subs}", "--sub-lang", help_list[sub_lang], "-o", './%(title)s.%(ext)s']
    

youtube_dl.main(opts)


