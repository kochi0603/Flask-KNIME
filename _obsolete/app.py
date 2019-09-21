from flask import Flask
import pandas as pd
import knime
import os

#knime.executable_path = "/Applications/KNIME 3.7.1.app/Contents/MacOS/Knime"
knime.executable_path = "/Applications/KNIME 4.0.1.app/Contents/MacOS/Knime"
if os.path.isfile(knime.executable_path):
	print(222)

WORKSPACE = "/Users/chemoinfo/knime-workspace"
app = Flask(__name__)

@app.route("/")
def hello():
	if os.path.isfile(knime.executable_path):
		print(111)
	workflow = "AUTOMATION/sample0"
	#workflow = "test_simple_container_table_01"
	input_table_1 = pd.DataFrame([["blau", -273.15], ["gelb", 100.0]], columns=["color", "temp"])
	#input_table_2 = {
	#	"table-spec": [{"color": "string"}, {"size": "long"}],
	#	"table-data": [["blue", 42], ["yellow", 8675309]]
	#}

	with knime.Workflow(workflow_path=workflow,workspace_path=WORKSPACE) as wf:
		print( len( wf.data_table_inputs ) )
		wf.data_table_inputs[0] = input_table_1
		#wf.data_table_inputs[1] = input_table_2
		wf.execute()
		output_table = wf.data_table_outputs[0]

	#return "Hello World!"
	return output_table.to_html()

if __name__ == "__main__":
	# webサーバー立ち上げ
	# @app.route("hoge")などで指定すると、http://127.0.0.1:5000/hogeでの動作を記述できる。
	app.run( debug=True )

