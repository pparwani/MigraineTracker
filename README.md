# Migraine Tracker

Migraine Tracker is an API designed to help users log and analyze their migraine episodes. Built with FastAPI and MongoDB, this application allows users to securely manage their migraine data and retrieve analytical insights through a series of endpoints.

## Features

- **User Authentication**: Secure user registration and login.
- **Migraine Logging**: Users can log migraine attacks, noting times, symptoms, triggers, and remedies.
- **Data Analysis**: Provides analytical views of the data to track patterns and potential triggers.
- **Data Export**: Users can export their data for offline analysis.

## Technologies

- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **[MongoDB](https://www.mongodb.com/)**: Source-available cross-platform document-oriented database program.
- **[Beanie](https://github.com/roman-right/beanie)**: An asynchronous Python ORM for MongoDB.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Data validation and settings management using Python type annotations.

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/migraine-tracker.git
cd migraine-tracker
