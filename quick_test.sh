#!/bin/bash
set -e  # Exit on any error

echo "🚀 Quick Health Check - RICHYS API Demo"
echo ""

# Check if server is running
if curl -s http://localhost:8001/v1/health > /dev/null; then
    echo "✅ Server is running at http://localhost:8001"
    echo "📖 Interactive docs: http://localhost:8001/docs"
    echo "🔑 Demo API Key: demo_key_12345"
    echo ""
    echo "Health status:"
    curl -s http://localhost:8001/v1/health | python3 -m json.tool
else
    echo "❌ Server not running. Start with: ./run_api_demo.sh"
fi 