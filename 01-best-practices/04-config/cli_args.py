"""
Best practices hands-on - Step 04a: command-line arguments with argparse.

Run:
  python3 cli_args.py --device-id sensor_1 --threshold 30
  python3 cli_args.py --help
"""

import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Process IoT sensor data.")
    parser.add_argument("--device-id", type=str, required=True,
                        help="ID of the device to process")
    parser.add_argument("--threshold", type=float, default=25.0,
                        help="temperature threshold (default: 25.0)")
    return parser

def main():
    args = build_parser().parse_args()          # reads sys.argv
    print(f"device_id = {args.device_id!r}  (str)")
    print(f"threshold = {args.threshold!r}  ({type(args.threshold).__name__}, converted by argparse)")

if __name__ == "__main__":
    main()
