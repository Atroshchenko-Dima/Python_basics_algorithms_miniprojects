def make_hotdog(*topings):
    print(f"Выберите компоненты хот дога")
    for toping in topings:
        print(f" - {toping}")
make_hotdog('сосиска', "огурец", "перец")