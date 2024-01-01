#!/usr/bin/env python3
"""
Generate a year's worth of backdated commits to create an ECG heartbeat pattern
on GitHub's contribution graph.
"""

import subprocess
from datetime import datetime, timedelta

# ECG heartbeat pattern: commits per day for one cycle
# CRITICAL: GitHub aggregates by WEEK. The SVG shows WEEKLY totals, not daily!
# Ideal SVG: baseline=5/week, P-wave=7/week, spike=15/week, recovery=0/week
# Strategy: Spread commits across days to achieve desired weekly totals
# Each beat cycle = ~18 weeks (126 days) for 3 beats per year

HEARTBEAT_PATTERN = [
    # Baseline weeks: ~5 commits total = spread 1 commit across the week
    0, 0, 0, 1, 0, 0, 0,  # Week 1: baseline
    0, 0, 1, 0, 0, 0, 0,  # Week 2: baseline
    0, 0, 0, 0, 1, 0, 0,  # Week 3: baseline
    0, 1, 0, 0, 0, 0, 0,  # Week 4: baseline
    0, 0, 0, 1, 0, 0, 0,  # Week 5: baseline
    0, 0, 0, 0, 0, 1, 0,  # Week 6: baseline
    0, 0, 1, 0, 0, 0, 0,  # Week 7: baseline
    0, 0, 0, 0, 1, 0, 0,  # Week 8: baseline
    0, 1, 0, 0, 0, 0, 0,  # Week 9: baseline

    # P-wave week: ~7 commits = 1 per day
    1, 1, 1, 1, 1, 1, 1,  # Week 10: P-wave

    # Pre-spike baseline
    0, 0, 1, 0, 0, 0, 0,  # Week 11: baseline

    # Dip week: ~2 commits
    0, 0, 1, 0, 0, 1, 0,  # Week 12: dip

    # SPIKE week: ~15 commits on one day
    0, 0, 0, 15, 0, 0, 0,  # Week 13: SPIKE!

    # Recovery week: 0 commits
    0, 0, 0, 0, 0, 0, 0,  # Week 14: recovery

    # Return to baseline
    0, 0, 0, 1, 0, 0, 0,  # Week 15: baseline
    1, 0, 0, 0, 0, 0, 0,  # Week 16: baseline
    0, 0, 1, 0, 0, 0, 0,  # Week 17: baseline
    0, 0, 0, 0, 0, 1, 0,  # Week 18: baseline
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
