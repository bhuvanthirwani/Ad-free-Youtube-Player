import PySimpleGUI as sg
import vlc
import os
from sys import platform as PLATFORM
import speech_recognition as sr 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from pytube import YouTube    

sg.theme('SystemDefault')

def btn1(name):
    return sg.Button(name, size=(20, 3), pad=(1, 1))

layout1 = [[sg.Text('    Choose your preferred interface type', size=(30, 1), font=("Helvetica", 25), text_color='black')],
          [btn1('Voice'), btn1('Mouse')],
          ]

window1 = sg.Window('Ad-free Youtube Player', layout=layout1, element_justification='center', finalize=True, resizable=True, keep_on_top = True)
window1.Normal()
window1.Minimize()
window1.Normal()
window1.TKroot.focus_force()

def get_subtitles(link):
    if os.path.exists("Captions.srt"):
        os.remove("Captions.srt")
    source = YouTube(link)
    en_caption = source.captions.get_by_language_code('en')

    try:
        en_caption_convert_to_srt =(en_caption.generate_srt_captions())
        text_file = open("Captions.srt", "w")
        text_file.write(en_caption_convert_to_srt)
        text_file.close()
    except:
        pass

def download_video_youtube(link,path,search): 
    name =search #Name to be given to the downloaded file

    try:
        yt_obj = YouTube(link)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        #print("Downloading...")
        filters.get_highest_resolution().download(filename=name)
        #print('Video Downloaded Successfully')
    except Exception as e:
        pass

while True:
    event, values = window1.read(timeout=1000)
   
    if(event=='Mouse'):
        window1.close()
        def btn(name):  # a PySimpleGUI "User Defined Element" (see docs)
            return sg.Button(name, size=(7, 1), pad=(1, 1))

        layout = [[sg.Text('Enter Youtube Search', font=("Helvetica", 10), text_color='black')],
                  [sg.Input(default_text='', size=(30, 1), key='-VIDEO_LOCATION-'), sg.Button('load')],
                  [sg.Image('', size=(300, 170), key='-VID_OUT-')],
                  [btn('play'), btn('pause'), btn('stop')],
                  [btn('mute'), btn('subtitles'), btn('download')],
                  [sg.Text('Load media to start', key='-MESSAGE_AREA-')]]

        window = sg.Window('Ad-free Youtube Player', layout, element_justification='center', finalize=True, resizable=True, keep_on_top = True)
        window.Normal()
        #window.Maximize()
        window.Minimize()
        window.Normal()
        window.TKroot.focus_force()
        window.Element('-VIDEO_LOCATION-').focus=True
        window.Element('-VIDEO_LOCATION-').SetFocus()
        window['-VID_OUT-'].expand(True, True)                # type: sg.Element
        #------------ Media Player Setup ---------#

        inst = vlc.Instance()
        list_player = inst.media_list_player_new()
        media_list = inst.media_list_new([])
        media_player = inst.media_player_new()
        list_player.set_media_list(media_list)
        player = list_player.get_media_player()
        if PLATFORM.startswith('linux'):
            player.set_xwindow(window['-VID_OUT-'].Widget.winfo_id())
        else:
            player.set_hwnd(window['-VID_OUT-'].Widget.winfo_id())
        link=''
        que=' '
        #------------ The Event Loop ------------#
        while True:
            event, values = window.read(timeout=1000)       # run with a timeout so that current location can be updated
            if event == sg.WIN_CLOSED or event=='Cancel':
                list_player.pause()
                list_player.stop()
                break
            if event == 'play':
                list_player.play()
            if event == 'pause':
                list_player.pause()
            if event == 'stop':
                list_player.stop()
                print('stop')

            if event == 'mute':
                if player.audio_get_mute() == False:
                    player.audio_set_mute(True)
                else:
                    player.audio_set_mute(False)
            if event == 'download':
                if(link!=''):
                    download_video_youtube(link,'',que1)
            if event == 'subtitles':
                player.video_set_subtitle_file('Captions.srt')
                player.video_set_spu(0)
            if event == 'load':
                list_player.stop()
                player.stop()

                if(media_list.count()==1):
                    media_list.remove_index(0)
                media_list.add_media(values['-VIDEO_LOCATION-'])
                list_player.set_media_list(media_list)

                    window['-VIDEO_LOCATION-'].update(que) # only add a legit submit
                get_subtitles(link)
            if player.is_playing():
                window['-MESSAGE_AREA-'].update("{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(player.get_time()//1000, 60),
                                                                             *divmod(player.get_length()//1000, 60)))
            else:

                window['-MESSAGE_AREA-'].update('Load media to start' if media_list.count() == 0 else 'Ready to play media' )

        window.close()
    
    if(event == sg.WIN_CLOSED):
        break
