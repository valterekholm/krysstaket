import math

# Definiera funktionen y
def y(x):
    return 90 * math.tan(x) + math.sqrt(49 + (7 * math.tan(x))**2)

# Definiera derivatan av y
def dy_dx(x):
    sec_x_squared = 1 / (math.cos(x)**2)  # sec(x)^2 = 1 / cos(x)^2
    term1 = 90 * sec_x_squared
    term2 = (7 * math.tan(x)) * 7 * sec_x_squared
    term2 /= math.sqrt(49 + (7 * math.tan(x))**2)
    return term1 + term2

# Newtons metod
def newtons_method(target_y, initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess
    for _ in range(max_iterations):
        fx = y(x) - target_y
        f_prime_x = dy_dx(x)
        
        if abs(fx) < tolerance:  # Om vi är tillräckligt nära målet
            return x
        
        if f_prime_x == 0:  # Undvik division med noll
            raise ValueError("Derivatan blev noll. Välj ett nytt startvärde.")
        
        x -= fx / f_prime_x  # Newtons metod-formeln
    
    raise ValueError("Maximalt antal iterationer överskridna. Lösningen konvergerade inte.")

# Använd funktionen för att hitta x där y = 70
try:
    initial_guess = 0.5  # Ett startvärde för x
    target_y = 70
    result_x = newtons_method(target_y, initial_guess)
    print(f"Lösningen är x ≈ {result_x}")
except Exception as e:
    print(f"Ett fel inträffade: {e}")
