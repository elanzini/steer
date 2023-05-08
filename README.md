# Steer

Steer is a high-level pseudocode language designed to guide LLMs in performing tasks based on user input. It is specifically designed for users to interact with language models and instruct them to perform operations.

The grammar includes basic control flow operators, for / while loops, variable and function declaration.

It also includes some functionalities designed for LLM interaction:

- `ai`: explain what you want to do in a sentence and pass inputs
- `extract`: used to extract information from the input
- `write`: used to include strings in the final output of the model

**Tip**: it's best to use `write` as you would `log` something. This makes the model "think out loud", improving the accuracy of the results.

## Example script:

```
function gcd(a, b):
    return ai(`find the greatest common divisor between {a} and {b}`)

function main(input_data):
    print("Extracting information from the input data")
    a = extract(input_data, 'a')
    b = extract(input_data, 'b')
    print("Computing the gcd of a and b")
    result = gcd(a, b)
    print(`The gcd is {a}`)
```

## Getting Started

- Create a python venv (`python3 -m venv venv`) and install the deps (`pip3 install -r requirements.txt`)
- Set your `OPENAI_API_KEY` as an env variable.

To generate the lexer, parser, and listener files from the grammar, run the following command:

`antlr4 -Dlanguage=Python3 antlr/steer.g4 -o src/`

You can now create your `.steer` script (see `examples` folder for examples).

Look at `run_example.py` to see how to use the `steer_utils` to run your steer file.

You can run the example with: `python3 src/run_example.py`

You should expect to see this:

```
Validating steer script with ANTLR
Parsing completed successfully!

Model output:
Extracting information from the input data
Computing the gcd of a and b
The gcd is 6
```

## Project Structure

The project is structured as follows:

- `antlr/`: Contains the ANTLR grammar file for Steer language (`steer.g4`).
- `examples/`: Contains example Steer programs.
- `src/`: Contains the source code for parsing and running Steer programs, along with any utility or helper files.

## Contributions

Contributions are welcomed, feel free to open issues and create PRs.
