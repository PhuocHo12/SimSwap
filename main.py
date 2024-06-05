from predict import Predictor
from pathlib import Path
swap_model = Predictor()
source_path = Path("/home/pc/Desktop/Documents/Project/SimSwap/4de18d9a941e75402c0f.jpg")
target_path = "/home/pc/Desktop/Documents/Project/SimSwap/videoplayback.mp4"
out_path = swap_model.predict(source= source_path,
                   target=target_path)
print(out_path)