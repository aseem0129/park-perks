# ParkPerks AI

An AI-powered mobile app connecting college students with local businesses for sponsored parking solutions.

## Overview

ParkPerks AI is a smart platform that matches college students with local businesses willing to sponsor their campus parking in exchange for targeted marketing opportunities. The platform uses AI to create personalized matches based on student preferences and business goals.

### Key Features

#### For Students
- Free or discounted campus parking
- Personalized business matches
- In-app rewards and deals
- Easy profile setup and management

#### For Businesses
- Targeted student sponsorship
- Real-time analytics dashboard
- Customizable campaign rules
- Performance tracking

## Tech Stack

### Backend
- FastAPI (Python web framework)
- PostgreSQL (Primary database)
- SQLAlchemy (ORM)
- PyTorch (AI/ML framework)
- JWT Authentication

### Frontend (Coming Soon)
- React Native
- TypeScript
- Redux Toolkit

## Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL 13+
- Node.js 16+ (for frontend)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/parkperks.git
cd parkperks
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
alembic upgrade head
```

6. Run the development server:
```bash
uvicorn app.main:app --reload
```

## Project Structure

```
parkperks/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   └── api.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   │
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── business.py
│   │   │   └── parking.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── business.py
│   │   │   └── parking.py
│   │   │
│   │   └── services/
│   │       ├── ai/
│   │       └── parking/
│   │
│   ├── tests/
│   │
│   ├── alembic/
│   │
│   ├── .env.example
│   │
│   └── requirements.txt
│
└── README.md 