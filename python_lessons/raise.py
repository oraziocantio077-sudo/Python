a = int(input("Inserire età utente\n"))

if a > 120 or a  < 0:
    raise ValueError("età non verosimile")

class VehicleError(Exception):
    def __init__(self, message = "vehicle is broken"):
        super().__init__(message)

a = input()
if a > 9:
    raise VehicleError
