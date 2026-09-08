MODEL_RISKS = {
    "backdoor": {
        "security_goal":
            "integrity",

        "impact":
            "conditional malicious behavior"
    },

    "training_poisoning": {
        "security_goal":
            "integrity",

        "impact":
            "corrupted learned behavior"
    },

    "model_theft": {
        "security_goal":
            "confidentiality",

        "impact":
            "loss of model IP"
    },

    "membership_inference": {
        "security_goal":
            "privacy",

        "impact":
            "training membership disclosure"
    },

    "resource_abuse": {
        "security_goal":
            "availability",

        "impact":
            "compute exhaustion"
    }
}