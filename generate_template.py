import os
import argparse


def _print(msg):
	print("*"*80)
	print(msg)
	print("*"*80 + "\n")

def template(folder: str, competition: str) -> None:

	path = os.path.join(folder, competition)
	# folders
	notebook = os.path.join(path, "notebooks")
	inputs = os.path.join(path, "inputs")
	outputs = os.path.join(path, "outputs")
	models = os.path.join(outputs, "models")
	data = os.path.join(outputs, "data")
	src = os.path.join(path, "src")

	# create folders
	os.makedirs(notebook, exist_ok=True)
	os.makedirs(inputs, exist_ok=True)
	os.makedirs(outputs, exist_ok=True)
	os.makedirs(models, exist_ok=True)
	os.makedirs(data, exist_ok=True)
	os.makedirs(src, exist_ok=True)
	_print(f"Template generated at: {path}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Creates a template for competition code")
	parser.add_argument("--folder", "-f", help="Path to the root folder within which to create the competition template", type=str, required=True)
	parser.add_argument("--competition", "-c", help="Name of the competition", type=str, required=True)
	args = parser.parse_args()

	template(args.folder, args.competition)
