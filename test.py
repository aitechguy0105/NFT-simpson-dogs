import requests
import json

url = "https://modelslab.com/api/v5/controlnet"

payload = json.dumps({
    "key": "Rr4zRlJRJes7ToWf65vTKzu1ijjDIFlhV18Yy87Sl6K01Y2hbDFhzZW2rkrE",
    "controlnet_type": "canny",
    "controlnet_model": "canny",
    "model_id": "midjourney",
    "init_image": "https://raw.githubusercontent.com/aitechguy0105/NFT-simpson-dogs/main/white-dog.jpg",
    "ip_adapter_id": "ip-adapter_sd15",
    "mask_image": None,
    "control_image": None,
    "auto_hint":"yes",
    "width": "512",
    "height": "512",
    "prompt": "simpson image of this dog",
    "negative_prompt": "human",
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