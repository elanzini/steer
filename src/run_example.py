from steer_utils import run_steerscript_with_openai

steer_filename = "examples/gcd.steer"
input_data = {
    "a": 42,
    "b": 24
}

run_steerscript_with_openai(steer_filename, input_data)
