from __future__ import unicode_literals
import tkinter as tk
import youtube_dl
import os
from moviepy.editor import VideoFileClip
import re
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np
def DownloadAndConvert(youtube_url,save_directory):
    os.chdir(save_directory)
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl.download([youtube_url])
        
        
    end_str = youtube_url.split('=')[-1]
    

    
    files = os.listdir(save_directory)
    for file in files:
        if len(re.findall(end_str,file)) != 0:

            downloaded_mp4 = file

            title_str = ''.join(re.split('-',file)[:-1])
            
            break    


    video = VideoFileClip(str(os.path.join(save_directory,downloaded_mp4)))
    
    video.audio.write_audiofile(title_str + '.wav')
    video.reader.close()
    video.audio.reader.close_proc()
    
    os.remove(downloaded_mp4)
    
    
    fs, data = wavfile.read(title_str + '.wav')

    l_track = data[:,0]
    r_track = data[:,1]



###########################################
    fc = 0.01
    b = 0.2
    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1
    n = np.arange(N)

    sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
    window = np.blackman(N)
    sinc_func = sinc_func * window
    sinc_func = sinc_func / np.sum(sinc_func)

    # reverse function
    sinc_func = -sinc_func
    sinc_func[int((N - 1) / 2)] += 1

    #s = list(data['10 Min Std Dev'])
    new_signal = np.convolve(l_track, 20* sinc_func)


    #out_track = l_track + (-1 * r_track)
    out_track = -10 * new_signal[:len(r_track)] + ( r_track)
    #out_track = 10 * new_signal




    scaled = np.int16(out_track/np.max(np.abs(out_track)) * 32767)
    write(title_str + '.mp3', 44100, scaled)
    
    os.remove(title_str + '.wav')
    
    
    return None

def run():
    youtube_url = e1.get()
    save_directory = e2.get()
    DownloadAndConvert(youtube_url,save_directory)
    return None



master = tk.Tk(className = ' Karaoke Creator')
tk.Label(master, text="URL to Download").grid(row=0)
tk.Label(master, text="Save Path").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
b1 = tk.Button(master, text = 'Close', command = quit)
b1.grid(row = 2, column = 0)
b2 = tk.Button(master, text = 'Run', command = run)
b2.grid(row = 2, column = 1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()








