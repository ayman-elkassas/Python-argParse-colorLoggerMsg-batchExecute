import argparse
import sys
from utils.logger import Logger


def main():
    try:
        parser = argparse.ArgumentParser(description='Description : Calculator two num')
        parser.add_argument('-x', '--x', type=float,required=False, default=1, help='What is the first num?')
        parser.add_argument('-y', '--y', type=float,required=False, default=1, help='What is the second num?')
        parser.add_argument('-op', '--op', type=str,required=False, default='add', help='What operation? (add,sub,mul, or div')

        # todo:fetch all args
        # vars -> take object and convert all object attr to dictionary
        args = vars(parser.parse_args())

        Logger.log.info("first num is {} "
                        "and second is : {} "
                        "ops is : {} EXECUTE NOW OPR !"
                        .format(args['x'],args['y'],args['op']))

        Logger.log.error('Error')
        Logger.log.warning('Warning')
        Logger.log.critical('Success Calculation')

        # write return value
        sys.stdout.write(str(calc(args)))

    except argparse.ArgumentError as exc:
        print(exc.message, '\n', exc.argument)


def calc(args):
    if args['op'] == 'add':
        return args['x'] + args['y']
    elif args['op'] == 'sub':
        return args['x'] - args['y']
    elif args['op'] == 'mul':
        return args['x'] * args['y']
    elif args['op'] == 'div':
        return args['x'] / args['y']


if __name__ == "__main__":
    main()

# CLI Execute
# python CalcArgParse.py -x=5 -y=10 -op=add
