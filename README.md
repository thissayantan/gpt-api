# GPT-API

This project integrates the OpenAI API with a FastAPI server to create a conversational AI system. It utilizes environment variables for API keys and includes routes for starting conversations and chatting with the AI.

## Installation

Before you start, make sure you have Python installed on your system.

1. Clone the repository:

```bash
git clone git@github.com:thissayantan/gpt-api.git
```

2. Navigate to the cloned directory:

```bash
cd gpt-api
```

3. Install the required packages:

```bash
poetry install
```

## Configuration

Create a `.env` file in the root of the project and set the `OPENAI_API_KEY` variable:

```env
OPENAI_API_KEY='your-openai-api-key'
```

## Running the Server

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables hot reloading during development.

## Usage

Once the server is running, you can interact with the API as follows:

- Send a GET request to the root (`/`) to verify that the server is running.
- Start a conversation with a GET request to `/start`. This will return a `thread_id`.
- Use the `thread_id` to chat with the AI by sending a POST request to `/chat` with a `DialogueSnippet` JSON object.

## Endpoints

- `GET /`: Root route that returns a welcome message.
- `GET /start`: Starts a new conversation thread with the AI.
- `POST /chat`: Sends a user's message to the AI and returns its response.

## Debugging

The code includes print statements for debugging purposes. These will show up in your terminal as you interact with the API.

## License

This project is licensed under MIT License. For more information, please see the [LICENSE](https://github.com/thissayantan/gpt-api/blob/main/LICENSE) file.