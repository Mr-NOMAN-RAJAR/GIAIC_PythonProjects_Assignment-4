def main():

    fahrenheit = float(input("\033[1;3m Inter the Temprature in Fehrenheit : \033[0m"));
    degree_selsius = (fahrenheit - 32) * 5.0/9.0

    print(f"temprature : {fahrenheit} F = {degree_selsius}C")

    
if __name__ == "__main__":
    main()