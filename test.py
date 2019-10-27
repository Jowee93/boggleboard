def print_bob(n):
    if n == 0: # Base / Terminating Condition
        print(f"bob no. {n + 1}")
        return None
    else:
        print(f"bob no. {n}")
        print_bob(n-1) # Call itself and move towards terminating condition

print_bob(9)