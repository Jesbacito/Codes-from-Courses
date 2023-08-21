def valikko():
    """otetaan ja tulostetaan arvo"""
    print(input(": "))

try:
    valikko()
    
except KeyboardInterrupt:
    print("Terve ja kiitos kaloista")
    