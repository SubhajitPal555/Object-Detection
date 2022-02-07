from threading import Thread
import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib
Gst.init()
main_loop = GLib.MainLoop()
thread = Thread(target=main_loop.run)
thread.start()
#pipeline = Gst.parse_launch("rtspsrc location=rtsp://admin:12345@192.168.0.198:8000/h264_ulaw.sdp latency=10 buffer-mode=auto ! rtph264depay ! h264parse ! rtph264pay name=pay0 pt=96 ! decodebin ! videoconvert ! videoscale ! video/x-raw,width=480,height=320 ! videoconvert ! autovideosink")
pipeline = Gst.parse_launch("rtspsrc location=rtsp://admin:12345@192.168.0.198:8000/h264_ulaw.sdp latency=0 buffer-mode=auto ! queue ! rtph265depay ! h265parse ! avdec_h265 ! decodebin ! videoconvert ! videoscale ! video/x-raw,width=1280,height=720 ! autovideosink") #This is for rtsp ip camera 
#pipeline = Gst.parse_launch("v4l2src ! videoconvert ! videoscale ! video/x-raw,width=640,height=480 ! videoconvert ! autovideosink") #This is for web camera 
pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
