import tkinter as tk
import threading
import pyzed.sl as sl
import cv2


class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.left_camera_btn = tk.Button(window, text="Open Left Camera", width=20, command=self.open_left_camera)
        self.right_camera_btn = tk.Button(window, text="Open Right Camera", width=20, command=self.open_right_camera)
        self.quit_btn = tk.Button(window, text="Quit", width=10, command=self.quit_app)

        self.left_camera_btn.pack(padx=10, pady=5)
        self.right_camera_btn.pack(padx=10, pady=5)
        self.quit_btn.pack(padx=10, pady=5)

        self.camera_open = False
        self.current_camera = None
        self.mutex = threading.Lock()
        self.camera_thread = None

    def open_left_camera(self):
        self.start_camera("left")

    def open_right_camera(self):
        self.start_camera("right")

    def quit_app(self):
        self.window.quit()
        if self.camera_thread:
            self.camera_open = False
            self.camera_thread.join()

    def start_camera(self, camera):
        if self.camera_open:
            return

        self.current_camera = camera
        self.camera_open = True
        self.camera_thread = threading.Thread(target=self.capture_camera)
        self.camera_thread.start()

    def capture_camera(self):
        init_params = sl.InitParameters()
        init_params.camera_resolution = sl.RESOLUTION.HD720
        init_params.camera_fps = 30

        zed = sl.Camera()
        try:
            if not zed.is_opened():
                print(f"Opening {self.current_camera.capitalize()} Camera...")
            status = zed.open(init_params)
            if status != sl.ERROR_CODE.SUCCESS:
                print(repr(status))
                return

            runtime_parameters = sl.RuntimeParameters()
            while self.camera_open:
                if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                    if self.current_camera == "left":
                        image_view = sl.VIEW.LEFT
                    else:
                        image_view = sl.VIEW.RIGHT

                    left_image = sl.Mat()
                    zed.retrieve_image(left_image, image_view)

                    left_image_opencv = left_image.get_data()
                    cv2.imshow(f"{self.current_camera.capitalize()} Camera", left_image_opencv)

                    key = cv2.waitKey(1)
                    if key == ord('q'):
                        break
        finally:
            zed.close()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root, "Camera Control")
    root.mainloop()