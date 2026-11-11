
def fuzzy_sets():
    """Experiment 7: Operations on Fuzzy Sets."""

    # Define two fuzzy sets
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.6, "c": 0.4, "d": 0.5}

    print("FUZZY SET OPERATIONS")
    print("Set A:", A)
    print("Set B:", B)

    # Union: Maximum membership value
    union = {key: max(A[key], B[key]) for key in A}
    print("\nUnion (A U B):", union)

    # Intersection: Minimum membership value
    intersection = {
        key: min(A[key], B[key]) for key in A
    }
    print("Intersection (A ∩ B):", intersection)

    # Complement of A
    complement = {
        key: 1 - A[key] for key in A
    }
    print("Complement of A:", complement)

    # Scalar multiplication
    alpha = 0.5
    scalar = {
        key: min(1, alpha * A[key]) for key in A
    }
    print("Scalar Multiplication (0.5A):", scalar)

    # Fuzzy addition
    addition = {
        key: min(1, A[key] + B[key]) for key in A
    }
    print("Fuzzy Addition (A + B):", addition)

    # Fuzzy subtraction (A - B)
    subtraction = {
        key: max(0, A[key] - B[key]) for key in A
    }
    print("Fuzzy Subtraction (A - B):", subtraction)

    return {
        "union": union,
        "intersection": intersection,
        "complement": complement,
        "scalar": scalar,
        "addition": addition,
        "subtraction": subtraction
    }
