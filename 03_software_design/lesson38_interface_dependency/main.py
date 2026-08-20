class Detector:
    def detect(self, image):
        pass

class YOLODetector(Detector):
    def detect(self, image):
        print("YOLO Detect")

class GroundingDINODetector(Detector):
    def detect(self, image):
        print("Grounding DINO Detect")

class Planner:
    def __init__(self, detector):
        self.detector = detector
    def run(self):
        self.detector.detect("image")

class LLM:
    def generate(self, prompt):
        pass

class Qwen(LLM):
    def generate(self, prompt):
        print("Qwen Output")

class Llama(LLM):
    def generate(self, prompt):
        print("Llama Output")

class Agent:
    def __init__(self, llm):
        self.llm = llm
    def run(self):
        self.llm.generate("prompt")