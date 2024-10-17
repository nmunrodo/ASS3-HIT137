import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Pre-trained MobileNetV2 model for image classification
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Class to handle image processing
class ImageProcessor:
    @staticmethod  # Static method as it doesn't rely on class instance
    def preprocess_image(image_path):
        # Load and preprocess image (method overriding happens here)
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        return img_array

# Main Tkinter Application Class with OOP concepts
class ImageClassificationApp(tk.Tk, ImageProcessor):
    def __init__(self):
        super().__init__()  # Call to the base class initializer (Tk)
        self.title("Image Classification App")
        self.geometry("500x400")
        self._init_widgets()  # Encapsulation in action

    def _init_widgets(self):
        # Encapsulation: Widgets are kept private within this method
        self.label = tk.Label(self, text="Image Classification App", font=("Arial", 16))
        self.label.pack(pady=20)

        self.upload_btn = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        self.result_label = tk.Label(self, text="Result will be shown here.", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.image_label = None

    def upload_image(self):
        # Polymorphism (file dialog varies depending on system)
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpeg *.png")])
        if image_path:
            self.show_image(image_path)
            self.classify_image(image_path)

    def show_image(self, image_path):
        # Method for displaying image
        img = Image.open(image_path)
        img.thumbnail((200, 200))  # Resize image
        img_tk = ImageTk.PhotoImage(img)
        if self.image_label:
            self.image_label.destroy()  # Overriding: destroying old image_label
        self.image_label = tk.Label(self, image=img_tk)
        self.image_label.image = img_tk  # Keep reference
        self.image_label.pack(pady=10)

    def classify_image(self, image_path):
        # Decorator for showing classification result
        @self.classification_result_decorator
        def run_classification(image_path):
            img_array = self.preprocess_image(image_path)  # Using static method from ImageProcessor
            predictions = model.predict(img_array)
            decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
            label = decoded_preds[0][0][1]  # Get label of top prediction
            return label

        result = run_classification(image_path)  # Call the function
        self.result_label.config(text=f"Prediction: {result}")

    # Multiple inheritance: Using method overriding from multiple parents
    def classification_result_decorator(self, func):
        def wrapper(image_path):
            # Pre-processing or result handling can be added here
            result = func(image_path)
            messagebox.showinfo("Classification Result", f"Predicted Class: {result}")
            return result
        return wrapper

# Multiple inheritance: Tk as main window and ImageProcessor for image handling
class AdvancedImageApp(ImageClassificationApp):
    def __init__(self):
        # Multiple inheritance
        super().__init__()

    # Method overriding: Customized welcome label
    def _init_widgets(self):
        super()._init_widgets()  # Call parent method and override
        self.label.config(text="Advanced Image Classification App", font=("Arial", 18))

# Run the application
if __name__ == "__main__":
    app = AdvancedImageApp()  # Polymorphism: Using advanced class
    app.mainloop()

