# Abdul Rafay - BSCS23031

# PDC-Sp24-BSCS23031-Rafay

Distributed Systems Assignment for Parallel and Distributed Computing (PDC).

This project analyzes and fixes a distributed systems synchronization issue in a FastAPI-based application inspired by the SecureAIApp architecture from Tech With Tim.

---

# Problem Implemented

## Synchronization / Lost Update Problem

When two users edit the same shared document simultaneously, one update can silently overwrite the other.

This project fixes the issue using:

* Optimistic Locking
* Version-based conflict detection
* HTTP 409 Conflict responses

---

# Implemented Distributed Systems Concepts

## Optimistic Locking

Each document contains a version number.

During updates:

1. Client sends document version.
2. Backend checks current version.
3. If versions mismatch:

   * update rejected
   * HTTP 409 returned

This prevents lost updates.

---

# Additional Requirement Implemented

## Custom Middleware Header

Every API response includes:

```text
X-Student-ID: BSCS23031
```

---

# Project Structure

```text
backend/
├── src/
│   ├── app.py
│   ├── ai_generator.py
│   └── routes/
│       ├── challenge.py
│       ├── webhooks.py
│       └── document.py
│
├── test_conflict.py
└── README.md
```

---

# How To Run

## 1. Clone Repository

```bash
git clone <YOUR_GITHUB_REPO_LINK>
cd PDC-Sp24-BSCS23031-Rafay
```

---

## 2. Install Dependencies

```bash
pip install fastapi uvicorn requests
```

---

## 3. Start FastAPI Server

```bash
uvicorn backend.src.app:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

Swagger API docs:

```text
http://127.0.0.1:8000/docs
```

---

# Optimistic Locking Endpoints

## Get Shared Document

### GET

```text
/document
```

Returns:

```json
{
  "id": 1,
  "content": "Initial text",
  "version": 1
}
```

---

## Update Shared Document

### PUT

```text
/document
```

Request:

```json
{
  "content": "Updated text",
  "version": 1
}
```

If versions match:

```json
{
  "message": "Document updated successfully"
}
```

If versions mismatch:

```json
{
  "detail": "Version conflict detected"
}
```

Status code:

```text
409 Conflict
```

---

# Running the Conflict Simulation Test

Open a second terminal while FastAPI server is running.

Run:

```bash
python test_conflict.py
```

Expected Result:

```text
User A:
200

User B:
409
```

One update succeeds while the conflicting update is rejected.

This demonstrates prevention of the Lost Update anomaly.

---

# Distributed Systems Problems Analyzed

The report also analyzes:

1. Synchronization Problems

   * Lost updates
   * Concurrent writes

2. Coordination Problems

   * Dropped Clerk webhooks
   * Permanent state inconsistency

3. Fault Tolerance Problems

   * Synchronous LLM API blocking
   * Single point of failure

---

# Proposed Architectural Improvements

## Synchronization

* Optimistic locking
* Version control
* Conflict detection

## Coordination

* Reliable webhook retries
* Idempotency keys
* Dead-letter queues

## Fault Tolerance

* Circuit breaker pattern
* Fallback responses
* Async request handling

---

# CAP Theorem Trade-offs

## Synchronization

Prioritizes:

* Consistency over Availability

Conflicting updates are rejected instead of risking corrupted data.

---

## Webhooks

Prioritizes:

* Availability and Eventual Consistency

Retries restore synchronization later.

---

## Circuit Breaker

Prioritizes:

* Availability and Low Latency

Fallback responses are returned quickly instead of waiting for external AI failures.

---

# Demo Video

The demo video demonstrates:

1. Concurrent update problem
2. Lost update prevention
3. Optimistic locking behavior
4. HTTP 409 conflict handling

---

# Technologies Used

* Python
* FastAPI
* Uvicorn
* REST APIs
* Threading
* Distributed Systems Concepts

---

# Author

Abdul Rafay
BSCS23031
