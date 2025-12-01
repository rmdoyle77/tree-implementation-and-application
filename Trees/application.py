import argparse
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Dict

from segment_tree import SegmentTree  # local file import


DATE_FMT = "%Y-%m-%d"


def read_csv(path: Path) -> tuple[List[str], List[float]]:
    dates: List[str] = []
    vals: List[float] = []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row["date"])
            vals.append(float(row["close"]))
    return dates, vals


def parse_date_idx(date_to_idx: Dict[str, int], s: str) -> int:
    datetime.strptime(s, DATE_FMT)
    if s not in date_to_idx:
        raise SystemExit(f"Date {s} not found in series")
    return date_to_idx[s]


def main() -> None:
    parser = argparse.ArgumentParser(description="StockScope Segment Tree CLI")
    parser.add_argument(
        "--data",
        required=True,
        help="Path to CSV with columns: date,close (in ascending date order)",
    )

    sub = parser.add_subparsers(dest="cmd", required=True)

    for name in ("sum", "min", "max"):
        sp = sub.add_parser(name)
        sp.add_argument("left", help="left date (YYYY-MM-DD)")
        sp.add_argument("right", help="right date (YYYY-MM-DD)")

    sp_update = sub.add_parser("update")
    sp_update.add_argument("date", help="date (YYYY-MM-DD)")
    sp_update.add_argument("value", type=float, help="new close value")

    sub.add_parser("all")

    args = parser.parse_args()

    data_path = Path(args.data)
    dates, vals = read_csv(data_path)
    date_to_idx = {d: i for i, d in enumerate(dates)}

    st = SegmentTree(vals)

    if args.cmd in {"sum", "min", "max"}:
        l = parse_date_idx(date_to_idx, args.left)
        r = parse_date_idx(date_to_idx, args.right)
        if l > r:
            l, r = r, l

        if args.cmd == "sum":
            result = st.query_sum(l, r)
            print(f"SUM {args.left}..{args.right} = {result}")
        elif args.cmd == "min":
            result = st.query_min(l, r)
            print(f"MIN {args.left}..{args.right} = {result}")
        else:
            result = st.query_max(l, r)
            print(f"MAX {args.left}..{args.right} = {result}")

    elif args.cmd == "update":
        i = parse_date_idx(date_to_idx, args.date)
        st.update(i, args.value)
        print(f"Updated {args.date} -> {args.value}")

    else:  
        s, mn, mx = st.query_all()
        print(f"ALL: sum={s}, min={mn}, max={mx}")


if __name__ == "__main__":
    main()
