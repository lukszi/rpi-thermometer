from information_provider.RESTInformationProvider import RESTInformationProvider

if __name__ == "__main__":
    prov = RESTInformationProvider("http://msu.oph.rwth-aachen.de/")
    print(prov["temperature"])
