from google import genai

client = genai.Client(api_key="AIzaSyB_ZzFPFGBYnjDdo-29tu8X3b_orUHDx6U")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how many countries in the world"
)
print(response.text)