from app.llm.llm import generate_response


user_text = "ગુજરાતમાં સૌથી વધુ બોલાતી ભાષા કઈ છે?"

response = generate_response(user_text)

print("\n--- LLM RESULT ---")
print(response)