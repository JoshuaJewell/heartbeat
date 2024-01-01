# GitHub Heartbeat

An artistic project that creates an ECG (electrocardiogram) heartbeat pattern on GitHub's contribution graph.

![Proof of concept](./previews/heartbeat.png)

## What is this?

This project manipulates GitHub's contribution graph to display a realistic ECG heartbeat pattern over the course of a year. By creating backdated commits with carefully calculated frequencies, the contribution graph shows three distinct heartbeats with proper ECG characteristics: P-waves, QRS complexes, T-waves, and recovery periods.

## How it works

GitHub's contribution graph displays **weekly aggregates** of commits, not daily values. Understanding this was crucial to creating the pattern.

### The Pattern

The script creates a repeating 18-week (126-day) cycle with the following structure:

- **Baseline weeks (9 weeks):** 1 commit spread across the week = ~1 commit/week on the graph
- **P-wave week:** 7 commits (1 per day) = ~7 commits/week (small bump before heartbeat)
- **Baseline week:** 1 commit
- **Dip week:** 2 commits = ~2 commits/week (slight dip before spike)
- **Spike week:** 15 commits on one day = ~15 commits/week (the QRS complex - main heartbeat!)
- **Recovery week:** 0 commits = flat line after heartbeat
- **Return to baseline (4 weeks):** 1 commit/week

This pattern repeats ~3 times across a year, creating three distinct heartbeats.

### Implementation

The `generate_heartbeat.py` script:

1. Defines the daily commit pattern for one 126-day cycle
2. Repeats the pattern across the past year
3. Creates empty backdated commits using `git commit --allow-empty --date`
4. Sets both author and committer dates to ensure GitHub recognizes the backdated commits

### Key Insights

- GitHub aggregates contributions by week, not by day
- Empty commits are sufficient to create the pattern
- Both `--date` (author date) and `GIT_COMMITTER_DATE` (committer date) must be set
- The pattern must account for weekly totals, not daily commit counts

## Usage

```bash
python3 generate_heartbeat.py
```

The script will:
- Generate commits for the past 365 days
- Show you the pattern and total commit count
- Ask for confirmation before creating commits
- Create all commits with proper backdating
- Provide instructions for pushing to GitHub

**Warning:** This rewrites git history. Use `git push --force` to update the remote repository.

## Technical Details

- **Total commits:** ~112 per year (plus 1 for project files)
- **Cycle length:** 126 days (18 weeks)
- **Heartbeats per year:** 3
- **Spike intensity:** 15 commits/week
- **Baseline intensity:** 1 commit/week

## Why?

An exploration of GitHub's contribution graph mechanics and a creative exercise in data visualization through commit manipulation.

## License

GNU Affero General Public License v3.0
