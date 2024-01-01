#!/usr/bin/env python3
"""
Generate a year's worth of backdated commits to create an ECG heartbeat pattern
on GitHub's contribution graph.
"""

import subprocess
from datetime import datetime, timedelta

# ECG heartbeat pattern: commits per day for one cycle
# Pattern based on the ideal SVG: 3-4 beats per year
# Each beat cycle = ~90-120 days for proper spacing
# Baseline=1, P-wave=2, Dip=0, QRS spike=15-20, Recovery=0, then long baseline
HEARTBEAT_PATTERN = [
    1, 1, 1, 1, 1, 1, 1,  # Week 1: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 2: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 3: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 4: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 5: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 6: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 7: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 8: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 9: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 10: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 11: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 12: baseline
    1, 1, 2, 2, 1, 0, 0,  # Week 13: P-wave and dip before spike
    20, 0, 1, 1, 1, 1, 1, # Week 14: SPIKE then recovery to baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 15: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 16: baseline
    1, 1, 1, 1, 1, 1, 1,  # Week 17: baseline (cycle = 119 days ~4 months)
]

def generate_commit_dates(start_date, end_date, pattern):
    """
    Generate a list of (date, commit_count) tuples for the entire date range.

    Args:
        start_date: datetime object for the start date
        end_date: datetime object for the end date
        pattern: list of integers representing commits per day in one cycle

    Returns:
        List of (date_string, commit_count) tuples
    """
    commits = []
    current_date = start_date
    pattern_index = 0

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        commit_count = pattern[pattern_index % len(pattern)]
        commits.append((date_str, commit_count))

        current_date += timedelta(days=1)
        pattern_index += 1

    return commits

def create_backdated_commits(commits):
    """
    Create backdated git commits for each date with the specified count.

    Args:
        commits: List of (date_string, commit_count) tuples
    """
    total_commits = sum(count for _, count in commits)
    print(f"Creating {total_commits} commits across {len(commits)} days...")

    for date_str, count in commits:
        for i in range(count):
            # Create commit with backdated timestamp
            commit_message = f"Heartbeat on {date_str}"
            commit_date = f"{date_str} 12:00:00"

            # Use --allow-empty to avoid needing file changes
            # Set both author and committer dates
            result = subprocess.run([
                'git', 'commit',
                '--allow-empty',
                '--date', commit_date,
                '-m', commit_message
            ],
            env={'GIT_COMMITTER_DATE': commit_date},
            capture_output=True,
            text=True)

            if result.returncode != 0:
                print(f"Error creating commit for {date_str}: {result.stderr}")
                return False

    print(f"✓ Successfully created {total_commits} commits!")
    return True

def main():
    # Define date range: past year from today
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    print("GitHub Heartbeat Generator")
    print("=" * 50)
    print(f"Start date: {start_date.strftime('%Y-%m-%d')}")
    print(f"End date: {end_date.strftime('%Y-%m-%d')}")
    print(f"Pattern length: {len(HEARTBEAT_PATTERN)} days per cycle")
    print(f"Pattern: {HEARTBEAT_PATTERN}")
    print()

    # Generate commit schedule
    commits = generate_commit_dates(start_date, end_date, HEARTBEAT_PATTERN)
    total = sum(count for _, count in commits)

    print(f"This will create {total} commits.")
    response = input("Continue? (yes/no): ")

    if response.lower() not in ['yes', 'y']:
        print("Aborted.")
        return

    # Create commits
    success = create_backdated_commits(commits)

    if success:
        print()
        print("All commits created successfully!")
        print("Don't forget to push to GitHub: git push -f origin main")
        print()
        print("⚠️  Warning: This rewrites history. Use 'git push --force' carefully.")

if __name__ == "__main__":
    main()
