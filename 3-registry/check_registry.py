def has_programming_badge(readme_file):
    with open(readme_file) as text:
        for line in text:
            for lang, badge in registries["by_language"].items():
                if badge in line:
                    return lang + " badge found"

    return "No registry found"


def main():
    print(has_programming_badge("README.md"))


if __name__ == "__main__":
    import yaml

    with open("/data/registries.yml") as opened_file:
        registries = yaml.safe_load(opened_file)
    main()
