import os
import base64
from datetime import datetime
from openai import OpenAI

client = OpenAI()

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

IMAGE_DIR = os.path.join(
    ROOT_DIR,
    "generated_images"
)

os.makedirs(
    IMAGE_DIR,
    exist_ok=True
)

def should_handle(message: str) -> bool:

    text = message.lower()

    triggers = [
        "pixie",
        "picture",
        "image",
        "create image",
        "generate image",
        "make an image",
        "draw",
        "poster",
        "map poster",
        "visual",
        "diagram"
    ]

    return any(
        t in text
        for t in triggers
    )

def clean_prompt(message: str) -> str:

    prompt = message.strip()

    prompt = prompt.replace(
        "Pixie",
        ""
    ).replace(
        "pixie",
        ""
    )

    prompt = prompt.replace(
        "create image",
        ""
    ).replace(
        "generate image",
        ""
    ).replace(
        "make an image",
        ""
    )

    prompt = prompt.strip()

    if not prompt:

        prompt = (
            "Create a calm, clear, ADHD-friendly visual memory "
            "anchor poster in Shine style."
        )

    return prompt

def create_image(message: str):

    prompt = clean_prompt(message)

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_b64 = response.data[0].b64_json

    filename = (
        "pixie_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".png"
    )

    path = os.path.join(
        IMAGE_DIR,
        filename
    )

    with open(path, "wb") as f:

        f.write(
            base64.b64decode(
                image_b64
            )
        )

    return {
        "reply": (
            "# 🎨 Pixie Pictures\n\n"
            "Image created successfully.\n\n"
            "Prompt used:\n"
            + prompt
        ),
        "image_url": "/generated_images/" + filename
    }
