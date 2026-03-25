import random

templates = [
    "I'm going out, so {}",
    "Before I sleep, {}",
    "Can you please {}",
    "It's too hot, so {}",
    "I'm leaving home, {}"
]

actions = [
    "turn off all lights in bedroom",
    "switch on kitchen fan",
    "dim living room lights to 30%",
    "turn off AC",
    "close the curtains",
    "turn on balcony light",
    "switch off bathroom heater"
]

def build_prompt():
    num_cmds = random.randint(2, 4)
    selected = random.sample(actions, num_cmds)
    sentence = ", and ".join(selected)
    template = random.choice(templates)

    paragraph = template.format(sentence)

    return f"""
Generate smart home command dataset.

Paragraph:
{paragraph}

Convert into JSON list of actions.

Format:
Paragraph:
<text>

JSON:
<list>
"""