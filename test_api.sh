#!/bin/bash
set -e  # Exit on any error

echo "🧪 Testing RICHYS AI Finance API Demo..."
echo ""

API_KEY="demo_key_12345"
BASE_URL="http://localhost:8001/v1"

# Test health endpoint
echo "❤️  Testing health endpoint..."
curl -s "$BASE_URL/health" | python3 -m json.tool
echo ""

# Test behavioral analysis
echo "🧠 Testing behavioral analysis..."
curl -X POST "$BASE_URL/ai/behavioral-analysis" \
  -H "Authorization: Bearer $API_KEY" \
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
  }' | python3 -m json.tool

echo ""
echo "✅ API testing complete!"
echo "🎪 For interactive testing, visit: http://localhost:8001/docs" 