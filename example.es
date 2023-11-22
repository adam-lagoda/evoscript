# Example EvoScript code

# Define a function to add two numbers
evofunction add(a, b) {
    evoreturn a + b;
}

# Main function
evofunction main() {
    # Print a message
    evoprint("Hello from EvoScript!");

    # Call the add function and print the result
    evoprint("The sum of 3 and 5 is: ", add(3, 5));
}
