import requests
import json

url = "https://modelslab.com/api/v5/controlnet"

payload = json.dumps({
    "key": "",
    "controlnet_type": "canny",
    "controlnet_model": "canny",
    "model_id": "midjourney",
    "init_image": "https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",
    "mask_image": None,
    "control_image": None,
    "auto_hint":"yes",
    "width": "512",
    "height": "512",
    "prompt": " (a frog wearing blue jean), full-body, Ghibli style, Anime, vibrant colors, HDR, Enhance, ((plain black background)), masterpiece, highly detailed, 4k, HQ, separate colors, bright colors",
    "negative_prompt": "human, unstructure, (black object, white object), colorful background, nsfw",
    "guess_mode": None,
    "use_karras_sigmas": "yes",
    "algorithm_type": None,
    "safety_checker_type": None,
    "tomesd": "yes",
    "vae": None,
    "embeddings": None,
    "lora_strength": None,
    "upscale": None,
    "instant_response": None,
    "strength": 1,
    "guidance_scale": 7.5,
    "samples": "1",
    "safety_checker": None,
    "num_inference_steps": "30",
    "controlnet_conditioning_scale": 0.4,
    "track_id": None,
    "scheduler": "EulerDiscreteScheduler",
    "base64": None,
    "clip_skip": "1",
    "temp": None,
    "seed": None,
    "webhook": None
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)