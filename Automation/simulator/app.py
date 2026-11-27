import json
from pathlib import Path
 
from flask import Flask, jsonify, render_template_string, request
 
 
app = Flask(__name__)
 
project_folder = Path(__file__).resolve().parent.parent.parent
equipment_file = project_folder / "config" / "equipment.json"
 
with open(equipment_file, "r", encoding="utf-8") as file:
    equipment_list = json.load(file)
 
equipments = {}
for equipment in equipment_list:
    equipments[equipment["id"]] = equipment
 
# Preserve the original misspelled name for compatibility.
equiments = equipments
 
 
@app.get("/")
def index():
    selected_id = request.args.get("id", type=int)
    selected_equipment = equipments.get(selected_id)
 
    return render_template_string(
        """
<!doctype html>
<title>Equipment lookup</title>
<h1>Equipment lookup</h1>
<form method="get">
<label for="equipment-id">Select an equipment ID:</label>
<select id="equipment-id" name="id" onchange="this.form.submit()">
<option value="">Select an ID</option>
                {% for item in equipment_list %}
<option value="{{ item.id }}"
                    {% if item.id == selected_id %}selected{% endif %}>
                    {{ item.id }}
</option>
                {% endfor %}
</select>
<noscript><button type="submit">Show equipment</button></noscript>
</form>
 
        {% if selected_equipment %}
<h2>{{ selected_equipment.name }}</h2>
<p>ID: {{ selected_equipment.id }}</p>
<p>Type: {{ selected_equipment.type }}</p>
<p>Status: {{ selected_equipment.status }}</p>
        {% elif selected_id is not none %}
<p>Equipment not found.</p>
        {% endif %}
        """,
        equipment_list=list(equipments.values()),
        selected_id=selected_id,
        selected_equipment=selected_equipment,
    )
 
 
@app.get("/equipment")
def get_equipment():
    return jsonify(list(equipments.values()))
 
 
@app.get("/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    equipment = equipments.get(equipment_id)
    if equipment is None:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(equipment)
 
 
if __name__ == "__main__":
    # debug=True enables auto-reload on code changes and detailed error pages
    app.run(debug=True)