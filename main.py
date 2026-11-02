import os

# Linear Congruential Generator (LCG) constants
# Classic parameters from "Numerical Recipes" / Donald Knuth's reference
A = 1664525
C = 1013904223
M = 2**32



def next_lcg(current_seed: int) -> int:
    """
    Generate the next pseudo-random number using the LCG formula.
    X_n+1 = (A * X_n + C) % M
    """
    return (A * current_seed + C) % M


def get_system_entropy() -> int:
    """
    Get 4 random bytes from the OS.
    Returns a random 32-bit number.
    """
    return int.from_bytes(os.urandom(4), byteorder="big")



def main() -> None:
    # Initialize the entropy pool using a mix of OS chaos and LCG
    state_seed = get_system_entropy()
    entropy_pool = []
    
    for _ in range(100):
        state_seed = next_lcg(state_seed)
        entropy_pool.append(state_seed)

    # Process and obfuscate elements
    for step in range(1, 51):
        # Select target index using system entropy
        target_idx = get_system_entropy() % 100
        buffered_value = entropy_pool[target_idx]

        # Dynamic decimal masking (obfuscate value length)
        dynamic_length = (get_system_entropy() % 10) + 1
        mask_modulus = 10**dynamic_length
        obfuscated_value = buffered_value % mask_modulus

        print(f"[{step:02d}]: {obfuscated_value}")

        # Pool state at the current index
        state_seed = next_lcg(state_seed)
        entropy_pool[target_idx] = state_seed




if __name__ == "__main__":
    main()