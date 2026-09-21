def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    test_input = ["25", "abc"]

    for value in test_input:
        print(f"Input data is '{value}'")

        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C\n")

        except Exception as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
