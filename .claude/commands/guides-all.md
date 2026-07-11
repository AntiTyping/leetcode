Run all eight generators in sequence:

1. First, invoke the `/guide` skill and wait for it to complete fully (including opening the file).
2. Then, invoke the `/lang-guide` skill and wait for it to complete fully (including opening the file).
3. Then, invoke the `/python-guide` skill and wait for it to complete fully (including opening the file).
4. Then, invoke the `/typescript-guide` skill and wait for it to complete fully (including opening the file).
5. Then, invoke the `/golang-guide` skill and wait for it to complete fully (including opening the file).
6. Then, invoke the `/javascript-guide` skill and wait for it to complete fully (including opening the file).
7. Then, invoke the `/report` skill and wait for it to complete fully (including opening the file).
8. Finally, invoke the `/report-problems` skill and wait for it to complete fully (including opening the file).

Each skill should be invoked exactly as if the user had typed the corresponding slash command. Wait for each to finish before starting the next.
