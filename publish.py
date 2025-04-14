from google.cloud import pubsub_v1
from google.oauth2 import service_account
import json

# Path to your service account key file
credentials_path = "D:/VCC Project/vcc-group-project-6-456306-3d1c490656fd.json"

# Load the credentials explicitly
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Replace with your GCP project ID and Pub/Sub topic name
project_id = "vcc-group-project-6-456306"
topic_id = "data_flow_streaming"

# Publisher client using the explicit credentials
publisher = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = publisher.topic_path(project_id, topic_id)

# Message to send
message = {
    "empid": 101,
    "name": "John Doe",
    "salary": 75000
}

# Convert the message to a JSON string
message_json = json.dumps(message).encode("utf-8")

# Publish the message
future = publisher.publish(topic_path, message_json)

# Print the message ID
print(f"Message published with ID: {future.result()}")
