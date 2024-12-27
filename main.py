def count_calls_from_file(filename):
    """Counts the total number of calls from a given file.

    Args:
        filename: The name of the file containing call data.

    Returns:
        The total number of calls.
    """

    call_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("Store #"):
                call_count += 1

    return call_count

# Specify the filename
filename = "call_data.txt"

# Count the calls from the file
total_calls = count_calls_from_file(filename)
print("Total number of calls:", total_calls)