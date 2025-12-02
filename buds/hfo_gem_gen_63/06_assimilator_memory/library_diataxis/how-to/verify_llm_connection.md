---
holon:
  id: 9a73b680-a7c9-4182-9ce2-6c87abbfe55c
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/verify_llm.py
hexagon:
  ontos: <owner>
  logos: diataxis
---

# How to Verify OpenRouter Connection

## Overview
This document provides step-by-step instructions for verifying the connection to the OpenRouter API, which is essential for utilizing the functionalities of the language model.

## Why Verify the OpenRouter Connection?
Verifying the OpenRouter connection is crucial because it ensures that your API key is set up correctly and that your application can communicate with the OpenRouter service. If the connection is not established properly, the application will not be able to access the AI model for generating responses, which is fundamental for operations requiring natural language processing.

## Steps to Verify the OpenRouter Connection
1. **Import Required Libraries**: Make sure to import the necessary libraries at the beginning of your script:
   ```python
   import os
   import sys
   from openai import OpenAI
   ```

2. **Configure Path for Imports**: Add the root directory to your system path to import settings from your configuration:
   ```python
   sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
   from src.config import settings
   ```

3. **Define the Verification Function**: Create a function named `verify_llm()` that will handle the verification process:
   ```python
   def verify_llm():
       """Verify OpenRouter Connection."""
   ```

4. **Check API Key**: Inside the function, retrieve the API key from your settings. If it's not found, attempt to get it from the environment variables:
   ```python
   api_key = settings.OPENROUTER_API_KEY
   if not api_key:
       api_key = os.environ.get("OPENROUTER_API_KEY")
   ```

5. **Handle Missing API Key**: If the API key is still not found, print an error message and exit:
   ```python
   if not api_key:
       print("❌ Verification FAILED: OPENROUTER_API_KEY not found in settings or environment.")
       return
   ```

6. **Initialize OpenAI Client**: If the API key is found, initialize the OpenAI client with the correct base URL and API key:
   ```python
   client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key=api_key,
   )
   ```

7. **Send a Test Request**: Use the client to create a test chat completion request:
   ```python
   completion = client.chat.completions.create(
       model=settings.OPENROUTER_MODEL,
       messages=[
           {
               "role": "user",
               "content": "Are you online? Reply with 'I am the Obsidian Spider'."
           }
       ]
   )
   ```

8. **Process the Response**: Extract the response and validate whether it contains the expected content:
   ```python
   response = completion.choices[0].message.content
   if "Obsidian Spider" in response:
        print("✅ Verification SUCCESS: LLM is responsive.")
   else:
        print("⚠️ Verification WARNING: Response received but content unexpected.")
   ```

9. **Handle Exceptions**: Wrap the API call in a try-except block to catch and print any errors that may occur during verification:
   ```python
   except Exception as e:
       print(f"❌ Verification FAILED: {e}")
   ```

10. **Run the Verification**: Finally, include a main guard to execute the `verify_llm()` function when the script is executed:
   ```python
   if __name__ == "__main__":
       verify_llm()
   ```

Following these steps ensures that your OpenRouter connection is properly verified, allowing for successful interaction with the language model.