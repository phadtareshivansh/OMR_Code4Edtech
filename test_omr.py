# test_omr.py
import json
from omr_evaluator import evaluate_image

img = "omr1.jpg"   # <-- replace with your actual image filename
keyfile = "sample_answer_key.json"

with open(keyfile, "r") as f:
    keys = json.load(f)

key_name = "Set A" if "Set A" in keys else list(keys.keys())[0]
answer_key = keys[key_name]

# evaluate_image returns (result_dict, overlay_img)
res = evaluate_image(img, answer_key, save_overlay_path="overlay_test.jpg")
if isinstance(res, tuple) and len(res) == 2:
    res_dict, overlay = res
else:
    res_dict = res
    overlay = None

print("Total:", res_dict["total_score"])
print("Per-subject:", res_dict["per_subject"])