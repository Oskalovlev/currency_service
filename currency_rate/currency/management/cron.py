import subprocess

from django_cron import CronJobBase, Schedule


class UpdateRate(CronJobBase):

    RUN_EVERY_MINS = 1440
    RETRY_AFTER_FAILURE_MINS = 5
    RUN_AT_TIMES = ['15:55',]
    MIN_NUM_FAILURES = 3

    schedule = Schedule(
        run_every_mins=RUN_EVERY_MINS,
        retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS,
        run_at_times=RUN_AT_TIMES
    )
    code = "update_rate"

    def do(self):
        cmd = ["python", "currency_rate/manage.py", "update_currency_rate"]
        subprocess.run(cmd)
