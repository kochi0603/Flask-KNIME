from flask import Flask
import pandas as pd
import knime
import os

knime.executable_path = "/Applications/KNIME 4.0.1.app/Contents/MacOS/Knime"
WORKSPACE = "/Users/chemoinfo/knime-workspace"
app = Flask(__name__)

@app.route("/")
def hello():
	workflow = "AUTOMATION/sample0"
	input_table_1 = pd.DataFrame(
		[["blau", -273.15], ["gelb", 100.0]], columns=["color", "temp"])

	with knime.Workflow(workflow_path=workflow,workspace_path=WORKSPACE) as wf:
		wf.data_table_inputs[0] = input_table_1
		wf.execute()
		output_table = wf.data_table_outputs[0]

	return output_table.to_html()

if __name__ == "__main__":
	app.run( debug=True )

