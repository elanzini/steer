# Steer: Enhancing Control Flow and Steerability for Large Language Models

Even after following [every](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api) [possible](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) [course](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) on [prompt engineering](https://www.promptingguide.ai/) I could find, I still had a hard time getting the model do what I wanted to. Below is a summary of what I found to be the most helpful:

- Be **clear** and **concise** in your instructions.
- Tell the model what to do, **not** what not to do. Simply replacing `Don't` with `Refrain from` can already make a huge difference.
- Break down the task **step by step** as if you are actually doing the task and logging every action that you take to get the the answer.
- Make the model **think out loud**, use `<ai></ai>` tags to leave a trail of thought for the model to follow. Since it's just trying to predict what comes next, it will be less likely to contradict itself.
- **Format** your instructions and input/output. Try to give some structure to your prompt, using markdown and format input and output to make it easier for the model. Use JSON or anything you fancy.

Despite applying all of these tricks, the model was still not sticking to the instructions given. The issue becomes more apparent when the model is tasked to follow a flow control, such as checking conditions and making decisions based on those conditions.

The more I tweaked my prompt, the more it started to look like code. That's when I realized the best way to handle flow and steerability is to write pseudocode and ask the model to simply execute the given instructions.

That's why I created a grammar for a new language, called Steer designed to make it easier to control large language models.

Steer is a high-level pseudocode language designed to guide LLMs in performing tasks based on user input. It is specifically designed for users to interact with language models and instruct them to perform operations.

On top of the usual basic control flow operators, loops, variable and function declaration, Steer includes some functionalities tailored for LLM interaction:

- `ai`: takes a sentence describing a task and any necessary inputs, then performs the task using the LLM and returns the result.
- `extract`: takes an input text and a specific piece of information to be extracted, then returns the extracted information from the input.
- `write`: takes a string as input and appends it to the final output of the model, allowing for the gradual construction of the response while maintaining a clear line of thought.

Other functionalities that have not been implemented yet are:

- `answer`: takes a text input, a question, and optionally an answer format, then returns the answer to the question based on the input text.
- `assert`: takes an expression or statement and evaluates its correctness or validity, useful for tasks like code review or fact-checking.
- `generate`: takes a set of input parameters, such as a topic or a list of keywords, and generates new content based on those inputs.

The model is fed description of these functionalities so that you can use them out of the box.

An example code written in Steer looks like this:

```steer
function gcd(a, b):
    return ai(`find the greatest common divisor between {a} and {b}`)

function main(input_data):
    write("Extracting information from the input data")
    a = extract(input_data, 'a')
    b = extract(input_data, 'b')
    write("Computing the gcd of a and b")
    result = gcd(a, b)
    write(`The gcd is {a}`)
```

In the repository, there is a `steer.g4` file defining the grammar of the language with docs on how to parse steer files locally and use them with OpenAI API.

This is just a pet project that I enjoyed playing with. Feel free to contribute to the project and play with it [here](https://github.com/elanzini/steer).
