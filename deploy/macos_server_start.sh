#!/usr/bin/env bash

# Make it executable once with: chmod +x deploy/macos_server_start.sh,
# then run with: ./deploy/macos_server_start.sh
#
# Start the Python Flask server for tablInspector (macOS)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$SCRIPT_DIR"
"$REPO_ROOT/.venv/bin/python" _tablserver.py &

echo "Waiting for server to be ready..."
until curl -s -o /dev/null http://localhost:3000/triangle; do
    sleep 1
done

echo
echo "Server is running at http://localhost:3000"

# Open the TableExplorer in the default browser (adjust filename if needed)
if ! open "http://localhost:3000/templates/TableExplorer.html" >/dev/null 2>&1; then
    echo "Could not open browser automatically."
    echo "Open: http://localhost:3000/templates/TableExplorer.html"
fi

read -r -p "Press Enter to exit..."