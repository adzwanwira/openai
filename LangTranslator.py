from openai import OpenAI

client = OpenAI(api_key=api_key)

# 2. Define the System Instruction
system_instruction = """
You are a professional language translator. 
The user will provide a text and a target language. 
Translate the text accurately. 
Output ONLY the translated text. Do not provide explanations or quotes.
"""

print("--- Language Translator ---")
print("Type 'quit' at any prompt to exit.")

while True:
    # 3. Get User Inputs
    source_text = input("\nInput (Text to translate) : ").strip()
    if source_text.lower() == "quit": break
    
    target_lang = input("To language (e.g., English, French) : ").strip()
    if target_lang.lower() == "quit": break

    if not source_text or not target_lang:
        print("Please provide both text and a target language.")
        continue

    try:
        # 4. Call OpenAI API
        # We combine the inputs into a clear request for the AI
        user_prompt = f"Translate the following text to {target_lang}: {source_text}"
        
        response = client.chat.completions.create(
            model="gpt-5.2", 
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )

        # 5. Output result
        translation = response.choices[0].message.content
        print(f"Output : {translation}")

    except Exception as e:
        print(f"An error occurred: {e}")
        break
