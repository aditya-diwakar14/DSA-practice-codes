def array_1d_ops():
    arr = [10, 20, 30, 40, 50]
    
    # Insertion at start (O(n))
    pos = 0
    shifts = len(arr) - pos
    arr.insert(pos, 5)
    print(f"Insert at {pos}: {arr}, Shifts: {shifts}")

    # Deletion from middle (O(n))
    pos_del = 2
    shifts_del = len(arr) - pos_del - 1
    arr.pop(pos_del)
    print(f"Delete at {pos_del}: {arr}, Shifts: {shifts_del}")

array_1d_ops()