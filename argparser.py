import argparse

"""
Example usage:
> python3 argparser.py sara
hello, sara from Hannover

> python3 argparser.py sara --city 'new york'
hello, sara from new york
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Say a Greeting.')
    parser.add_argument('--city', type=str, default="Hannover",
                        help="Where is there person from?")
    parser.add_argument('name', type=str)

    args = parser.parse_args()
    city = args.city
    name = args.name

    print(f'hello, {name} from {city}')