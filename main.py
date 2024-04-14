import cv2
import glob
import time
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob("assets/*.jpg")
while True:
    for img_path in images_folder:
        img = cv2.imread(img_path)
        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)
        run_time = vehicle_count
        for box in vehicle_boxes:
            x, y, w, h = box
            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
            cv2.putText(img, "Time: " + str(run_time), (20, 200), 0, 2, (0, 250, 200), 3)

        cv2.imshow("Cars", img)
        cv2.waitKey(1)

        print("Green")
        time.sleep(run_time)
        print("Red-current lane")
