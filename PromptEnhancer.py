from openai import OpenAI

client = OpenAI(api_key=api_key)

# 2. Define the Prompt Engineering Logic
# This instruction tells the AI how to transform the user's input.
system_instruction = """
You are a Prompt Engineering Expert. 
Your task is to take a raw, simple, or poorly phrased prompt from the user and rewrite it into a "Pro Prompt".
The Pro Prompt should be clear, professional, and provide enough context for an AI to give a high-quality response.

Format your output exactly like this:
Pro Prompt : [Your enhanced prompt here]
"""

print("--- Prompt Enhancer Tool ---")
print("Type 'quit' to exit.")

while True:
    # 3. Get User Input
    user_input = input("\nEnter Your Prompt : ").strip()

    # Check for exit condition
    if user_input.lower() == "quit":
        print("Exiting Enhancer...")
        break
    
    # Skip empty inputs
    if not user_input:
        continue

    try:
        # 4. Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-5.2", # You can also use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )

        # 5. Extract and Print the Result
        pro_prompt = response.choices[0].message.content
        print(pro_prompt)

    except Exception as e:
        print(f"An error occurred: {e}")
        break
