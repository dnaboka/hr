from argparse import Action, ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    """)
    parser.add_argument('--format', help="CSV or JSON (default)", default='JSON', choices=['json', 'csv'], type=str.lower),
    parser.add_argument('--path', help='filesystem path for storing the output')
    return parser

def main():
    import sys
    from hr import export, users as u

    args = create_parser().parse_args()
    users = u.fetch_users()

    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json_file(file, users)
    else:
        export.to_csv_file(file, users)
