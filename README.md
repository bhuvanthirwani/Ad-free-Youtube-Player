# Ad-free YouTube Player

<p>YouTube is a widely used online platform which streams videos as asked by the user. After the input given by the user, it shows a list of videos from most relevant to least
relevant. Our model aims to integrate this task with the Vision as well as Audition modalities, that is, user can search using keyboard or through voice, and hence can stream ad-free videos. We have implemented this approach by building an interactive GUI application to play the requested video.<br></p>

<p>The novelty of our proposed project is that the user need not open the YouTube platform explicitly. The GUI Application provides advertisement free streaming and an option to download the loaded video. These additional features help enhance the user experience further.</p>

## GUI Application
<p>A Python GUI application is like a VLC player for YouTube running in pip mode. It can be minimized, maximized or run in movie mode just like YouTube. Also, the GUI application will have most of the functionalities just like the one in YouTube. As a general flow, when the GUI application is started, it asks for the user’s choice, if he/she wants to interact with ”Voice” or ”Mouse”. Then, according to the preference given, it provides an ad-free streaming of the YouTube videos.</p>

### Mouse Based
<p>When the user opts for a Mouse Based interface, he/she needs to type the query in the search box. Clicking on <em>load</em> button will open the most relevant video related to the search term within the application. The model obtains the YouTube link of this relevant video through the process of Web Scraping. It is the process of extracting content and data from a website. We have used the concept of regular expressions in order to implement this process.</p>
<p>After getting the URL of the requested video, the model loads the video on the application and makes it ready to be controlled by the user. Now, the user can perform various clicks shown on the application in order to control the video:<br>
  1. <em>Play</em>: plays the video.<br>
  2. <em>Pause</em>: pauses the video.<br>
  3. <em>Mute</em>: mutes the video or makes its volume 0.<br>
  4. <em>Subtitles</em>: enables subtitles for the video if they are present.<br>
  5. <em>Stop</em>: stops the video and exits the interface.<br>
  6. <em>Download</em>: downloads the video.<br></p>
<p>Apart from these, the user can control the size of the video by choosing the Full screen (shown by maximise button) or Minimise screen (shown by minimise button) or Normal screen (restores the original size) or Cancel screen (shown by cross mark) options from the Title bar of the application.</p>

### Voice Based
<p>When the user opts for a Voice Based interface, he/she needs to give the search term, for example train, by saying <em>search train</em>. The model confirms the voice command by saying <em>I heard train</em>. It then performs Web Scraping at the back-end similar to the Mouse-based approach. It extracts and loads the link of the most relevant video related to the search term on the application. Now, the user can control the video through various voice commands listed below:<br>
  1. <em>Play</em>: plays the video.<br>
  2. <em>Pause</em>: pauses the video.<br>
  3. <em>Mute</em>: mutes the video or makes its volume 0.<br>
  4. <em>Unmute</em>: unmutes the video.<br>
  5. <em>Subtitles</em>: enables subtitles for the video if they are present.<br>
  6. <em>Full Screen</em>: continues commands in full screen.<br>
  7. <em>Minimise</em>: continues commands in mini version.<br>
  8. <em>Normal</em>: restores original size and continue commands.<br>
  9. <em>Download</em>: downloads the video.<br>
  10. <em>Exit</em>: stops the video and exits the interface.<br>
