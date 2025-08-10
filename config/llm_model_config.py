from ollama import Client

def display_available_models(client):

    clientModels = client.list()

    print("\nAvailable models:")
    for idx, model in enumerate(clientModels['models']):
        # print available models
        print(f"[{idx}]: {model['model']}")

def fetch_model(client, modelIndex):

    clientModel = client.list()['models'][modelIndex]

    return clientModel

def fetch_response(client, myModel, myPrompt):

    response = client.chat(model=myModel, messages=[
        {"role": "user", "content": myPrompt}
    ])

    return response['message']['content']

    
if __name__ == "__main__":
    main()
