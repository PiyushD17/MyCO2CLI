import json
import click
import sys
sys.path.append('..')
from myco2cli.funcmodule import co2calc
# from funcmodule import co2calc

transport_help = """
                Mode of transport.Possible options: small-diesel-car,
                small-petrol-car,small-plugin-hybrid-car,
                small-electric-car, medium-diesel-car, medium-petrol-car,
                medium-plugin-hybrid-car, medium-electric-car,
                large-diesel-car, large-petrol-car,
                large-plugin-hybrid-car, large-electric-car, bus, train
                """
@click.command()

@click.option('--transportation-method','transport', required=True, \
help=transport_help, default="default")


@click.option('--distance', required=True,
help="Distance - by default in km. Please enter a numeric value. \
Please use the --unit-of-distance to change the unit.", default="default")

@click.option('--unit-of-distance','unit',
help="unit of distance: either m or km (default km).", default='km')

@click.option('--output',
help="Please specify the output units, either in kg or g.", default='na')

def main(transport, distance, unit, output):
    """A CLI Tool that calculates CO2 equivalent emissions
    for different vehicles. To use this tool, the transportation-method and
    distance arguments are mandatory.
    """
    if transport =='default' and distance=='default':
        print("Please provide --transportation-method and --distance arguments.\
         \nUse 'python main.py --help' for more info.")
    elif unit!='km' and unit!='m':
        print("Please provide appropriate units for distance, i.e 'km' or 'm'.")
    elif output!="na" and output!="kg" and output!="g":
        print("Please provide appropriate units for output, i.e. 'kg' or 'g'.")
    else:
        with open('emissions.json','r') as f:
            co2emissions = json.load(f)
        try:
            co2eq,op,u = co2calc(co2emissions[transport], \
            distance, unit, output)
            print(f'Your trip caused {co2eq}{op} of CO2-equivalent.')
        except ValueError as error:
            print("You have entered an invalid value for distance. \
Please provide numeric input for distance.")
        except KeyError as error:
            print("You have entered an invalid value for \
--transportation-method.")
            print("Please refer help for possible input options to \
--transportation-method. \nUse 'python main.py --help'")

if __name__ =="__main__":
    main()
