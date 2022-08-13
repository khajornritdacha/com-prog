from time import monotonic


def mosteller(w, h):
 # return the body surface area of a person
 # based on body weight (w) and height (h)
 # using Mosteller formula
 mosteller = ((w*h)**0.5) / 60
 return mosteller

def du_bois(w, h):
 # return the body surface area of a person
 # based on body weight (w) and height (h)
 # using Du Bois formula
 du_bois = 0.007184 * (w**0.425) * (h**0.725)
 return du_bois

def fujimoto(w, h):
 # return the body surface area of a person
 # based on body weight (w) and height (h)
 # using Fujimoto formula
 fujimoto = 0.008883 * (w**0.444) * (h**0.663)
 return fujimoto
 
def main():
 weight = float(input())
 height = float(input())
 print("Mosteller =", round(mosteller(weight, height), 5))
 print("Du Bois =", round(du_bois(weight, height), 5))
 print("Fujimoto =", round(fujimoto(weight, height), 5))
exec(input()) # DON'T remove this line