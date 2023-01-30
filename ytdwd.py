
# YouTube video downloader


from pytube import YouTube
link = input("Enter the link of youtube video:  ")
yt = YouTube(link)

# for the highest resolution
dw = yt.streams.get_highest_resolution()
print("Downloading...")

# Specifying the location
dw.download("Downloads\python")
print("Download completed!!")
