# 🔧 RICHYS – Live API Demo & Examples

*Interactive demonstration of AI-powered behavioral finance APIs*

**Real-time access to machine learning endpoints for portfolio optimization, behavioral analysis, and market prediction.**

---

## 🎯 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [🧠 Behavioral Analysis API](#-behavioral-analysis-api)
- [📈 Portfolio Optimization API](#-portfolio-optimization-api)
- [🔮 Market Prediction API](#-market-prediction-api)
- [💬 AI Financial Advisor API](#-ai-financial-advisor-api)
- [❤️ Health Check API](#-health-check-api)
- [🔗 Integration Examples](#-integration-examples)

---

## 🚀 Quick Start

### **Start the Demo Server**
```bash
# Clone and start the demo
git clone https://github.com/richys-co/richys-api.git
cd richys-api
./run_api_demo.sh
```

### **API Base URL**
```
http://localhost:8001/v1
```

### **Authentication**
```bash
# Demo API key (for localhost testing only)
API_KEY="demo_key_12345"

# All requests require API key in Authorization header
curl -H "Authorization: Bearer demo_key_12345" \
     -H "Content-Type: application/json" \
     http://localhost:8001/v1/health
```

### **Interactive API Explorer**
🎪 **[Live Swagger UI →](http://localhost:8001/docs)**

**Steps to use Swagger UI:**
1. Open http://localhost:8001/docs
2. Click "Authorize" button 
3. Enter: `demo_key_12345`
4. Test any endpoint with real AI responses!

---

## 🧠 Behavioral Analysis API

### **Comprehensive Behavioral Profile**

#### **Endpoint**: `POST /v1/ai/behavioral-analysis`

```bash
curl -X POST "http://localhost:8001/v1/ai/behavioral-analysis" \
  -H "Authorization: Bearer demo_key_12345" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo_user_001",
    "behavioral_features": {
      "transaction_history": [
        {
          "date": "2024-01-15",
          "action": "buy",
          "asset": "AAPL",
          "amount": 5000,
          "market_condition": "volatile"
        }
      ],
      "market_interactions": [
        {
          "date": "2024-01-20",
          "action": "portfolio_check",
          "market_decline": -0.05,
          "user_reaction": "anxiety"
        }
      ]
    }
  }'
```

#### **Response**: AI-Powered Behavioral Insights
```json
{
  "user_id": "demo_user_001",
  "analysis_timestamp": "2024-06-23T18:15:00",
  "behavioral_scores": {
    "loss_aversion": 2.3,
    "overconfidence": 1.8,
    "herding_tendency": 2.1,
    "confirmation_bias": 2.7,
    "anchoring_bias": 1.9
  },
  "risk_profile": {
    "calculated_risk_tolerance": "moderate_aggressive",
    "emotional_volatility": "medium",
    "decision_consistency": 0.76
  },
  "detected_patterns": [
    {
      "pattern": "loss_aversion",
      "confidence": 0.85,
      "description": "User shows tendency to hold losing positions too long",
      "recommendation": "Set automatic stop-loss orders to reduce emotional decision-making"
    }
  ],
  "ai_coaching": {
    "primary_recommendation": "Focus on long-term investment strategy and reduce emotional trading",
    "coaching_areas": ["emotional_regulation", "systematic_approach", "risk_management"],
    "next_steps": [
      "Review portfolio allocation quarterly instead of daily",
      "Set up automatic investments to reduce timing decisions",
      "Practice mindfulness techniques before making large trades"
    ]
  },
  "confidence_score": 0.82
}
```

---

## 📈 Portfolio Optimization API

### **AI-Powered Portfolio Optimization**

#### **Endpoint**: `POST /v1/ai/optimize-portfolio`

```bash
curl -X POST "http://localhost:8001/v1/ai/optimize-portfolio" \
  -H "Authorization: Bearer demo_key_12345" \
  -H "Content-Type: application/json" \
  -d '{
    "user_profile": {
      "risk_tolerance": "moderate_aggressive",
      "investment_horizon": "long_term",
      "behavioral_constraints": {
        "loss_aversion_score": 2.3,
        "max_volatility_comfort": 0.18
      }
    },
    "current_portfolio": {
      "US_STOCKS": 0.60,
      "BONDS": 0.20,
      "INTERNATIONAL_STOCKS": 0.15,
      "CASH": 0.05
    },
    "optimization_objectives": [
      "maximize_sharpe_ratio",
      "minimize_behavioral_friction"
    ]
  }'
```

#### **Response**: AI-Optimized Portfolio
```json
{
  "optimization_timestamp": "2024-06-23T18:15:00",
  "user_profile": { /* original profile */ },
  "current_allocation": {
    "US_STOCKS": 0.60,
    "BONDS": 0.20,
    "INTERNATIONAL_STOCKS": 0.15,
    "CASH": 0.05
  },
  "optimized_allocation": {
    "US_STOCKS": 0.55,
    "BONDS": 0.25,
    "INTERNATIONAL_STOCKS": 0.15,
    "CASH": 0.05
  },
  "allocation_changes": {
    "US_STOCKS": -0.05,
    "BONDS": +0.05,
    "INTERNATIONAL_STOCKS": 0.00,
    "CASH": 0.00
  },
  "risk_metrics": {
    "expected_annual_return": 0.087,
    "volatility": 0.162,
    "sharpe_ratio": 1.34,
    "max_drawdown": 0.245,
    "value_at_risk_95": 0.032
  },
  "behavioral_adjustments": {
    "loss_aversion_accommodation": "Increased bond allocation for emotional comfort",
    "volatility_buffer": "Maintained cash position for peace of mind",
    "rebalancing_frequency": "quarterly"
  },
  "implementation_plan": {
    "immediate_actions": [
      "Reduce US stock exposure by 5%",
      "Increase bond allocation by 5%"
    ],
    "timeline": "Implement changes over 2-3 weeks to avoid market timing issues",
    "monitoring": "Review allocation monthly, rebalance quarterly"
  },
  "confidence_score": 0.91
}
```

---

## 🔮 Market Prediction API

### **AI-Powered Market Forecasting**

#### **Endpoint**: `POST /v1/ai/market-prediction`

```bash
curl -X POST "http://localhost:8001/v1/ai/market-prediction" \
  -H "Authorization: Bearer demo_key_12345" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo_user_001",
    "market_data": {
      "timeframe": "3_months",
      "market_indicators": {
        "vix": 18.5,
        "sp500_pe": 22.1,
        "treasury_10y": 0.045
      },
      "economic_factors": [
        "inflation_outlook",
        "fed_policy",
        "employment_data"
      ]
    },
    "prediction_horizon": "medium_term"
  }'
```

#### **Response**: Market Forecast
```json
{
  "user_id": "demo_user_001",
  "prediction_timestamp": "2024-06-23T18:15:00",
  "prediction_horizon": "medium_term",
  "market_forecast": {
    "overall_direction": "moderately_bullish",
    "confidence_level": 0.73,
    "expected_return_range": {
      "low": 0.042,
      "medium": 0.078,
      "high": 0.114
    },
    "probability_distribution": {
      "bear_market": 0.15,
      "flat_market": 0.25,
      "bull_market": 0.60
    }
  },
  "sector_predictions": {
    "technology": {"direction": "bullish", "confidence": 0.81},
    "healthcare": {"direction": "moderately_bullish", "confidence": 0.72},
    "energy": {"direction": "neutral", "confidence": 0.65},
    "financials": {"direction": "moderately_bullish", "confidence": 0.69}
  },
  "actionable_recommendations": [
    "Maintain diversified equity exposure",
    "Consider technology sector overweight",
    "Keep 6-12 months cash reserves",
    "Monitor Federal Reserve communications closely"
  ],
  "model_accuracy": 0.78
}
```

---

## 💬 AI Financial Advisor API

### **Conversational AI Financial Guidance**

#### **Endpoint**: `POST /v1/ai/financial-advisor`

```bash
curl -X POST "http://localhost:8001/v1/ai/financial-advisor" \
  -H "Authorization: Bearer demo_key_12345" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo_user_001",
    "question": "I am worried about market volatility affecting my retirement planning. Should I reduce my stock allocation?",
    "context": {
      "age": 45,
      "retirement_target": 65,
      "current_portfolio_value": 250000
    }
  }'
```

#### **Response**: AI Financial Advice
```json
{
  "user_id": "demo_user_001",
  "response_timestamp": "2024-06-23T18:15:00",
  "question": "I am worried about market volatility affecting my retirement planning...",
  "ai_response": {
    "analysis": "Based on your question, I can see you're concerned about market volatility and its impact on your retirement planning. This is a very common and legitimate concern.",
    "personalized_advice": "Given your investment timeline and risk profile, here's my recommendation: maintain a diversified portfolio with 60% stocks and 40% bonds. The current market volatility is normal and shouldn't derail your long-term strategy.",
    "action_items": [
      "Review your asset allocation quarterly",
      "Consider increasing your 401(k) contribution by 1-2%",
      "Set up automatic rebalancing to maintain target allocation"
    ],
    "educational_insight": "Market volatility is actually an opportunity for long-term investors. Dollar-cost averaging helps you buy more shares when prices are low and fewer when prices are high."
  },
  "follow_up_questions": [
    "Would you like me to analyze your specific risk tolerance?",
    "Should we discuss tax-efficient investment strategies?",
    "Are you interested in exploring ESG investment options?"
  ],
  "confidence_score": 0.87,
  "disclaimer": "This is educational information only and not personalized financial advice. Please consult with a qualified financial advisor for decisions specific to your situation."
}
```

---

## ❤️ Health Check API

### **Service Health Monitoring**

#### **Endpoint**: `GET /v1/health`

```bash
curl http://localhost:8001/v1/health
```

#### **Response**: Service Status
```json
{
  "status": "healthy",
  "timestamp": "2024-06-23T18:15:00",
  "service": "RICHYS AI Finance API Demo",
  "version": "1.0.0"
}
```

---

## 🔗 Integration Examples

### **Frontend Integration (JavaScript)**

```javascript
// Initialize RICHYS API client
const richysClient = {
  baseURL: 'http://localhost:8001/v1',
  apiKey: 'demo_key_12345',
  
  async request(endpoint, data = null) {
    const options = {
      method: data ? 'POST' : 'GET',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      }
    };
    
    if (data) options.body = JSON.stringify(data);
    
    const response = await fetch(`${this.baseURL}${endpoint}`, options);
    return response.json();
  },
  
  // Get behavioral analysis
  async analyzeBehavior(userId, behavioralFeatures) {
    return this.request('/ai/behavioral-analysis', {
      user_id: userId,
      behavioral_features: behavioralFeatures
    });
  },
  
  // Optimize portfolio
  async optimizePortfolio(userProfile, currentPortfolio, objectives) {
    return this.request('/ai/optimize-portfolio', {
      user_profile: userProfile,
      current_portfolio: currentPortfolio,
      optimization_objectives: objectives
    });
  }
};

// Example usage
const analysis = await richysClient.analyzeBehavior('user_001', {
  transaction_history: [...],
  market_interactions: [...]
});

console.log('Behavioral Analysis:', analysis);
```

### **Python Integration**

```python
import requests
import json

class RichysAPI:
    def __init__(self):
        self.base_url = "http://localhost:8001/v1"
        self.api_key = "demo_key_12345"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def behavioral_analysis(self, user_id, behavioral_features):
        data = {
            "user_id": user_id,
            "behavioral_features": behavioral_features
        }
        response = requests.post(
            f"{self.base_url}/ai/behavioral-analysis",
            headers=self.headers,
            json=data
        )
        return response.json()
    
    def optimize_portfolio(self, user_profile, current_portfolio, objectives):
        data = {
            "user_profile": user_profile,
            "current_portfolio": current_portfolio,
            "optimization_objectives": objectives
        }
        response = requests.post(
            f"{self.base_url}/ai/optimize-portfolio",
            headers=self.headers,
            json=data
        )
        return response.json()

# Example usage
client = RichysAPI()

analysis = client.behavioral_analysis(
    user_id="demo_user_001",
    behavioral_features={
        "transaction_history": [
            {
                "date": "2024-01-15",
                "action": "buy",
                "asset": "AAPL",
                "amount": 5000,
                "market_condition": "volatile"
            }
        ],
        "market_interactions": [
            {
                "date": "2024-01-20",
                "action": "portfolio_check",
                "market_decline": -0.05,
                "user_reaction": "anxiety"
            }
        ]
    }
)

print("Behavioral Analysis Result:")
print(json.dumps(analysis, indent=2))
```

---

## 🧪 Testing

### **Automated Testing**
```bash
# Test all endpoints
./test_api.sh

# Quick health check
./quick_test.sh
```

### **Manual Testing via Swagger UI**
1. Start server: `./run_api_demo.sh`
2. Open: http://localhost:8001/docs
3. Click "Authorize" and enter: `demo_key_12345`
4. Test any endpoint with interactive forms

---

## 📚 Additional Resources

- **[README.md](README.md)** - Project overview, demo guide, and setup instructions

*For detailed feature documentation and partnership opportunities, please contact our team.*

---

## 💡 API Tips

### **Best Practices**
- Always include the Authorization header with Bearer token
- Use POST for all AI endpoints (they require request bodies)
- Check the health endpoint first to ensure server is running
- Review response schemas in Swagger UI for complete field definitions

### **Error Handling**
```json
{
  "detail": "Invalid API key. Use: demo_key_12345"
}
```

### **Rate Limiting**
Demo server has no rate limits, but production APIs would include:
- Rate limit headers in responses
- 429 status codes when limits exceeded
- Retry-After headers for backoff timing

---

*This is a demonstration of RICHYS AI-powered behavioral finance APIs. For production access and partnership opportunities, please contact our team.*
