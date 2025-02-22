import os
from tracker import Tracker

mqtt_address = os.environ.get("MQTT_ADDRESS", "10.1.1.100")
mqtt_port = int(os.environ.get("MQTT_PORT", 1883))
mqtt_username = os.environ.get("MQTT_USERNAME", "username")
mqtt_passwd = os.environ.get("MQTT_PASSWD", "password")
mqtt_client_id = os.environ.get("MQTT_CLIENT_ID", "cvzone_tracker_01")
min_face_score = float(os.environ.get("MIN_FACE_SCORE", 0.5))
rotate_img = int(os.environ.get("ROTATE_IMAGE", 0))

tracker = Tracker(
    mqtt_address=mqtt_address,
    mqtt_port=mqtt_port,
    mqtt_passwd=mqtt_passwd,
    mqtt_username=mqtt_username,
    mqtt_client_id=mqtt_client_id,
    min_face_score=min_face_score,
    rotate_img=rotate_img == 1,
    show_img=True)

while True:
    tracker.loop()

tracker.release()
