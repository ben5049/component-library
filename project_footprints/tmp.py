import os

folder = os.path.dirname(__file__)

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if not os.path.isfile(path):
        continue

    ext = file.split(".")[-1]
    if ext not in ["kicad_mod"]:
        continue

    print(f"working on '{file}'")

    contents = ""
    with open(path, "r", encoding="utf-8") as file:
        contents = file.read()

    contents = contents.replace("switch_models", "project_models")
    contents = contents.replace("component_library", "component-library")

    with open(path, "w", encoding="utf-8") as file:
        file.write(contents)
