# RICHYS – Behavioral Finance Demo

AI-driven financial-planning toolkit that calculates personalized goal milestones, optimizes portfolios, and flags behavioral biases.

*This repository contains documentation, architecture diagrams, and demo API endpoints. Full production code is available to partners under NDA.*

[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/django-4.2+-green.svg)](https://djangoproject.com)
[![Demo](https://img.shields.io/badge/status-demo-orange.svg)](#demo-endpoints)
[![Stars](https://img.shields.io/github/stars/richys-co/richys?style=social)](https://github.com/richys-co/richys/stargazers)

---

## Quick Start

```bash
# Clone the demo repository
git clone https://github.com/richys-co/richys.git
cd richys

# Start the live API demo server
./run_api_demo.sh

# This will install dependencies and start FastAPI server at:
# → http://localhost:8001/docs (Interactive Swagger UI)
# → http://localhost:8001/v1/health (Health check)
```

**Live Demo**: [Portfolio Optimization API](https://github.com/richys-co/richys/blob/main/API_DEMO.md#portfolio-optimization-api)

---

## What's Inside

### 🚀 **Core Features**
- **Portfolio Optimization**: ML-based asset allocation with behavioral constraints
- **Bias Detection**: Cognitive bias analysis using behavioral finance models  
- **Market Prediction**: Time series forecasting with multiple ML models
- **Risk Analysis**: Advanced risk metrics and stress testing
- **AI Financial Advisor**: LLM-driven personalised guidance

### 📊 **Technical Stack**
- **Backend**: Django 4.2+, FastAPI for ML endpoints
- **ML/AI**: TensorFlow, PyTorch, scikit-learn, OpenAI
- **Data**: PostgreSQL, Redis, time-series analysis
- **Infrastructure**: Docker, Kubernetes-ready architecture
- **APIs**: REST + GraphQL with comprehensive documentation

### 🏗️ **Architecture**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Django API    │    │   ML Pipeline   │
│   React/Vue     │───▶│   FastAPI       │───▶│   TensorFlow    │
│   Portfolio UI  │    │   GraphQL       │    │   PyTorch       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Data     │    │   PostgreSQL    │    │   Redis Cache   │
│   Portfolios    │    │   Time Series   │    │   ML Models     │
│   Behavioral    │    │   Market Data   │    │   Predictions   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## Demo Endpoints

🎪 **NEW: Live API Demo Server**

Experience our AI-powered behavioral finance APIs in action with a fully working FastAPI server:

```bash
# Start the live demo server
./run_api_demo.sh

# Test endpoints automatically  
./test_api.sh
```

**Interactive Demo:** http://localhost:8001/docs  
**Demo API Key:** `demo_key_12345`

The demo server includes:
- 🧠 **Behavioral Analysis** - Real cognitive bias detection
- 📈 **Portfolio Optimization** - AI-powered asset allocation
- 🔮 **Market Prediction** - ML-based forecasting
- 💬 **AI Financial Advisor** - Conversational guidance
- ❤️ **Health Check** - Service monitoring

### Portfolio Optimization
```python
POST /api/v1/optimize-portfolio
{
    "current_allocation": {"stocks": 0.6, "bonds": 0.4},
    "risk_profile": "moderate",
    "constraints": {"max_single_position": 0.2}
}

# Response: AI-optimized allocation with expected metrics
{
    "optimized_weights": {"stocks": 0.55, "bonds": 0.35, "alternatives": 0.1},
    "expected_return": 0.078,
    "volatility": 0.156,
    "sharpe_ratio": 1.21
}
```

### Behavioral Analysis
```python
POST /api/v1/behavioral-analysis
{
    "user_id": "demo_user",
    "transaction_history": [...],
    "analysis_period": "12_months"
}

# Response: Cognitive bias detection and coaching
{
    "detected_biases": {
        "loss_aversion": {"score": 2.1, "severity": "moderate"},
        "overconfidence": {"score": 1.8, "severity": "low"}
    },
    "recommendations": ["Enable automatic rebalancing", "Set up DCA schedule"]
}
```

---

## 🎯 What You'll Experience

This demo showcases **AI-powered behavioral finance APIs** that analyze investment psychology and optimize portfolios. Here's exactly what you'll see:

### 🧠 **Behavioral Analysis Demo**
- **Input:** Trading history + market reactions  
- **Output:** Cognitive bias scores (loss aversion: 2.3, overconfidence: 1.8) + AI coaching
- **Business Value:** "User shows tendency to hold losing positions too long - set automatic stop-loss orders"

### 📈 **Portfolio Optimization Demo** 
- **Input:** Current allocation (60% stocks, 20% bonds) + risk profile
- **Output:** AI-optimized portfolio (55% stocks, 25% bonds) + rationale
- **Business Value:** "Increased bond allocation for emotional comfort while maintaining growth"

### 🔮 **Market Prediction Demo**
- **Input:** Market indicators + economic factors
- **Output:** Return forecasts (7.8% expected) + sector predictions
- **Business Value:** "Technology sector bullish (81% confidence), maintain diversified exposure"

### 💬 **AI Financial Advisor Demo**
- **Input:** "I'm worried about market volatility affecting my retirement"
- **Output:** Personalized advice + action items + educational insights
- **Business Value:** Human-like financial guidance at scale

### **Key Takeaways:**

1. **🧠 Real Behavioral Finance AI** - Live bias detection and coaching
2. **📊 Psychology-Aware Optimization** - Risk management with emotional constraints  
3. **🔮 Market Intelligence** - AI predictions with confidence intervals
4. **💡 Conversational Financial Planning** - Natural language advisory

---

## Documentation

| Document | Description |
|----------|-------------|
| [🔧 **API_DEMO.md**](API_DEMO.md) | Complete API documentation with examples, code samples, and integration guides |

*For production architecture details and partnership opportunities, please contact our team.*

---

## Technology Highlights

### Machine Learning Models
- **Portfolio Optimization**: Modern portfolio theory enhanced with behavioral constraints
- **Bias Detection**: Pattern recognition in trading behavior using ensemble methods
- **Market Prediction**: LSTM and transformer models for time series forecasting
- **Risk Assessment**: Monte Carlo simulation and VaR calculations

### AI Integration
- **OpenAI**: Financial advisory and natural language processing
- **Behavioral Analytics**: Psychological pattern recognition in investment decisions
- **Real-time Processing**: Stream processing for live market data and user interactions

### Performance Characteristics *(Example Metrics)*
- **Response Time**: Typical API response < 200ms
- **Model Accuracy**: Behavioral bias detection ~85-90% on test data
- **Scalability**: Designed for horizontal scaling with microservices architecture
- **Reliability**: Production-ready with comprehensive error handling

*Note: Actual performance depends on deployment configuration and data complexity*

---

## Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 13+
- Redis 6+
- Node.js 18+ (for frontend development)

### Installation
```bash
# Quick start - run the live API demo
./run_api_demo.sh

# Or manual installation:
pip install -r requirements-api-demo.txt

# Start FastAPI server
python3 api_demo_server.py

# Test the API endpoints
./test_api.sh
```

### Docker Setup
```bash
# For production deployment (not included in demo)
# The demo uses simple FastAPI server via ./run_api_demo.sh

# Demo server access:
# http://localhost:8001/docs (Swagger UI)
# http://localhost:8001/v1/health (Health check)
```

---

## Security & Compliance

- **Data Privacy**: User data anonymization and secure storage
- **API Security**: Rate limiting, authentication, and input validation
- **Financial Compliance**: Designed with regulatory requirements in mind
- **Code Quality**: Comprehensive testing and static analysis

*Note: Compliance certifications (SOC2, ISO27001) are planned for production deployment*

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

The API examples and documentation in this repository are provided **for demonstration purposes only** and do not constitute professional financial advice. Always consult a qualified advisor before making investment decisions.
