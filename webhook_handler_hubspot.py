from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hubspot-webhook', methods=['POST'])
def handle_webhook():
    """
    Flask-based receiver for HubSpot API Webhooks.
    Triggers automated RevOps logic on property changes.
    """
    data = request.json
    for event in data:
        print(f"Event: {event['subscriptionType']} for Object: {event['objectId']}")
        # Logic to trigger CRM Data Cleansing or Syncing goes here
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(port=5000)
