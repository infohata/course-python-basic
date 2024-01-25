from datetime import datetime

def trukme(funkcija):
    def wrapper(*args, **kwargs):
        # print("pradedam matuoti")
        start = datetime.now()
        rezultatas = funkcija(*args, **kwargs)
        end = datetime.now()
        duration = end - start
        if duration.seconds > 0:
            print(f"funkcijos vykdymo trukme: {duration}")
        elif duration.microseconds >= 1000:
            print(f"funkcijos vykdymo trukme: {duration.microseconds} mikrosekundziu")
        return rezultatas
    return wrapper

@trukme
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

@trukme
def generate_primes(end, start=1):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print(len(generate_primes(1000000)))
