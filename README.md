
# PostIgnite 🌍

**PostIgnite** is an AI-powered platform designed to streamline interactions with Poste Algérie. By leveraging Optical Character Recognition (OCR) technology, it simplifies form-filling, document processing, and task management for both employees and users.

---

## Table of Contents

1. [Overview](#overview)
2. [Build Status](#build-status)
3. [Key Features](#key-features)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Setup](#setup)
5. [Why PostIgnite?](#why-postignite)
6. [Contact](#contact)
7. [License](#license)

---

## Overview

**PostIgnite** bridges the gap between users and the services of Poste Algérie. It provides an efficient, AI-driven approach to handling forms and administrative tasks, making processes faster and more accurate.

---

## Build Status

![Build Status](https://img.shields.io/github/actions/workflow/status/PostIgnite/PostIgnite-Front/ci.yml?label=build)

---

## Key Features

### 📝 Smart Form Processing

- Uses OCR to automatically extract data from documents.
- Simplifies and accelerates form-filling for users and employees.

### 📋 Administrative Assistance

- Streamlines common tasks like form submission, tracking, and updates.
- Reduces manual errors with AI-based validation.

### 🔍 Enhanced Accessibility

- Makes administrative services user-friendly and efficient.
- Designed to cater to both employees and the public.

---
## Technologies utilisés
### Machine Learning
- **TensorFlow** : Custom-trained models for OCR to extract and validate text from documents.
- **Custom OCR Models**: Tailored to recognize specific document types and extract key details efficiently.

###  Cloud Services
- **Google Cloud Vision API**: Used for image analysis and OCR to extract text from documents.
- **Google Cloud SQL**: A managed relational database to store user information and processed documents.

### Backend Framework
- **FastAPI**: A high-performance, modern web framework for building APIs.

### Database
- **PostgreSQL**: For structured storage of users, documents, and transaction data.

### Deployment
- **Google Cloud Platform**: For hosting services like database and Vision API.


## Getting Started

### Prerequisites

Prerequisites

- Python 3.10 or above
- PostgreSQL

### Installation

1. **Clone the Repository**
   ```bash
   git clonehttps://github.com/PostIgnite-Innovpost/backend.git
   ```
2. **Set Up Environment Variables**
- Create a .env file in the project root and configure the following variables
3. **Install Dependencies**
- pip install -r requirements.txt
4. fastapi dev main.py
