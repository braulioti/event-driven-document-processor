# Event-Driven Document Processor

Mini enterprise backend project built to simulate a modern corporate environment using event-driven architecture, cloud integrations, containerization, and observability concepts.

---

# Overview

This project demonstrates how modern backend systems work in real-world companies using:

- Event-driven communication
- Asynchronous processing
- Cloud-native concepts
- Structured logging
- Containerized services
- Monitoring and observability

The application receives document requests through a REST API, publishes events to Kafka, processes them asynchronously, stores generated files in S3, and exposes metrics for monitoring.

---

# Architecture

```text
Client
   ↓
FastAPI API
   ↓
Kafka Producer
   ↓
Kafka Topic
   ↓
Kafka Consumer
   ↓
Document Processing
   ↓
S3 Storage / Retry Queue
   ↓
Logs + Metrics
```

---

# Tech Stack

## Backend
- Python 3.12
- FastAPI
- Pydantic

## Messaging
- Apache Kafka
- Kafka Producer/Consumer

## Cloud
- AWS S3
- AWS SQS (simulated locally)
- LocalStack

## Infrastructure
- Docker
- Docker Compose

## Observability
- Structured JSON Logging
- Prometheus Metrics

---

# Features

## API
- REST API with FastAPI
- Healthcheck endpoint
- Metrics endpoint
- Request validation
- Structured error handling

## Event-Driven Architecture
- Kafka producer
- Kafka consumer
- Asynchronous processing
- Retry flow simulation

## Cloud Integrations
- S3 file upload
- SQS simulation
- Environment-based configuration

## Observability
- Structured logs
- Request tracing
- Basic metrics
- Monitoring-ready architecture

---

# Project Structure

```text
event-driven-document-processor/
│
├── app/
│   ├── api/
│   ├── consumers/
│   ├── producers/
│   ├── services/
│   ├── models/
│   ├── core/
│   ├── config/
│   └── main.py
│
├── tests/
├── docker/
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# Main Flow

## 1. API receives request

```http
POST /documents
```

Example payload:

```json
{
  "document_id": "123",
  "document_type": "invoice"
}
```

---

## 2. Event is published to Kafka

The API publishes a message to a Kafka topic.

---

## 3. Consumer processes event

The consumer:
- Reads the event
- Simulates document processing
- Generates logs
- Uploads result to S3

---

## 4. Metrics and logs are exposed

Monitoring endpoints:
- `/health`
- `/metrics`

---

# Local Development

## Requirements

- Docker
- Docker Compose
- Python 3.12

---

# Running the Project

## Clone repository

```bash
git clone https://github.com/braulioti/event-driven-document-processor.git
```

## Start services

```bash
docker compose up --build
```

---

# Planned Services

- FastAPI API
- Kafka
- Zookeeper
- LocalStack
- Prometheus (future)
- Grafana (future)

---

# Learning Goals

This project was created to practice:

- FastAPI
- Docker
- Kafka/Event-driven systems
- AWS integrations
- Cloud-native architecture
- Observability concepts
- Corporate backend patterns

---

# Future Improvements

- Kubernetes deployment
- CI/CD pipelines
- DynamoDB integration
- Distributed tracing
- Authentication and authorization
- Terraform infrastructure
- Grafana dashboards

---

# Author

Developed as a backend engineering practice project focused on modern enterprise architecture patterns.