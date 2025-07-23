keep the client.py but also bring that client setup switch between gemini api key and vertex auth over to main.py
- have a cli option for enabling vertex 
- the default is to go with non-vertex ("Gemini-api") (gemini api is still default of GOOGLE_GENAI_USE_VERTEXAI=true in .env or in env vars, the only way to override is with cli args to main.py)