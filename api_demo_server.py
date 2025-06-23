"""
RICHYS AI Finance API Demo Server
Live demonstration of AI-powered behavioral finance APIs

Run with: python3 api_demo_server.py
Interactive docs: http://localhost:8001/docs

Author: RICHYS AI Finance Team
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import uvicorn
from datetime import datetime, date
import json

# Initialize FastAPI app
app = FastAPI(
    title="RICHYS AI Finance API",
    description="Live Demo of AI-Powered Behavioral Finance APIs",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Demo API key
DEMO_API_KEY = "demo_key_12345"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify the demo API key"""
    if credentials.credentials != DEMO_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key. Use: demo_key_12345",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

# Pydantic Models
class TransactionHistory(BaseModel):
    date: str = Field(..., description="Transaction date (YYYY-MM-DD)")
    action: str = Field(..., description="buy/sell/hold")
    asset: str = Field(..., description="Asset symbol")
    amount: float = Field(..., description="Transaction amount")
    market_condition: str = Field(..., description="Market condition during transaction")

class MarketInteraction(BaseModel):
    date: str = Field(..., description="Interaction date")
    action: str = Field(..., description="Type of market interaction")
    market_decline: Optional[float] = Field(None, description="Market decline percentage")
    user_reaction: str = Field(..., description="User's emotional reaction")

class BehavioralFeatures(BaseModel):
    transaction_history: List[TransactionHistory]
    market_interactions: List[MarketInteraction]

class BehavioralAnalysisRequest(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    behavioral_features: BehavioralFeatures

class BehavioralConstraints(BaseModel):
    loss_aversion_score: float = Field(..., description="Loss aversion score (1-5)")
    max_volatility_comfort: float = Field(..., description="Maximum volatility tolerance")

class UserProfile(BaseModel):
    risk_tolerance: str = Field(..., description="conservative/moderate/aggressive")
    investment_horizon: str = Field(..., description="short_term/medium_term/long_term")
    behavioral_constraints: BehavioralConstraints

class Portfolio(BaseModel):
    US_STOCKS: float
    BONDS: float
    INTERNATIONAL_STOCKS: float
    CASH: float

class PortfolioOptimizationRequest(BaseModel):
    user_profile: UserProfile
    current_portfolio: Portfolio
    optimization_objectives: List[str] = Field(..., description="List of optimization goals")

class MarketData(BaseModel):
    timeframe: str = Field(..., description="Prediction timeframe")
    market_indicators: Dict[str, float] = Field(..., description="Current market indicators")
    economic_factors: List[str] = Field(..., description="Economic factors to consider")

class MarketPredictionRequest(BaseModel):
    user_id: str
    market_data: MarketData
    prediction_horizon: str = Field(..., description="short_term/medium_term/long_term")

class FinancialQuestion(BaseModel):
    user_id: str
    question: str = Field(..., description="Financial question or concern")
    context: Dict[str, Any] = Field(default={}, description="Additional context")

# API Endpoints

@app.get("/v1/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "RICHYS AI Finance API Demo",
        "version": "1.0.0"
    }

@app.post("/v1/ai/behavioral-analysis")
async def behavioral_analysis(
    request: BehavioralAnalysisRequest,
    token: str = Depends(verify_token)
):
    """
    Analyze user's behavioral patterns and identify cognitive biases
    """
    try:
        # Simulated AI analysis with realistic responses
        analysis_result = {
            "user_id": request.user_id,
            "analysis_timestamp": datetime.now().isoformat(),
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
                },
                {
                    "pattern": "market_timing_attempts",
                    "confidence": 0.72,
                    "description": "Frequent trading during volatile periods",
                    "recommendation": "Consider dollar-cost averaging strategy"
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
        
        return analysis_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/v1/ai/optimize-portfolio")
async def optimize_portfolio(
    request: PortfolioOptimizationRequest,
    token: str = Depends(verify_token)
):
    """
    AI-powered portfolio optimization with behavioral constraints
    """
    try:
        # Simulated portfolio optimization
        optimization_result = {
            "optimization_timestamp": datetime.now().isoformat(),
            "user_profile": request.user_profile.dict(),
            "current_allocation": request.current_portfolio.dict(),
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
            "rationale": {
                "optimization_method": "Mean-Variance Optimization with Behavioral Constraints",
                "key_factors": [
                    "Risk-adjusted returns maximization",
                    "Behavioral comfort zone maintenance",
                    "Market correlation diversification"
                ],
                "trade_offs": "Slightly lower expected return for significantly reduced emotional stress"
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
        
        return optimization_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Optimization failed: {str(e)}")

@app.post("/v1/ai/market-prediction")
async def market_prediction(
    request: MarketPredictionRequest,
    token: str = Depends(verify_token)
):
    """
    AI-powered market prediction and forecasting
    """
    try:
        # Simulated market prediction
        prediction_result = {
            "user_id": request.user_id,
            "prediction_timestamp": datetime.now().isoformat(),
            "prediction_horizon": request.prediction_horizon,
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
            "risk_factors": [
                {
                    "factor": "inflation_uncertainty",
                    "impact": "medium",
                    "probability": 0.68
                },
                {
                    "factor": "geopolitical_tensions",
                    "impact": "high",
                    "probability": 0.45
                }
            ],
            "ai_insights": {
                "key_drivers": [
                    "Corporate earnings growth",
                    "Federal Reserve policy normalization",
                    "Consumer spending patterns"
                ],
                "investment_themes": [
                    "AI and automation adoption",
                    "Sustainable energy transition",
                    "Healthcare innovation"
                ],
                "timing_considerations": "Market appears to be in mid-cycle expansion phase"
            },
            "actionable_recommendations": [
                "Maintain diversified equity exposure",
                "Consider technology sector overweight",
                "Keep 6-12 months cash reserves",
                "Monitor Federal Reserve communications closely"
            ],
            "model_accuracy": 0.78
        }
        
        return prediction_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post("/v1/ai/financial-advisor")
async def financial_advisor(
    request: FinancialQuestion,
    token: str = Depends(verify_token)
):
    """
    Conversational AI financial advisor
    """
    try:
        # Simulated AI financial advisor response
        advisor_response = {
            "user_id": request.user_id,
            "response_timestamp": datetime.now().isoformat(),
            "question": request.question,
            "ai_response": {
                "analysis": "Based on your question, I can see you're concerned about market volatility and its impact on your retirement planning. This is a very common and legitimate concern.",
                "personalized_advice": "Given your investment timeline and risk profile, here's my recommendation: maintain a diversified portfolio with 60% stocks and 40% bonds. The current market volatility is normal and shouldn't derail your long-term strategy.",
                "action_items": [
                    "Review your asset allocation quarterly",
                    "Consider increasing your 401(k) contribution by 1-2%",
                    "Set up automatic rebalancing to maintain target allocation"
                ],
                "educational_insight": "Market volatility is actually an opportunity for long-term investors. Dollar-cost averaging helps you buy more shares when prices are low and fewer when prices are high.",
                "risk_assessment": "Your current strategy aligns well with your goals, but consider stress-testing your portfolio against a 20-30% market decline."
            },
            "follow_up_questions": [
                "Would you like me to analyze your specific risk tolerance?",
                "Should we discuss tax-efficient investment strategies?",
                "Are you interested in exploring ESG investment options?"
            ],
            "related_topics": [
                "retirement_planning",
                "risk_management",
                "portfolio_diversification",
                "tax_optimization"
            ],
            "confidence_score": 0.87,
            "disclaimer": "This is educational information only and not personalized financial advice. Please consult with a qualified financial advisor for decisions specific to your situation."
        }
        
        return advisor_response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Advisor response failed: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting RICHYS AI Finance API Demo Server...")
    print("📖 Interactive documentation: http://localhost:8001/docs")
    print("🔑 Demo API Key: demo_key_12345")
    print("❤️  Health check: http://localhost:8001/v1/health")
    
    uvicorn.run(
        "api_demo_server:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    ) 