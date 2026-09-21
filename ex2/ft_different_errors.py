def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "x" + 21
    else:
        print("Operation completed successfully!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    test_operations = [0, 1, 2, 3, 4]

    for operation in test_operations:
        print(f"Testing operation {operation}...")

        try:
            garden_operations(operation)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
