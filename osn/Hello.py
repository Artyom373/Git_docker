import os
import json
import datetime
from flask imprt Flask

app = Flask(__name__)

BASE_FOLDER = oa.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources")

@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_DIR, "response.json")) as f:
        return "%s - %s" % (json.loads(f.read()).get("payload"), datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


if __name__ == "__man__":
    app.run(host="0.0.0.0", port=8080, depug=True)