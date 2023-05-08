import openai
from antlr4 import FileStream, CommonTokenStream
from antlr.steerLexer import steerLexer
from antlr.steerParser import steerParser
import os

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


def validate_steerscript(steer_filename):
    print("Validating steer script with ANTLR")
    input_stream = FileStream(steer_filename)
    lexer = steerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = steerParser(token_stream)

    # Start parsing from the 'program' rule
    parser.program()

    # Check for syntax errors
    if parser.getNumberOfSyntaxErrors() == 0:
        print("Parsing completed successfully!")
        return True
    else:
        print(
            f"Parsing completed with {parser.getNumberOfSyntaxErrors()} syntax errors.")
        return False


def generate_system_prompt(steer_filename):
    # Validate the steer file
    if not validate_steerscript(steer_filename):
        print("Invalid steer file")
        exit()

    # Load Steer script from file
    with open(steer_filename, 'r') as f:
        steer_script = f.read()

    # Load prompt template from file and substitute placeholders
    with open('src/steer.prompt', 'r') as f:
        system_prompt = f.read().format(instructions=steer_script)

    return {
        "role": "system",
        "content": system_prompt
    }


def generate_input_prompt(input_data):
    return {
        "role": "user",
        "content": f"input_data = {input_data}\nmain(input_data)"
    }


def run_steerscript_with_openai(steer_filename, input_data):
    # Initialize OpenAI API
    openai.api_key = OPENAI_API_KEY

    # Generate the prompt
    system_prompt = generate_system_prompt(steer_filename)
    input_prompt = generate_input_prompt(input_data)

    instructions = [system_prompt, input_prompt]

    # Send the request to OpenAI API
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature=0.0,
        messages=instructions
    )

    print("\nModel output:")
    print(completion.choices[0].message.content)
