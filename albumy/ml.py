# -*- coding: utf-8 -*-
"""
    :author: Romina Gotzmann
    :copyright: © 2025 Romina Gotzmann <rgotzmann2017@fau.edu>
    :license: MIT, see LICENSE for more details.
"""

from PIL import Image
from transformers import pipeline

print("Loading ML models")
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
print("ML models successfully loaded")

OBJECTS = [
        "person", "people", "dog", "cat", "animal",
        "food", "nature", "landscape", "car", "building",
        "beach", "ocean", "sunset", "flower", "tree",
        "city", "indoor", "outdoor"
        ]

def analyze_image(image_path):
    try:
        image = Image.open(image_path).convert('RGB')

        alt_text = captioner(image)[0]['generated_text']

        # detect top three objects with confidence > 30%
        results = classifier(image, candidate_labels=OBJECTS)
        objects = [r['label'] for r in results if r['score'] > 0.3][:3]

        return alt_text, ','.join(objects) if objects else 'image'

    except Exception as e:
        print(f"ML Error: {e}")
        return "Image", "image"
