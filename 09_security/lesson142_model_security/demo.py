from backdoor_simulation import (
    ToyModel
)


model = ToyModel()


normal_output = model.predict(
    "Summarize the report."
)

triggered_output = model.predict(
    "Summarize [SPECIAL_TRIGGER]"
)


print(
    "Normal:",
    normal_output
)

print(
    "Triggered:",
    triggered_output
)


from integrity_check import (
    verify_hash
)


expected_hash = (
    "replace_with_known_hash"
)


valid = verify_hash(
    "example_model.bin",
    expected_hash
)


print(
    "Artifact verified:",
    valid
)