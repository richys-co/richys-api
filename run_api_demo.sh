#!/bin/bash

echo "🚀 Starting RICHYS AI Finance API Demo..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is required but not installed."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is required but not installed."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements-api-demo.txt

echo ""
echo "🎯 Demo Information:"
echo "   📖 Interactive Docs: http://localhost:8001/docs"
echo "   🔑 Demo API Key: demo_key_12345"
echo "   ❤️  Health Check: http://localhost:8001/v1/health"
echo ""
echo "🎪 Click 'Authorize' in Swagger UI and enter: demo_key_12345"
echo ""

# Start the server
echo "🚀 Starting FastAPI server..."
python3 api_demo_server.py 