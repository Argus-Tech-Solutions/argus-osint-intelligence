import socket, whois, json

def domain_recon(domain: str) -> dict:
    result = {}
    try:
        result["ip"] = socket.gethostbyname(domain)
        w = whois.whois(domain)
        result["registrar"] = w.registrar
        result["creation_date"] = str(w.creation_date)
        result["expiration_date"] = str(w.expiration_date)
    except Exception as e:
        result["error"] = str(e)
    return result

if __name__ == "__main__":
    data = domain_recon("example.com")
    print(json.dumps(data, indent=2))
