
from clock import ping
from todos import check

def run_step(name, step):
    try:
        step()
    except Exception as error:
        print(f"{name} failed: {error}")

def main():
    run_step("clock ping", ping)
    run_step("todo check", check)


if __name__ == "__main__":
    main()
