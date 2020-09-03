def has_programming_badge(readme_file):
    with open(readme_file) as text:
        for line in text:
            if registries["by_language"]["pypi"] in line:
                return "PyPi badge is found"

            if registries["by_language"]["julia"] in line:
                return "Julia badge is found"

            if registries["by_language"]["ropensci"] in line:
                return "ROpenSci badge is found"

            if registries["by_language"]["cran"] in line:
                return "CRAN badge is found"

    return "No registry found"


def main():
    print(has_programming_badge("README.md"))


if __name__ == "__main__":
    import yaml

    with open("/data/registries.yml") as opened_file:
        registries = yaml.safe_load(opened_file)
    main()
