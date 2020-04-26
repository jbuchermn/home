Smart Home Config

Google Assistant
  + First, download client credentials and activate: 
    google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --save --headless --client-secrets /path/to/client_secret_client-id.json
  + Second, register device:
    googlesamples-assistant-pushtotalk --project-id home2-2d703 --device-model-id home2-2d703-python-endpoint-ofud5y
  + Doesn't work...
    python3 textinput.py --device-model-id home2-2d703-python-endpoint-ofud5y --verbose --device-id 8527c7aa-87e0-11ea-aa1f-9801a7a2d29d
  
