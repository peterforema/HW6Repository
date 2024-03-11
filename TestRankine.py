from Rankine import rankinee

def main():
    # Test Case 1: Saturated vapor entering turbine
    print("Test Case 1:")
    rankine1 = rankinee(p_high=8000, p_low=8, x1=1, name='Rankine Cycle 1')
    eff1 = rankine1.calc_efficiency()
    rankine1.print_summary()

    # Test Case 2: Superheated steam entering turbine
    print("\nTest Case 2:")
    T1_superheated = 1.7 * 179.9  # 179.9°C is the saturation temperature at 8000 kPa
    rankine2 = Rankine(p_high=8000, p_low=8, T1=T1_superheated, name='Rankine Cycle 2')
    eff2 = rankine2.calc_efficiency()
    rankine2.print_summary()

if __name__ == "__main__":
    main()
