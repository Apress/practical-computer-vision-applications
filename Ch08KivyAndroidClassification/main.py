import kivy.app
import Fruits

class FirstApp(kivy.app.App):
    def classify_image(self):
        img_path = self.root.ids["img"].source

        img_features = Fruits.extract_features(img_path)

        predicted_class = Fruits.predict_output("weights.npy", img_features, activation="sigmoid")

        self.root.ids["label"].text = "Predicted Class : " + predicted_class

firstApp = FirstApp(title="Fruits 360 Recognition.")
firstApp.run()

