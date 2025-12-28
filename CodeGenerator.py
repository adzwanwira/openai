from openai import OpenAI

client = OpenAI(api_key=api_key)

# 2. Define the System Instruction
# This is crucial to ensure the output is just the code, as per your requirement.
system_instruction = """
You are an expert Python Programmer. 
When the user asks for a program, write the Python code in plain text.
Do not include any introductory text, explanations, or markdown code blocks (like ```python).
Just provide the raw, runnable code.
"""

print("--- Python Program Generator ---")
print("Type 'quit' to exit.")

while True:
    # 3. Get the Question from User
    user_question = input("\nQuestion : ").strip()

    # Check for exit condition
    if user_question.lower() == "quit":
        print("Closing Generator...")
        break
    
    if not user_question:
        continue

    try:
        # 4. Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-5.2", 
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_question}
            ],
            temperature=0  # Keeping it at 0 ensures stable, accurate code
        )

        # 5. Extract and Print the Result
        # We wrap the output in ''' to match your requested format
        code_output = response.choices[0].message.content
        print("Output : should be in a plain text")
        print(f"\n'''\n{code_output}\n'''")

    except Exception as e:
        print(f"An error occurred: {e}")
        break
