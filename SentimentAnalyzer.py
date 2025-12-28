from openai import OpenAI

client = OpenAI(api_key=api_key)

# 2. Define the System Instruction
# This tells the AI how to behave and forces the emoji output.
system_instruction = """
You are a sentiment analyzer. 
Classify the user's input as 'positive', 'neutral', or 'negative'.
Always add a matching emoji after the classification (e.g., 😞 for negative, 😃 for positive).
Output ONLY the classification and the emoji.
"""
try:
    while True:
        # 3. Get User Input
        user_review = input("Enter User Review : ")
    
        # Allow user to exit
        if user_review.lower() == "quit":
            print("Exiting...")
            break
    
        # 4. Call the API
        response = client.chat.completions.create(model="gpt-5.2",
                messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_review}
            ],
            temperature=0 # Low temperature makes the output more deterministic/consistent
        )
    
        # 5. Print Output
        result = response.choices[0].message.content
        print(f"Output : {result}")
        print("-" * 30)

except Exception as e:
    print('Error:',e)
