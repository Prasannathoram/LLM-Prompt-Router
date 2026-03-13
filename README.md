
---

# LLM-Powered Prompt Router for Intent Classification

## Project Overview

This project implements an **LLM-powered prompt routing system** that intelligently detects a user's intent and routes the request to a specialized AI persona. Instead of using a single large prompt for all tasks, the system uses a **two-stage architecture**:

1. **Intent Classification** – A lightweight LLM call classifies the user's intent.
2. **Prompt Routing** – Based on the detected intent, the system routes the request to a specialized expert prompt.

This architecture improves response quality by allowing each persona to focus on a specific domain such as coding, writing improvement, data analysis, or career advice.

The application is containerized using **Docker** and logs all routing decisions and responses to a **JSON Lines log file** for observability.

---

# Architecture

The system follows a **two-step LLM pipeline**.

```
User Message
      ↓
Intent Classification (LLM Call #1)
      ↓
Intent Label + Confidence
      ↓
Prompt Router
      ↓
Select Expert Persona
      ↓
Response Generation (LLM Call #2)
      ↓
Final Response
      ↓
Log Entry (route_log.jsonl)
```

Supported intents:

```
code
data
writing
career
unclear
```

---

# Tech Stack

| Technology        | Purpose                                         |
| ----------------- | ----------------------------------------------- |
| Python            | Backend service implementation                  |
| Groq API          | LLM inference for classification and generation |
| OpenAI Python SDK | API client (Groq compatible endpoint)           |
| Docker            | Containerized deployment                        |
| JSON Lines        | Request logging                                 |
| dotenv            | Environment variable management                 |

---

# Project Structure

```
ai-prompt-router
│
├── app
│   ├── classifier.py       # Intent classification logic
│   ├── router.py           # Prompt routing and response generation
│   ├── prompts.py          # Expert persona system prompts
│   ├── logger.py           # JSONL logging utility
│   └── main.py             # CLI interface for interacting with the router
│
├── route_log.jsonl         # Log file for all routing decisions
├── Dockerfile              # Container build instructions
├── docker-compose.yml      # Container orchestration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
└── README.md
```

---

# Expert Personas

The system includes four specialized expert prompts:

### Code Expert

Provides programming solutions with clean code examples and technical explanations.

### Data Analyst

Interprets numerical data and suggests statistical insights and visualizations.

### Writing Coach

Provides feedback on clarity, tone, and grammar without rewriting the user's text.

### Career Advisor

Offers practical career guidance and asks clarifying questions before giving recommendations.

---

# Environment Setup

## 1. Clone the Repository

```
git clone <repository-url>
cd ai-prompt-router
```

---

## 2. Create `.env` File

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

You can obtain a free API key from:

```
https://console.groq.com/keys
```

---

# Running the Project with Docker

## Build the Docker Image

```
docker compose build
```

---

## Run the Application

```
docker compose run ai-router
```

You will see:

```
Enter message:
```

---

# Testing Guide

The following tests verify that the system correctly routes different user intents.

## Code Intent

Input:

```
how do i sort a list of objects in python?
```

Expected intent:

```
code
```

---

## Writing Intent

Input:

```
This paragraph sounds awkward, can you help me fix it?
```

Expected intent:

```
writing
```

---

## Career Intent

Input:

```
I'm preparing for a job interview, any tips?
```

Expected intent:

```
career
```

---

## Data Intent

Input:

```
what's the average of these numbers: 12, 45, 23, 67, 34
```

Expected intent:

```
data
```

---

## Unclear Intent

Input:

```
hey
```

Expected intent:

```
unclear
```

The system should respond with a clarification question.

---

# Ambiguous Input Testing

Example:

```
I need help writing a Python function and advice about my career.
```

This message contains multiple intents.
The classifier will select the **most likely intent** and route the request accordingly.

---

# Logging

All requests are logged to:

```
route_log.jsonl
```

Each log entry contains:

```
intent
confidence
user_message
final_response
timestamp
```

Example log entry:

```json
{
 "intent": "code",
 "confidence": 0.94,
 "user_message": "how do i sort a list in python?",
 "final_response": "...",
 "timestamp": "2026-03-09T10:20:41"
}
```

This provides traceability for routing decisions.

---

# Error Handling

The system includes safeguards for:

* malformed JSON responses from the LLM
* unsupported inputs
* low confidence classifications

If classification fails, the system safely defaults to:

```
intent = unclear
confidence = 0.0
```

---

# Key Features

* Intent classification using LLMs
* Prompt routing to specialized AI personas
* Two-stage LLM architecture
* Dockerized backend service
* JSONL logging for observability
* Robust error handling for malformed model responses

---

# Author

**Prasanna**

---


