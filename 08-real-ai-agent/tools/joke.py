import random

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did Python go to therapy? It had too many unresolved imports.",
    "Debugging: Being the detective in a crime movie where you're also the murderer."
]


def random_joke():
    return random.choice(JOKES)