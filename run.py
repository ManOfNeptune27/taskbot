
from clock import ping
from todos import check
from water import remind

def run_step(name, step):
    try:
        step()
    except Exception as error:
        print(f"{name} failed: {error}")

def main():
    run_step("clock ping", ping)
    run_step("todo check", check)
    run_step("water reminder", remind)


if __name__ == "__main__":
    main()
