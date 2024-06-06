from predict import Predictor
from pathlib import Path
swap_model = Predictor()
source_path = Path("/home/pc/Desktop/Documents/Project/SimSwap/demo_file/Iron_man.jpg")
# target_path = "/home/pc/Desktop/Documents/Project/SimSwap/videoplayback.mp4"
target_path = 0
out_path = swap_model.predict(source= source_path,
                   target=target_path)
