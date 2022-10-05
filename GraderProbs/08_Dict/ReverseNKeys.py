def reverse(d: dict) -> dict:
    return { v:k for k, v in d.items()}

def keys(d, v):
    return [k for k, cv in d.items() if cv == v]
    
exec(input().strip())
